import blob
import time
import random
import re
import sys
if sys.argv[1]:
    blob.initialize(sys.argv[1], "discord")
else:
    print("人格フォルダを指定してください。")
    exit()

persons = [[blob.DATA.settings["myname"], 0]]
channel = None
lastMessage = ""
lastUsername = "誰か"
messages = []
prevTime = time.time()
pin = False

from discord.ext import tasks
import discord
import threading
import asyncio
from rapidfuzz.distance import Levenshtein
import datetime

helpMessage = f"""==blobAIヘルプ==
このbotはユーザーのメッセージに自分の意思で返信するAIです。
話している人数に応じて返信頻度を下げます。
botの名前を呼ぶとそのチャンネルに来てくれます。
メンションでは呼べません。

=学習方法=
以下のコマンドで学習します。
```
さとみちゃん！ぎゅー！===ちょっと[YOU]！えっち！
```
[YOU]という文字列は実際に発言する際ユーザー名に置き換えられます。

=配慮コマンドについて=
botに「静かにして」というと「寡黙モード」になり、メッセージにbotの名前が含まれない限り返信しなくなります。
botに「話して」というと「通常モード」になり、メッセージに通常通りbotの名前が含まれてなくても人数に応じて頻度を変えて返信します。
botに「じっとしてて」というと、チャンネルを動かなくなります。
botに「動いて」というと、チャンネルを動けるようになります。
"""

# 自分のBotのアクセストークンに置き換えてください
TOKEN = blob.DATA.settings["discToken"]
# 接続に必要なオブジェクトを生成
intents = discord.Intents.all()
client = discord.Client(intents=intents)
mode = 2

print("mode: {}".format(mode))
print("sentences: {}".format(len(blob.DATA.data["sentence"])))

def setMode(x):
    global mode, channel
    mode = x
    print("mode: {}".format(mode))

draft = ""
async def speak(result):
    global channel, persons, prevTime, mode, pin, draft
    global lastMessage, prevTime, messages
    try:
        print("{}: {}".format(blob.DATA.settings["myname"], result))
        #result = re.sub(r'@(everyone|here|[!&]?[0-9]{17,21})', '@\u200b\\1', result)
        pattern = re.compile(r"^[!/]command")
        print("users: {}".format(persons))
        results = result.split("\n")

        Message = ""
        for result in results:
            if bool(pattern.search(result)):
                com = result.split(" ")
                if com[1] == "discMove" and not pin:
                    if client.get_channel(int(com[2])) != None:
                        try:
                            channel = client.get_channel(int(com[2]))
                        except:
                            print("チャンネルが存在しません")
                        persons = [[blob.DATA.settings["myname"], 0]]
                        try:
                            print("チャンネルを移動しました: {}".format(channel.name))
                        except:
                            print("チャンネルを移動しました: DM")
                    else:
                        blob.receive("エラー: あなたは固定されています。", "!system")
                        print("エラー: あなたは固定されています。")
                elif com[1] == "ignore":
                    pass
                elif com[1] == "setMode":
                    setMode(int(com[2]))
                elif com[1] == "saveMyData":
                    blob.MEMORY.save()
                elif com[1] == "pin":
                    pin = True
                elif com[1] == "unpin":
                    pin = False
                elif com[1] == "saveMyData":
                    blob.MEMORY.save()
            else:
                Message += result + "\n"
        Message = Message[:-1]
        if Message != "":
            async with channel.typing():
                if len(Message) / (mode * 3) <= 1:
                    await asyncio.sleep(len(Message) / (mode * 3))
                else:
                    await asyncio.sleep(1)
                await channel.send(Message)
        if mode == 3:
            draft = "入力: {}\n出力ドラフト: {}".format(lastMessage, result)
            for i in range(random.randint(0,10)):
                blob.receive(draft, "!system")
                result = blob.speakFreely()
                async with channel.typing():
                    if len(result) / (mode * 3) <= 1:
                        await asyncio.sleep(len(result) / (mode * 3))
                    else:
                        await asyncio.sleep(1)
                    await channel.send(result)
                draft += "\n"+result
            draft = ""
        prevTime = time.time()
    except:
        import traceback
        traceback.print_exc()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    global lastMessage, prevTime, messages
    print('ログインしました')
    cron.start()
    blob.receive("通知: 貴方は目を覚ましました。", "!system")
    print("通知: 貴方は目を覚ましました。")

