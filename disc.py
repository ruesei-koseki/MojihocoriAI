import mojihocori
import time
import random
import re
import sys
if sys.argv[1]:
    mojihocori.initialize(sys.argv[1], "discord")
else:
    mojihocori.initialize("main", "discord")

people = [[mojihocori.DATA.settings["myname"], 0]]
channel = None
lastMessage = None
lastUsername = "誰か"
messages = []
pin = False
answerFlag = False

import datetime
dt = datetime.datetime.now()

from discord.ext import tasks
import discord
import threading
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
from rapidfuzz.distance import Levenshtein

helpMessage = f"""==mojihocoriAIヘルプ==
このbotはユーザーのメッセージに自分の意思で返信するAIです。
話している人数に応じて返信頻度を下げます。
botの名前を呼ぶとそのチャンネルに来てくれます。
メンションでは呼べません。

=学習方法=
チャットのメッセージからも学習しますが、コマンドでの学習のほうが便利です。
```
ぬんへっへ！===下品だよ！
```

=強化学習=
「!bad」とメッセージを送ると、「このメッセージは悪い」と教えることができます。
「!good」とメッセージを送ると、「このメッセージは良い」と教えることができます。

=配慮コマンドについて=
botに「通常モード」というと「通常モード」になり、メッセージにbotの名前が含まれてなくても人数に応じて頻度を変えて返信します。また、沈黙が続いたときにメッセージを送信します。
botに「寡黙モード」というと「寡黙モード」になり、沈黙が続いたときにメッセージを送信しなくなります。
botに「沈黙モード」というと「沈黙モード」になり、呼ばれたときにしかメッセージを送信しなくなります。
botに「ピン」というと、チャンネルを動かなくなります。
botに「アンピン」というと、チャンネルを動けるようになります。
これらのコマンドのタイミングも学習します。"""

# 自分のBotのアクセストークンに置き換えてください
TOKEN = mojihocori.DATA.settings["discToken"]
# 接続に必要なオブジェクトを生成
intents = discord.Intents.all()
client = discord.Client(intents=intents)

mode = mojihocori.DATA.settings["defaultMode"]

print("mode: {}".format(mode))
print("sentences: {}".format(len(mojihocori.DATA.data["sentence"])))

def setMode(x):
    global mode, channel
    mode = x
    print("mode: {}".format(mode))

kaisu = 0
async def speak(result):
    global channel, people, mode, pin, lastMessage, messages, kaisu, dt, add, i, answerFlag
    try:
        if not add:
            i = 0
            add = True
            mojihocori.MEMORY.learnSentence(result, "!")
        print("{}: {}".format(mojihocori.DATA.settings["myname"], result))
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
                                mojihocori.receive("チャンネルが存在しません", "!system", add=add)
                                messages.append(["チャンネルが存在しません", "!system"])
                                try:
                                    print("チャンネルを移動しました: {}".format(channel.name))
                                    mojihocori.receive("チャンネルを移動しました: {}".format(channel.name), "!system", add=add)
                                    people = [[mojihocori.DATA.settings["myname"], 0]]
                                    messages.append(["チャンネルを移動しました: {}".format(channel.name), "!system"])
                                except:
                                    print("チャンネルを移動しました: DM")
                                    mojihocori.receive("チャンネルを移動しました: DM", "!system", add=add)
                                    people = [[mojihocori.DATA.settings["myname"], 0]]
                                    messages.append(["チャンネルを移動しました: DM", "!system"])
                    else:
                        print("エラー: あなたは固定されています。")
                        mojihocori.receive("エラー: あなたは固定されています。", "!system", add=add)
                        messages.append(["エラー: あなたは固定されています。", "!system"])
                elif com[1] == "ignore":
                    pass
                elif com[1] == "setMode":
                    setMode(int(com[2]))
                elif com[1] == "saveMyData":
                    mojihocori.MEMORY.saveData()
                elif com[1] == "pin":
                    pin = True
                elif com[1] == "unpin":
                    pin = False
                elif com[1] == "saveMyData":
                    mojihocori.MEMORY.saveData()
                elif com[1] == "confirmClock":
                    dt = datetime.datetime.now()
                    i = 0
                    add = True
                    mojihocori.receive(dt.strftime('只今の日付と時刻は、 %Y年 %m月 %d日 %H時 %M分 %S秒 です。'), "!clock", add=add)
                    lastMessage = [dt.strftime('只今の日付と時刻は、 %Y年 %m月 %d日 %H時 %M分 %S秒 です。'), "!clock"]
                    messages.append([dt.strftime('只今の日付と時刻は、 %Y年 %m月 %d日 %H時 %M分 %S秒 です。'), "!clock"])
            else:
                Message += result + "\n"
        Message = Message[:-1]
        if Message != "":
            async with channel.typing():
                if len(Message) / (mode * 3) >= 1:
                    await asyncio.sleep(len(Message) / (mode * 3))
                else:
                    await asyncio.sleep(1)
                await channel.send(Message)
                
                result = mojihocori.nextNode(add=add)
                if result:
                    result = mojihocori.speakFreely(add=add)
                    await speak(result)
                    dt = datetime.datetime.now()
                answerFlag = False
                
    except:
        mojihocori.receive("エラー: チャンネルがNoneか、このチャンネルに入る権限がありません", "!system", add=add)
        #messages.append(["エラー: チャンネルがNoneか、このチャンネルに入る権限がありません", "!system"])
        print("エラー: チャンネルがNoneか、このチャンネルに入る権限がありません")

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    global lastMessage, messages
    print('ログインしました')
    cron.start()
    mojihocori.receive("通知: 貴方は目を覚ましました。", "!system", add=add)
    lastMessage = ["通知: 貴方は目を覚ましました。", "!system"]
    messages.append(["通知: 貴方は目を覚ましました。", "!system"])

