import requests
import pyaudio
import re
import time

host = "127.0.0.1"
port = 50021 # VOICEVOXデフォルト

def play_voicevox(text, speaker=2):
    # 1. クエリ作成
    res1 = requests.post(f"http://{host}:{port}/audio_query", params={"text": text, "speaker": speaker})
    # 2. 音声合成
    res2 = requests.post(f"http://{host}:{port}/synthesis", params={"speaker": speaker}, json=res1.json())
    
    audio_data = res2.content
    # 3. 再生 (PyAudioを使用)
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=24000, output=True)
    stream.write(audio_data)
    stream.stop_stream()
    stream.close()
    p.terminate()

import mojihocori
import sys
import threading

if sys.argv[1]:
    cronThread = threading.Thread(target=mojihocori.initialize, args=(sys.argv[1], "discord"), daemon=True)
    cronThread.start()
else:
    cronThread = threading.Thread(target=mojihocori.initialize, args=("main", "discord"), daemon=True)
    cronThread.start()
time.sleep(1)

mode = mojihocori.DATA.settings["defaultMode"]
def setMode(x):
    global mode
    mode = x
    print("mode: {}".format(mode))

def speak(x):
    print(x)
    com = x.split(" ")
    if com[0] == "!command":
        return
    play_voicevox(x)

import pyaudio
import numpy as np
from faster_whisper import WhisperModel

# モデルは軽量なものか、turboを推奨
model = WhisperModel("small", device="cpu")

RATE = 16000
CHUNK = 1024
# 判定用設定
SILENCE_WAIT = 0.8  # 何秒無音が続いたら「言い終わり」とするか
THRESHOLD = 0.02    # 声かどうかの音量しきい値（環境に合わせて調整）

audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)

print("リスニング中...")

audio_buffer = []
silent_chunks = 0
is_speaking = False

try:
    while True:
        data = stream.read(CHUNK)
        audio_int16 = np.frombuffer(data, dtype=np.int16)
        audio_float32 = audio_int16.astype(np.float32) / 32768.0
        
        # 1. 音量で簡易VAD（軽い処理）
        max_vol = np.max(np.abs(audio_float32))
        
        if max_vol > THRESHOLD:
            if not is_speaking:
                is_speaking = True
                print("録音中...")
            audio_buffer.append(audio_int16)
            silent_chunks = 0
        elif is_speaking:
            audio_buffer.append(audio_int16)
            silent_chunks += 1
            
            # 2. 指定時間以上無音が続いたら「言い終わり」と判断
            if silent_chunks > int(RATE / CHUNK * SILENCE_WAIT):
                print("推論中...")
                full_audio = np.concatenate(audio_buffer).astype(np.float32) / 32768.0
                
                # ここで初めてWhisperを呼ぶ（重い処理を1回だけ）
                segments, _ = model.transcribe(full_audio, beam_size=1, language=mojihocori.DATA.settings["languageHear"], vad_filter=True) # beam_size=1で高速化
                for s in segments:
                    print(f"結果: {s.text}")
                    
                    into = s.text
                    if bool(re.search("沈黙モード|黙|だま", into)) and bool(re.search(mojihocori.DATA.settings["mynames"]+"|モジホコリ、", into)):
                        mojihocori.receive("!command setMode 0", "あなた")
                        setMode(0)
                        continue
                    if bool(re.search("寡黙モード|静かに|しずかに", into)) and bool(re.search(mojihocori.DATA.settings["mynames"]+"|モジホコリ、", into)):
                        mojihocori.receive("!command setMode 1", "あなた")
                        setMode(1)
                        continue
                    if bool(re.search("通常モード|喋って|話して|しゃべって|はなして", into)) and bool(re.search(mojihocori.DATA.settings["mynames"]+"|モジホコリ、", into)):
                        mojihocori.receive("!command setMode 2", "あなた")
                        setMode(2)
                        continue
                    if bool(re.search("饒舌モード", into)) and bool(re.search(mojihocori.DATA.settings["mynames"]+"|モジホコリ、", into)):
                        mojihocori.receive("!command setMode 3", "あなた")
                        setMode(3)
                        continue
                    if bool(re.search("セーブして", into)) and bool(re.search(mojihocori.DATA.settings["mynames"], into)):
                        mojihocori.receive("!command saveMyData", "あなた")
                        print("セーブします")
                        mojihocori.MEMORY.saveData()
                        print("完了")
                        continue
                    mojihocori.receive(into, "あなた")
                    result = mojihocori.speakFreely()
                    if result == None:
                        pass
                    else:
                        speak(result)
                    
                # リセット
                audio_buffer = []
                silent_chunks = 0
                is_speaking = False
                print("リスニング中...")

except KeyboardInterrupt:
    pass
finally:
    stream.stop_stream()
    stream.close()
    audio.terminate()