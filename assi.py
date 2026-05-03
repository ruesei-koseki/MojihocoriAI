import requests
import pyaudio
import re
import time
import mojihocori
import sys
import threading
import random

if sys.argv[1]:
    cronThread = threading.Thread(target=mojihocori.initialize, args=(sys.argv[1], "discord"), daemon=True)
    cronThread.start()
else:
    cronThread = threading.Thread(target=mojihocori.initialize, args=("main", "discord"), daemon=True)
    cronThread.start()
time.sleep(1)


host = "127.0.0.1"
port = 50021 # VOICEVOXデフォルト
isSpeaking = False

def play_voicevox(text, speaker=mojihocori.DATA.settings["defaultMode"]):
    global isSpeaking
    # 1. クエリ作成
    res1 = requests.post(f"http://{host}:{port}/audio_query", params={"text": text, "speaker": speaker})
    # 2. 音声合成
    res2 = requests.post(f"http://{host}:{port}/synthesis", params={"speaker": speaker}, json=res1.json())
    
    audio_data = res2.content
    # 3. 再生 (PyAudioを使用)
    isSpeaking = True
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=24000, output=True)
    stream.write(audio_data)
    stream.stop_stream()
    stream.close()
    p.terminate()
    isSpeaking = False

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


import numpy as np
from faster_whisper import WhisperModel

# モデルは軽量なものか、turboを推奨
model = WhisperModel("small", device="cpu", compute_type="int8")

RATE = 16000
CHUNK = 1024
# 判定用設定
SILENCE_WAIT = 0.8  # 何秒無音が続いたら「言い終わり」とするか
THRESHOLD = 0.02    # 声かどうかの音量しきい値（環境に合わせて調整）

audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)

print("リスニング中...")

audio_buffer = []
audio_subbuffer = []
silent_chunks = 0
silent_subchunks = 0
is_speaking = False
is_speaking_sub = False


import cv2
import imagehash
from PIL import Image

def image():
    stop_event = threading.Event()
    cap = cv2.VideoCapture(0)
    image = None
    while True:
        ret, frame = cap.read()
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(rgb_frame)
        dhash = imagehash.dhash(pil_img)
        if image:
            if dhash - image > 10:
                image = dhash
                mojihocori.receive("視覚刺激: {}".format(image), "!system")
                if not isSpeaking and not is_speaking:
                    if mode == 1:
                        if bool(re.search(mojihocori.DATA.settings["mynames"], into)) and mojihocori.DATA.myVoice != None:
                            result = mojihocori.speakFreely()
                            if result == None:
                                pass
                            else:
                                speak(result)
                    if mode >= 2:
                        if (bool(re.search(mojihocori.DATA.settings["mynames"], into)) or random.randint(0, 3) == 0) and mojihocori.DATA.myVoice != None:
                            result = mojihocori.speakFreely()
                            if result == None:
                                pass
                            else:
                                speak(result)
        else:
            image = dhash
            mojihocori.receive("視覚刺激: {}".format(image), "!system")
            if not isSpeaking and not is_speaking:
                if mode == 1:
                    if bool(re.search(mojihocori.DATA.settings["mynames"], into)) and mojihocori.DATA.myVoice != None:
                        result = mojihocori.speakFreely()
                        if result == None:
                            pass
                        else:
                            speak(result)
                if mode >= 2:
                    if (bool(re.search(mojihocori.DATA.settings["mynames"], into)) or random.randint(0, 3) == 0) and mojihocori.DATA.myVoice != None:
                        result = mojihocori.speakFreely()
                        if result == None:
                            pass
                        else:
                            speak(result)
        stop_event.wait(timeout=0.5)


cronThread = threading.Thread(target=image, daemon=True)
cronThread.start()


from PIL import Image
import imagehash

def audio_to_dhash(audio_data):
    # audio_data: np.frombufferで取得したnp.int16配列
    
    # 1. 音声を短く分割してFFT（高速フーリエ変換）をかける
    # 例: 8x8の画像にしたい場合
    chunks = np.array_split(audio_data, 720)
    spectrogram = []
    for chunk in chunks:
        fft = np.abs(np.fft.rfft(chunk)) # 低解像度で十分
        spectrogram.append(fft[:8]) # 必要な周波数成分を抽出
    
    # 2. 2次元配列（画像）に変換
    spec_array = np.array(spectrogram)
    
    # 3. 0-255に正規化してPIL画像化
    spec_norm = ((spec_array - spec_array.min()) * (255 / (spec_array.max() - spec_array.min() + 1e-6))).astype(np.uint8)
    pil_img = Image.fromarray(spec_norm)
    
    # 4. dhash適用
    return imagehash.dhash(pil_img)

# 使い方
# hash_val = audio_to_dhash(np.frombuffer(in_data, dtype=np.int16))

import datetime
mojihocori.receive("通知: 貴方は目を覚ましました。", "!system", reply=True)
dt_now = datetime.datetime.now()
mojihocori.receive(dt_now.strftime('%Y / %m / %d %H : %M : %S'), "!systemClock")