ii = 0
i = 0
add = True
# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    global pin, channel, people, lastMessage, messages, helpMessage, lastUsername, ii, mode, i, add, dt

    if message.channel == channel or bool(re.search(mojihocori.DATA.settings["mynames"], message.content)) or isinstance(message.channel, discord.DMChannel):
        username = message.author.display_name.split("#")[0]
        if message.channel != channel:
            try:
                print("チャンネルを移動しました: {}".format(message.channel.name))
                mojihocori.MEMORY.learnSentence("!command discMove {} | チャンネル名: {}, カテゴリー: {}, トピック: {}".format(message.channel.id, message.channel.name, message.channel.category, message.channel.topic).replace("\n", " "), username)
            except:
                print("チャンネルを移動しました: {}のDM".format(username))
                mojihocori.MEMORY.learnSentence("!command discMove {} | 誰のDMか: {}".format(message.channel.id, username).replace("\n", " "), username)
            channel = message.channel
            people = [[mojihocori.DATA.settings["myname"], 0]]
        if message.author == client.user:
            return

        ff = False
        parts = message.content.split("\n")
        for part in parts:
            if bool(re.search("(.*?)===(.*?)", part)):
                if part.split("===")[0] == "":
                    mojihocori.MEMORY.learnSentence(lastMessage[0], "!input", mama=True)
                    mojihocori.MEMORY.learnSentence(part.split("===")[1], "!output", mama=True)
                else:
                    mojihocori.MEMORY.learnSentence(part.split("===")[0], "!input", mama=True)
                    mojihocori.MEMORY.learnSentence(part.split("===")[1], "!output", mama=True)
                ff = True
        if bool(re.search("(.*?)\n==>\n(.*?)", message.content)):
            mojihocori.MEMORY.learnSentence(message.content.split("\n==>\n")[0], "!input", mama=True)
            mojihocori.MEMORY.learnSentence(message.content.split("\n==>\n")[1], "!output", mama=True)
            ff = True
        if ff:
            mojihocori.MEMORY.learnSentence("!good", "!system", mama=True)
            return
        
        ff = False
        xx = message.content.split("\n")
        for x in xx:
            if bool(re.search("(.+): (.+)", x)):
                mojihocori.MEMORY.learnSentence(x.split(": ")[1], x.split(": ")[0], mama=True)
                ff = True
        if ff:
            mojihocori.MEMORY.learnSentence("!good", "!system", mama=True)
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

        if bool(re.search("沈黙モード|黙|だま", message.content)) and bool(re.search(mojihocori.DATA.settings["mynames"], message.content)):
            setMode(0)
            return
        if bool(re.search("寡黙モード|静かに|しずかに", message.content)) and bool(re.search(mojihocori.DATA.settings["mynames"], message.content)):
            setMode(1)
            return
        if bool(re.search("通常モード|喋って|話して|しゃべって|はなして", message.content)) and bool(re.search(mojihocori.DATA.settings["mynames"], message.content)):
            setMode(2)
            return
        if bool(re.search("ピン|じっとしてて", message.content)) and bool(re.search(mojihocori.DATA.settings["mynames"], message.content)):
            pin = True
            return
        if bool(re.search("アンピン|動いていい", message.content)) and bool(re.search(mojihocori.DATA.settings["mynames"], message.content)):
            pin = False
            return
        elif bool(re.search("ヘルプを表示|ヘルプ表示|show help", message.content)) and bool(re.search(mojihocori.DATA.settings["mynames"], message.content)):
            await channel.send(helpMessage)
            return
        if bool(re.search("セーブして", message.content)) and bool(re.search(mojihocori.DATA.settings["mynames"], message.content)):
            mojihocori.receive("!command saveMyData", username)
            print("セーブします")
            mojihocori.MEMORY.saveData()
            print("完了")
            return
        
        print("受信: {}, from {}".format(message.content, username))
        if len(people) <= 2 or isinstance(message.channel, discord.DMChannel):
            mojihocori.receive(message.content, username, force=True)
        else:
            mojihocori.receive(message.content, username, force=True)
        lastMessage = [message.content, username]
        lastUsername = username
        i = 0
        add = True
        messages.append([message.content, username])
        dt = datetime.datetime.now()

