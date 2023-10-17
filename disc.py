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

people = [[blob.DATA.settings["myname"], 0]]
channel = None
lastMessage = None
lastUsername = "誰か"
messages = []
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
チャットのメッセージからも学習しますが、コマンドでの学習のほうが便利です。
```
ぬんへっへ！===下品だよ！
```
[YOU]という文字列は実際に発言する際ユーザー名に置き換えられます。

=強化学習=
「×」「❌」とメッセージを送ると、「このメッセージは悪い」と教えることができます。

=配慮コマンドについて=
botに「通常モード」というと「通常モード」になり、メッセージにbotの名前が含まれてなくても人数に応じて頻度を変えて返信します。また、沈黙が続いたときにメッセージを送信します。
botに「寡黙モード」というと「寡黙モード」になり、沈黙が続いたときにメッセージを送信しなくなります。
botに「沈黙モード」というと「沈黙モード」になり、呼ばれたときにしかメッセージを送信しなくなります。
botに「ピン」というと、チャンネルを動かなくなります。
botに「アンピン」というと、チャンネルを動けるようになります。
これらのコマンドのタイミングも学習します。"""

# 自分のBotのアクセストークンに置き換えてください
TOKEN = blob.DATA.settings["discToken"]
# 接続に必要なオブジェクトを生成
intents = discord.Intents.all()
client = discord.Client(intents=intents)
if len(blob.DATA.data["sentence"]) >= 1000:
    mode = blob.DATA.settings["defaultMode"]
else:
    mode = 1

print("mode: {}".format(mode))
print("sentences: {}".format(len(blob.DATA.data["sentence"])))

def setMode(x):
    global mode, channel
    mode = x
    print("mode: {}".format(mode))

kaisu = 0
async def speak(result):
    global channel, people, mode, pin, lastMessage, messages, kaisu
    try:
        print("{}: {}".format(blob.DATA.settings["myname"], result))
        #result = re.sub(r'@(everyone|here|[!&]?[0-9]{17,21})', '@\u200b\\1', result)
        pattern = re.compile(r"^[!/]command")
        print("users: {}".format(people))
        results = result.split("\n")

        Message = ""
        for result in results:
            if bool(pattern.search(result)):
                com = result.split(" ")
                if com[1] == "discMove":
                    if not pin:
                        if client.get_channel(int(com[2])) != None:
                            try:
                                channel = client.get_channel(int(com[2]))
                            except:
                                print("チャンネルが存在しません")
                                blob.receive("チャンネルが存在しません", "!system", add=add)
                                messages.append(["チャンネルが存在しません", "!system"])
                                try:
                                    print("チャンネルを移動しました: {}".format(channel.name))
                                    blob.receive("チャンネルを移動しました: {}".format(channel.name), "!system", add=add)
                                    people = [[blob.DATA.settings["myname"], 0]]
                                    messages.append(["チャンネルを移動しました: {}".format(channel.name), "!system"])
                                except:
                                    print("チャンネルを移動しました: DM")
                                    blob.receive("チャンネルを移動しました: DM", "!system", add=add)
                                    people = [[blob.DATA.settings["myname"], 0]]
                                    messages.append(["チャンネルを移動しました: DM", "!system"])
                    else:
                        print("エラー: あなたは固定されています。")
                        blob.receive("エラー: あなたは固定されています。", "!system", add=add)
                        messages.append(["エラー: あなたは固定されています。", "!system"])
                elif com[1] == "ignore":
                    pass
                elif com[1] == "setMode":
                    setMode(int(com[2]))
                elif com[1] == "saveMyData":
                    blob.MEMORY.saveData()
                elif com[1] == "pin":
                    pin = True
                elif com[1] == "unpin":
                    pin = False
                elif com[1] == "saveMyData":
                    blob.MEMORY.saveData()
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
                
    except:
        blob.receive("エラー: チャンネルがNoneか、このチャンネルに入る権限がありません", "!system", add=add)
        messages.append(["エラー: チャンネルがNoneか、このチャンネルに入る権限がありません", "!system"])
        print("エラー: チャンネルがNoneか、このチャンネルに入る権限がありません")

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    global lastMessage, messages
    print('ログインしました')
    cron.start()
    blob.receive("通知: 貴方は目を覚ましました。", "!system", add=add)
    lastMessage = ["通知: 貴方は目を覚ましました。", "!system"]
    messages.append(["通知: 貴方は目を覚ましました。", "!system"])

ii = 0
i = 0
add = True
# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    global pin, channel, people, lastMessage, messages, helpMessage, lastUsername, ii, mode, i, add

    if message.channel == channel or bool(re.search(blob.DATA.settings["mynames"], message.content)) or isinstance(message.channel, discord.DMChannel):
        username = message.author.name.split("#")[0]
        if message.channel != channel:
            try:
                print("チャンネルを移動しました: {}".format(message.channel.name))
                blob.MEMORY.learnSentence("!command discMove {} | チャンネル名: {}, カテゴリー: {}, トピック: {}".format(message.channel.id, message.channel.name, message.channel.category, message.channel.topic).replace("\n", " "), username)
            except:
                print("チャンネルを移動しました: {}のDM".format(username))
                blob.MEMORY.learnSentence("!command discMove {} | 誰のDMか: {}".format(message.channel.id, username).replace("\n", " "), username)
            channel = message.channel
            people = [[blob.DATA.settings["myname"], 0]]
        if message.author == client.user:
            return
        pss = []
        for ps in people:
            pss.append(ps[0])
        if username not in pss:
            people.append([username, 0])
        if message.content == "" and message.attachments == []:
            return
        if message.content == None:
            return        
        additional = ""
        for attachment in message.attachments:
            additional += "\n" + attachment.url
            print(attachment.url)
        message.content += additional

        ff = False
        parts = message.content.split("\n")
        for part in parts:
            if bool(re.search("(.*?)===(.*?)", part)):
                blob.MEMORY.learnSentence(part.split("===")[0], "!input")
                blob.MEMORY.learnSentence(part.split("===")[1], "!output")
                ff = True
        xx = message.content.split("\n")
        for x in xx:
            if bool(re.search("(.+): (.+)", x)):
                blob.MEMORY.learnSentence(x.split(": ")[1], x.split(": ")[0])
                ff = True
        if ff:
            return

        if bool(re.search("沈黙モード|黙|だま", message.content)) and bool(re.search(blob.DATA.settings["mynames"], message.content)):
            setMode(0)
            return
        if bool(re.search("寡黙モード|静かに|しずかに", message.content)) and bool(re.search(blob.DATA.settings["mynames"], message.content)):
            setMode(1)
            return
        if bool(re.search("通常モード|喋って|話して|しゃべって|はなして", message.content)) and bool(re.search(blob.DATA.settings["mynames"], message.content)):
            setMode(2)
            return
        if bool(re.search("ピン|じっとしてて", message.content)) and bool(re.search(blob.DATA.settings["mynames"], message.content)):
            pin = True
            return
        if bool(re.search("アンピン|動いていい", message.content)) and bool(re.search(blob.DATA.settings["mynames"], message.content)):
            pin = False
            return
        if bool(re.search("セーブして", message.content)) and bool(re.search(blob.DATA.settings["mynames"], message.content)):
            blob.receive("!command saveMyData", username)
            print("セーブします")
            blob.MEMORY.save()
            print("完了")
            return
        
        print("受信: {}, from {}".format(re.sub(r'@(everyone|here|[!&]?[0-9]{17,21})', '@\u200b\\1', message.content), username))
        if len(people) <= 2 or isinstance(message.channel, discord.DMChannel):
            blob.receive(re.sub(r'@(everyone|here|[!&]?[0-9]{17,21})', '', message.content), username, force=True)
        else:
            blob.receive(re.sub(r'@(everyone|here|[!&]?[0-9]{17,21})', '', message.content), username)
        a = []
        for person in people:
            if person[1] < 6:
                a.append([person[0], person[1]+0.5])
        people = a
        pss = []
        for ps in people:
            pss.append(ps[0])
        if blob.DATA.settings["myname"] not in pss:
            people.append([blob.DATA.settings["myname"], 0])
        lastMessage = [message.content, message.author.name]
        lastUsername = username
        i = 0
        add = True
        messages.append([message.content, message.author.name])

@tasks.loop(seconds=1)
async def cron():
    global people, lastMessage, messages, mode, channel, i, add
    try:
        dt_now = datetime.datetime.now()
        pattern = re.compile(r":00$")
        if bool(pattern.search(dt_now.strftime('%Y/%m/%d %H:%M:%S'))):
            blob.receive(dt_now.strftime('%Y/%m/%d %H:%M:%S'), "!systemClock", add=add)
        if mode == 1:
            if len(messages) != 0:
                if blob.DATA.myVoice != None:
                    if bool(re.search(blob.DATA.settings["mynames"], lastMessage[0])):
                        result = blob.speakFreely(add=add)
                        if result == None:
                            pass
                        else:
                            await speak(result)
                    messages = []
            else:
                if i > -2:
                    i -= 1
                add = True
                if i <= -2:
                    add = False
                blob.nextNode(add=add, force=True)
        elif mode == 2:
            if len(messages) != 0 and lastMessage != None:
                pss = []
                for ps in people:
                    pss.append(ps[0])
                aaa = ""
                for person in pss:
                    if person[0] == blob.DATA.settings["myname"]:
                        pass
                    else:
                        aaa = aaa + person[0] + "|"
                aaa = aaa[0:-1]
                
                denominator = 0
                if len(people) - 2 < 0:
                    denominator = 0
                else:
                    denominator = len(people) - 2
                if bool(re.search(blob.DATA.settings["mynames"], lastMessage[0])) or (not bool(re.search(aaa, lastMessage[0])) and random.randint(0, denominator) == 0 and blob.DATA.myVoice != None):
                    result = blob.speakFreely(add=add)
                    if result == None:
                        pass
                    else:
                        await speak(result)
                messages = []
            else:
                if i > -2:
                    i -= 1
                add = True
                if i <= -2:
                    add = False
                denominator = 0
                if len(people) - 2 < 0:
                    denominator = 0
                else:
                    denominator = len(people) - 2
                if random.randint(0, denominator+3) == 0 and blob.DATA.myVoice != None:
                    a = blob.nextNode(add=add, force=True)
                    if a:
                        result = blob.speakFreely(add=add)
                        await speak(result)
    except:
        import traceback
        traceback.print_exc()


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


                pss = []
                for ps in people:
                    pss.append(ps[0])
                if "あなた" not in pss:
                    people.append(["あなた", 0])



                if bool(re.search("セーブして", into)) and bool(re.search(blob.DATA.settings["mynames"], into)):
                    blob.receive("!command saveMyData", "あなた")
                    print("セーブします")
                    blob.MEMORY.saveData()
                    print("完了")
                
                else:


                    lastMessage = [into, "あなた"]
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


client.run(TOKEN)