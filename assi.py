import mojihocori
import sys
import re
import datetime

if sys.argv[1] and sys.argv[2]:
    mojihocori.initialize(sys.argv[1], "discord")
else:
    print("人格フォルダとコーパスを指定してください。")
    exit()

def speak(x):
    print(x)


import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

into = "こんにちは"

def listen():
    while True:
        
        print("聞き取っています...")
        
        with mic as source:
            r.adjust_for_ambient_noise(source) #雑音対策
            audio = r.listen(source)

        print ("解析中...")

        try:
            into = r.recognize_google(audio, language=mojihocori.DATA.settings["languageHear"])
            print(into)
            if bool(re.search("セーブして", into)) and bool(re.search(mojihocori.DATA.settings["mynames"], into)):
                mojihocori.receive("!command saveMyData", "あなた")
                print("セーブします")
                mojihocori.MEMORY.saveData()
                print("完了")
            else:
                a = 0
                b = ""
                c = []
                for intoo in into.split():
                    if a >= 4:
                        c.append(b)
                        b = ""
                        a = 0
                    else:
                        if a != 0:
                            b += " "
                    b += intoo
                    a += 1
                if b != "":
                    c.append(b)
                    b = ""
                    a = 0
                for cc in c:
                    mojihocori.receive(into, "あなた")
                    result = mojihocori.speakFreely()
                    if result == None:
                        pass
                    else:
                        speak(result)

        # 以下は認識できなかったときに止まらないように。
        except sr.UnknownValueError:
            dt = datetime.datetime.now()
            mojihocori.receive("!command ignore", "あなた")
            print("沈黙を検知")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


import threading
cronThread = threading.Thread(target=listen, daemon=True)
cronThread.start()