@tasks.loop(seconds=1)
async def cron():
    global people, lastMessage, messages, mode, channel, i, add, dt, answerFlag
    try:
        dt_now = datetime.datetime.now()
        """
        pattern = re.compile(r"(0|3)0:00$")
        if bool(pattern.search(dt_now.strftime('%Y/%m/%d %H:%M:%S'))):
            mojihocori.receive(dt_now.strftime('%Y/%m/%d %H:%M:%S'), "!systemClock")
        """

        a = []
        for person in people:
            if person[1] < 60*10:
                a.append([person[0], person[1]+1])
        people = a
        pss = []
        for ps in people:
            pss.append(ps[0])
        if mojihocori.DATA.settings["myname"] not in pss:
            people.append([mojihocori.DATA.settings["myname"], 0])

        if mode == 1:
            if len(messages) != 0:
                if mojihocori.DATA.myVoice != None:
                    if bool(re.search(mojihocori.DATA.settings["mynames"], lastMessage[0])) or isinstance(channel, discord.channel.DMChannel):
                        result = mojihocori.speakFreely(add=add)
                        if result == None:
                            pass
                        else:
                            await speak(result)
                    messages = []
            if random.randint(0, 60*25) == 0 and mojihocori.DATA.myVoice != None:
                result = mojihocori.speakFreely(add=add)
                if result == None:
                    pass
                else:
                    await speak(result)
        elif mode == 2:
            if len(messages) != 0:
                if bool(re.search(mojihocori.DATA.settings["mynames"], lastMessage[0])):
                    answerFlag = True
                pss = []
                for ps in people:
                    pss.append(ps[0])
                aaa = ""
                for person in pss:
                    if person == mojihocori.DATA.settings["myname"]:
                        pass
                    else:
                        aaa = aaa + person + "|"
                aaa = aaa[0:-1]
                
                if len(people) <= 1:
                    denominator = 0
                else:
                    denominator = (len(people) - 2)
                
                if answerFlag or bool(re.search(mojihocori.DATA.settings["mynames"], lastMessage[0])) or isinstance(channel, discord.channel.DMChannel) or ((not bool(re.search(aaa, lastMessage[0])) or aaa == "") and random.randint(0, denominator) == 0 and mojihocori.DATA.myVoice != None):
                    result = mojihocori.speakFreely(add=add)
                    if result == None:
                        pass
                    else:
                        await speak(result)
                messages = []
        if dt_now - dt >= datetime.timedelta(seconds=20):
            if i > -2:
                i -= 1
            add = True
            if i <= -2:
                add = False

            dt = datetime.datetime.now()
            mojihocori.receive("!command ignore", mojihocori.DATA.userLog[-1], add=add)
            print("沈黙を検知")
            if mode == 2 and random.randint(0, 5) == 0:
                result = mojihocori.speakFreely(add=add)
                if result == None:
                    pass
                else:
                    await speak(result)
        
    except:
        import traceback
        traceback.print_exc()


"""
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

into = "こんにちは"


def listen():
    global messages, people, lastMessage, i
    while True:
        
        print("聞き取っています...")
        
        with mic as source:
            r.adjust_for_ambient_noise(source) #雑音対策
            audio = r.listen(source)

        print ("解析中...")

        try:
            into = r.recognize_google(audio, language=mojihocori.DATA.settings["languageHear"])
            print(into)

            if Levenshtein.normalized_similarity(into, mojihocori.DATA.lastSentence) < 0.85:


                pss = []
                for ps in people:
                    pss.append(ps[0])
                if "あなた" not in pss:
                    people.append(["あなた", 0])



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
                        lastMessage = [cc, "あなた"]
                        mojihocori.receive(cc, "あなた")
                        lastUsername = "あなた"
                        messages.append([cc, "あなた"])




        # 以下は認識できなかったときに止まらないように。
        except sr.UnknownValueError:
            dt = datetime.datetime.now()
            mojihocori.receive("!command ignore", lastUsername, add=add)
            print("沈黙を検知")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


import threading
cronThread = threading.Thread(target=listen, daemon=True)
cronThread.start()
"""



client.run(TOKEN)