ii = 0
learnMemory = ""
# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    global pin, channel, persons, prevTime, lastMessage, messages, helpMessage, learnMemory, prevTime, lastUsername, ii, mode
    ff = False
    parts = message.content.split("\n")
    for part in parts:
        if bool(re.search("(.*?)===(.*?)", part)):
            learnMemory = ""
            blob.MEMORY.learnSentence(part.split("===")[0], "!input")
            blob.MEMORY.learnSentence(part.split("===")[1], "!output")
            learnMemory = "入力: {}\n出力ドラフト: {}".format(part.split("===")[0], part.split("===")[1])
            ff = True
        if bool(re.search("\+==(.*?)", part)):
            blob.MEMORY.learnSentence(learnMemory, "!input")
            blob.MEMORY.learnSentence(part.replace("+==", ""), "!output")
            learnMemory += "\n" + part.replace("+==", "")
            ff = True
    learnMemory = ""
    if ff:
        return
    if message.channel == channel or bool(re.search(blob.DATA.settings["mynames"], message.content)) or isinstance(message.channel, discord.DMChannel):
        prevTime = time.time()
        username = message.author.name.split("#")[0]
        if message.channel != channel:
            try:
                print("チャンネルを移動しました: {}".format(message.channel.name))
            except:
                print("チャンネルを移動しました: {}のDM".format(username))
            channel = message.channel
            persons = [[blob.DATA.settings["myname"], 0]]
        if message.author == client.user:
            return
        pss = []
        for ps in persons:
            pss.append(ps[0])
        if username not in pss:
            persons.append([username, 0])
        if message.content == "":
            return
        if message.content == None:
            return        
        additional = ""
        for attachment in message.attachments:
            additional += "\n" + attachment.url
        message.content += additional
        if bool(re.search("silent mode|沈黙モード|黙っ|だま", message.content)) and bool(re.search(blob.DATA.settings["mynames"], message.content)):
            setMode(0)
            return
        elif bool(re.search("only for mention mode|寡黙モード|静かに|しずかに", message.content)) and bool(re.search(blob.DATA.settings["mynames"], message.content)):
            setMode(1)
            blob.receive("!command setMode {}".format(1), username)
            return
        elif bool(re.search("normal mode|通常モード|喋って|話して|しゃべって|はなして", message.content)) and bool(re.search(blob.DATA.settings["mynames"], message.content)):
            setMode(2)
            blob.receive("!command setMode {}".format(2), username)
            return
        elif bool(re.search("advice mode|アドバイスモード|アドバイスして", message.content)) and bool(re.search(blob.DATA.settings["mynames"], message.content)):
            setMode(3)
            blob.receive("!command setMode {}".format(2), username)
            return
        elif bool(re.search("pin|じっとしてて|じっとしていて", message.content)) and bool(re.search(blob.DATA.settings["mynames"], message.content)):
            pin = True
            blob.receive("!command pin", username)
            return
        elif bool(re.search("unpin|うごいて|動いて", message.content)) and bool(re.search(blob.DATA.settings["mynames"], message.content)):
            pin = False
            blob.receive("!command unpin", username)
            return
        elif bool(re.search("ヘルプを表示|ヘルプ表示|show help", message.content)) and bool(re.search(blob.DATA.settings["mynames"], message.content)):
            await channel.send(helpMessage)
            return
        print("受信: {}, from {}".format(re.sub(r'@(everyone|here|[!&]?[0-9]{17,21})', '@\u200b\\1', message.content), username))
        if len(persons) == 2 or isinstance(message.channel, discord.DMChannel):
            blob.receive(re.sub(r'@(everyone|here|[!&]?[0-9]{17,21})', '@\u200b\\1', message.content), username, force=True)
        else:
            blob.receive(re.sub(r'@(everyone|here|[!&]?[0-9]{17,21})', '@\u200b\\1', message.content), username)
        a = []
        for person in persons:
            if person[1] < 6:
                a.append([person[0], person[1]+0.5])
        persons = a
        pss = []
        for ps in persons:
            pss.append(ps[0])
        if blob.DATA.settings["myname"] not in pss:
            persons.append([blob.DATA.settings["myname"], 0])
        lastMessage = [message.content, message.author.name]
        lastUsername = username
        prevTime = time.time()
        messages.append([message.content, message.author.name])