oto = None
renzokuC = 0
try:
    while True:
        if not isSpeaking:
            data = stream.read(CHUNK)
            audio_int16 = np.frombuffer(data, dtype=np.int16)
            audio_float32 = audio_int16.astype(np.float32) / 32768.0
            
            # 1. 音量で簡易VAD（軽い処理）
            max_vol = np.max(np.abs(audio_float32))

            if max_vol > THRESHOLD:
                if not is_speaking_sub:
                    is_speaking_sub = True
                audio_subbuffer.append(audio_int16)
                silent_subchunks = 0
            elif is_speaking_sub:
                audio_subbuffer.append(audio_int16)
                silent_subchunks += 1
            if silent_subchunks > int(RATE / CHUNK * SILENCE_WAIT):
                full_audio = np.concatenate(audio_subbuffer).astype(np.float32) / 32768.0
                audio_subbuffer = []
                
                dhash = audio_to_dhash(full_audio)

                if oto:
                    if dhash - oto > 10:
                        oto = dhash
                        mojihocori.receive("聴覚刺激: {}".format(oto), "!system")
                        if not isSpeaking and not is_speaking:
                            if mode == 1:
                                if bool(re.search(mojihocori.DATA.settings["mynames"], into)) and mojihocori.DATA.myVoice != None:
                                    result = mojihocori.speakFreely()
                                    if result == None:
                                        pass
                                    else:
                                        speak(result)
                            if mode >= 2:
                                if (bool(re.search(mojihocori.DATA.settings["mynames"], into)) or random.randint(0, 3) == 0) and mojihocori.DATA.myVoice != None:
                                    result = mojihocori.speakFreely()
                                    if result == None:
                                        pass
                                    else:
                                        speak(result)
                else:
                    oto = dhash
                    mojihocori.receive("聴覚刺激: {}".format(oto), "!system")
                    if not isSpeaking and not is_speaking:
                        if mode == 1:
                            if bool(re.search(mojihocori.DATA.settings["mynames"], into)) and mojihocori.DATA.myVoice != None:
                                result = mojihocori.speakFreely()
                                if result == None:
                                    pass
                                else:
                                    speak(result)
                        if mode >= 2:
                            if (bool(re.search(mojihocori.DATA.settings["mynames"], into)) or random.randint(0, 3) == 0) and mojihocori.DATA.myVoice != None:
                                result = mojihocori.speakFreely()
                                if result == None:
                                    pass
                                else:
                                    speak(result)
                audio_subbuffer = []
                silent_subchunks = 0
                is_speaking_sub = False

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
                    segments, _ = model.transcribe(full_audio, beam_size=10, language=mojihocori.DATA.settings["languageHear"], vad_filter=True) # beam_size=1で高速化
                    kazu = 0
                    for s in segments:
                        renzokuC = 0
                        print(f"結果: {s.text}")
                        
                        into = s.text
                        if bool(re.search("沈黙モード|黙|だま", into)) and bool(re.search(mojihocori.DATA.settings["mynames"]+"|モジホコリ、", into)):
                            mojihocori.receive("!command setMode 0", "あなた")
                            setMode(0)
                            # リセット
                            audio_buffer = []
                            silent_chunks = 0
                            is_speaking = False
                            print("リスニング中...")
                            continue
                        if bool(re.search("寡黙モード|静かに|しずかに", into)) and bool(re.search(mojihocori.DATA.settings["mynames"]+"|モジホコリ、", into)):
                            mojihocori.receive("!command setMode 1", "あなた")
                            setMode(1)
                            # リセット
                            audio_buffer = []
                            silent_chunks = 0
                            is_speaking = False
                            print("リスニング中...")
                            continue
                        if bool(re.search("通常モード|喋って|話して|しゃべって|はなして", into)) and bool(re.search(mojihocori.DATA.settings["mynames"]+"|モジホコリ、", into)):
                            mojihocori.receive("!command setMode 2", "あなた")
                            setMode(2)
                            # リセット
                            audio_buffer = []
                            silent_chunks = 0
                            is_speaking = False
                            print("リスニング中...")
                            continue
                        if bool(re.search("饒舌モード", into)) and bool(re.search(mojihocori.DATA.settings["mynames"]+"|モジホコリ、", into)):
                            mojihocori.receive("!command setMode 3", "あなた")
                            setMode(3)
                            # リセット
                            audio_buffer = []
                            silent_chunks = 0
                            is_speaking = False
                            print("リスニング中...")
                            continue
                        if bool(re.search("セーブして", into)) and bool(re.search(mojihocori.DATA.settings["mynames"], into)):
                            mojihocori.receive("!command saveMyData", "あなた")
                            print("セーブします")
                            mojihocori.MEMORY.saveData()
                            print("完了")
                            # リセット
                            audio_buffer = []
                            silent_chunks = 0
                            is_speaking = False
                            print("リスニング中...")
                            continue
                        mojihocori.receive(into, "あなた")
                        if not isSpeaking:
                            if mode == 1:
                                if bool(re.search(mojihocori.DATA.settings["mynames"], into)) and mojihocori.DATA.myVoice != None:
                                    result = mojihocori.speakFreely()
                                    if result == None:
                                        pass
                                    else:
                                        speak(result)
                            if mode >= 2:
                                if (bool(re.search(mojihocori.DATA.settings["mynames"], into)) or random.randint(0, 3) == 0) and mojihocori.DATA.myVoice != None:
                                    result = mojihocori.speakFreely()
                                    if result == None:
                                        pass
                                    else:
                                        speak(result)
                        kazu += 1
                    if kazu == 0:
                        if renzokuC == 0:
                            dt = datetime.datetime.now()
                            mojihocori.receive("!command ignore", mojihocori.DATA.lastUser)
                            pattern = re.compile(r"(0|3)0 : [0-9][0-9]$")
                            if bool(pattern.search(dt.strftime('%Y/%m/%d %H:%M:%S'))):
                                mojihocori.receive(dt.strftime('%Y/%m/%d %H:%M:%S'), "!systemClock")
                            print("沈黙を検知")
                        renzokuC += 1
                        
                        
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