import blob
import time
import random
import re
import sys
if sys.argv[1]:
    blob.initialize(sys.argv[1], "assistant")
else:
    print("人格フォルダを指定してください。")
    exit()


import threading
import asyncio
from rapidfuzz.distance import Levenshtein
import datetime


if len(blob.DATA.data["sentence"]) >= 10000:
    mode = blob.DATA.settings["defaultMode"]
else:
    mode = 1

print("mode: {}".format(mode))
print("sentences: {}".format(len(blob.DATA.data["sentence"])))

def setMode(x):
    global mode, channel
    mode = x
    print("mode: {}".format(mode))

import requests
def speak_bouyomi(text='ゆっくりしていってね'):
    time.sleep(1)
    res = requests.get(
        'http://localhost:50080/Talk',
        params={
            'text': text,
            'voice': blob.DATA.settings["yukkuri"]["voice"],
            'volume': blob.DATA.settings["yukkuri"]["volume"],
            'speed': blob.DATA.settings["yukkuri"]["speed"],
            'tone': blob.DATA.settings["yukkuri"]["tone"]})
    return res.status_code

kaisu = 0
def speak(result):
    global mode, kaisu
    pattern = re.compile(r"^[!/]command")
    results = result.split("\n")

    Message = ""
    for result in results:
        if bool(pattern.search(result)):
            com = result.split(" ")
            if com[1] == "setMode":
                setMode(int(com[2]))
            elif com[1] == "saveMyData":
                blob.MEMORY.saveData()
        else:
            Message += result + "\n"
    Message = Message[:-1]
    if Message != "":
        speak_bouyomi(Message)
                



import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

into = "こんにちは"

def listen():
    global messages, people, lastMessage
    while True:
        
        print("聞き取っています...")
        
        with mic as source:
            r.adjust_for_ambient_noise(source) #雑音対策
            audio = r.listen(source)

        print ("解析中...")

        try:
            into = r.recognize_google(audio, language=blob.DATA.settings["languageHear"])
            print(into)

            if Levenshtein.normalized_similarity(into, blob.DATA.lastSentence) < 0.85:



                if bool(re.search("沈黙モード|黙|だま", into)) and bool(re.search(blob.DATA.settings["mynames"], into)):
                    setMode(0)
                    return
                elif bool(re.search("寡黙モード|静かに|しずかに", into)) and bool(re.search(blob.DATA.settings["mynames"], into)):
                    setMode(1)
                    return
                elif bool(re.search("通常モード|喋って|話して|しゃべって|はなして", into)) and bool(re.search(blob.DATA.settings["mynames"], into)):
                    setMode(2)
                    return
                elif bool(re.search("セーブして", into)) and bool(re.search(blob.DATA.settings["mynames"], into)):
                    blob.receive("!command saveMyData", "あなた")
                    print("セーブします")
                    blob.MEMORY.save()
                    print("完了")
                    return
                else:
                    blob.receive(into, "あなた")
                    
                    if mode == 1:
                        if bool(re.search(blob.DATA.settings["mynames"], into)):
                            result = blob.speakFreely()
                            if result == None:
                                pass
                            else:
                                speak(result)
                    elif mode == 2:
                        result = blob.speakFreely()
                        if result == None:
                            pass
                        else:
                            speak(result)





        # 以下は認識できなかったときに止まらないように。
        except sr.UnknownValueError:
            if mode == 2:
                if blob.DATA.myVoice != None:
                    a = blob.nextNode(force=True)
                    if a:
                        result = blob.speakFreely()
                        speak(result)
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


listen()