i = 0
add = True
@tasks.loop(seconds=1)
async def cron():
    global persons, prevTime, lastMessage, i, messages, add, mode
    try:
        if mode == 1:
            if len(messages) != 0:
                i = 0
                if blob.DATA.myVoice != None:
                    if bool(re.search(blob.DATA.settings["mynames"], messages[-1][0])):
                        result = blob.speakFreely()
                        if result == None:
                            pass
                        else:
                            await speak(result)
                        messages = []
        elif mode == 2 or mode == 3:
            if len(messages) != 0 and lastMessage != None:
                i = 0
                pss = []
                for ps in persons:
                    pss.append(ps[0])
                aaa = ""
                for person in pss:
                    if person[0] == blob.DATA.settings["myname"]:
                        pass
                    else:
                        aaa = aaa + person[0] + "|"
                aaa = aaa[0:-1]
                if bool(re.search(blob.DATA.settings["mynames"], lastMessage[0])) or (not bool(re.search(aaa, lastMessage[0])) and random.randint(0, len(persons)-1) == 0 and blob.DATA.myVoice != None):
                    result = blob.speakFreely()
                    if result == None:
                        pass
                    else:
                        await speak(result)
                    messages = []
        elif len(messages) != 0:
            i = 0
        nowTime = time.time()
        if nowTime >= prevTime + 20:
            print("沈黙を検知")
            if i >= 1:
                i = -1
            elif i == -1:
                pass
            else:
                i += 1
            add = True
            if i == -1:
                add = False
            dt_now = datetime.datetime.now()
            blob.receive(dt_now.strftime('%Y/%m/%d %H:%M:%S'), "!systemClock")
            a = []
            for person in persons:
                if person[1] < 6:
                    a.append([person[0], person[1]+1])
            persons = a
            pss = []
            for ps in persons:
                pss.append(ps[0])
            if blob.DATA.settings["myname"] not in pss:
                persons.append([blob.DATA.settings["myname"], 0])
            if mode == 2:
                blob.receive("!command ignore", lastUsername)
                if blob.DATA.myVoice != None and random.randint(0, len(persons)) == 0:
                    if blob.DATA.myVoice != None:
                        result = blob.speakFreely()
                        if result == None:
                            messages = []
                        else:
                            await speak(result)
                            messages = []
            if mode <= 1:
                blob.receive("!command ignore", lastUsername)
            prevTime = time.time()
        else:
            pass
    except:
        import traceback
        traceback.print_exc()

"""
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

into = "こんにちは"


def listen():
    global messages, persons, prevTime, lastMessage, i
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


                pss = []
                for ps in persons:
                    pss.append(ps[0])
                if "あなた" not in pss:
                    persons.append(["あなた", 0])



                if bool(re.search("セーブして", into)) and bool(re.search(blob.DATA.settings["mynames"], into)):
                    blob.receive("!command saveMyData", "あなた")
                    print("セーブします")
                    blob.MEMORY.save()
                    print("完了")
                
                else:


                    i = 0
                    lastMessage = [into, "あなた"]
                    prevTime = time.time()
                    blob.receive(into, "あなた")
                    lastUsername = "あなた"
                    messages.append([into, "あなた"])




        # 以下は認識できなかったときに止まらないように。
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))



import threading
cronThread = threading.Thread(target=listen, daemon=True)
cronThread.start()
"""

client.run(TOKEN)