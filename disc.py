import sanae
import time
import random
import re
import sys
if sys.argv[1]:
    sanae.initialize(sys.argv[1], "discord")
else:
    print("人格フォルダを指定してください。")
    exit()

persons = [[sanae.DATA.settings["myname"], 0]]
channel = None
lastMessage = None
lastUsername = None
messages = []
prevTime = time.time()
pin = False


from discord.ext import tasks
import discord
import threading
import asyncio
import Levenshtein

import datetime


helpMessage = f"""==sanaeAIヘルプ==
このbotはユーザーのメッセージに自分の意思で返信するAIです。
話している人数に応じて返信頻度を下げます。
botの名前を呼ぶとそのチャンネルに来てくれます。
メンションでは呼べません。

=学習方法=
チャットのメッセージからも学習しますが、コマンドでの学習のほうが効力が強いです。
```
哲学ユートピア: {sanae.DATA.settings["mynames"].split("|")[0]}、おいで
{sanae.DATA.settings["mynames"].split("|")[0]}: どうしましたか？
哲学ユートピア: ただよんだだけ
{sanae.DATA.settings["mynames"].split("|")[0]}: そうなのかい
```

=強化学習=
「×」「❌」とメッセージを送ると、「このメッセージは悪い」と教えることができます。

=配慮コマンドについて=
botに「静かにして」というと「寡黙モード」になり、メッセージにbotの名前が含まれない限り返信しなくなります。
botに「話して」というと「通常モード」になり、メッセージに通常通りbotの名前が含まれてなくても人数に応じて頻度を変えて返信します。
botに「じっとしてて」というと、チャンネルを動かなくなります。
botに「動いて」というと、チャンネルを動けるようになります。
これらのコマンドのタイミングも、学習します。
このbotの作成者: 笑いのユートピア#8254

**また、300メッセージ学習するまで何もしゃべらず、20万メッセージ学習するまで自発的に話しません。**
"""



# 自分のBotのアクセストークンに置き換えてください
TOKEN = sanae.DATA.settings["discToken"]

# 接続に必要なオブジェクトを生成
intents = discord.Intents.all()
client = discord.Client(intents=intents)

if len(sanae.DATA.data["sentence"]) >= 200000:
    mode = 2
    yet = 2
if len(sanae.DATA.data["sentence"]) >= 300:
    mode = 1
    yet = 1
else:
    mode = 0
    yet = 0

print("mode: {}".format(mode))
print("yet: {}".format(yet))
print("sentences: {}".format(len(sanae.DATA.data["sentence"])))


def setMode(x):
    global mode, channel, restStep
    mode = x
    print("mode: {}".format(mode))

async def speak(result):
    global channel, persons, prevTime, mode, yet, pin
    try:
        print("{}: {}".format(sanae.DATA.settings["myname"], result))
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
                        persons = [[sanae.DATA.settings["myname"], 0]]
                    try:
                        print("チャンネルを移動しました: {}".format(channel.name))
                    except:
                        print("チャンネルを移動しました: DM")
                elif com[1] == "ignore":
                    pass
                elif com[1] == "setMode":
                    setMode(int(com[2]))
                elif com[1] == "saveMyData":
                    sanae.MEMORY.save()
                elif com[1] == "pin":
                    pin = True
                elif com[1] == "unpin":
                    pin = False
                elif com[1] == "saveMyData":
                    sanae.MEMORY.save()
            else:
                Message += result + "\n"
        
        Message = Message[:-1]

        if Message != "":
            async with channel.typing():
                if len(Message) / (mode * 3) <= 7:
                    await asyncio.sleep(len(Message) / (mode * 3))
                else:
                    await asyncio.sleep(7)
                await channel.send(Message)
                restStep = 0


        prevTime = time.time()
        print("< ", sanae.DATA.sa)



        result = sanae.speakNext()
        if result:
            await speak(result)

        
        if len(sanae.DATA.data["sentence"]) >= 200000 and yet == 1:
            mode = 2
            yet = 2
            print("自分からしゃべれるようになりました")
        elif len(sanae.DATA.data["sentence"]) >= 300 and yet == 0:
            mode = 1
            yet = 1
            print("しゃべれるようになりました")
        else:
            pass
        

    except:
        import traceback
        traceback.print_exc()
        sanae.receive("エラー: このチャンネルに入る権限がありません", "!system")





# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    
    game = discord.Game(f'ヘルプ: 「{sanae.DATA.settings["myname"]}、ヘルプを表示して」')
    await client.change_presence(status=discord.Status.online, activity=game)
    
    cron.start()


ii = 0
# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    global pin, channel, persons, prevTime, lastMessage, messages, helpMessage, restStep, prevTime, lastUsername, ii, mode
    
    try:
        if message.channel.id == 1049365514251677807:
            prevTime = time.time()
            if bool(re.search("> (.+)", message.content)):
                sanae.MEMORY.learnSentence(message.content.replace("> ", ""), message.author.name)
            else:
                sanae.MEMORY.learnSentence(message.content, sanae.DATA.settings["myname"])
            return
    except:
        pass

    if message.channel == channel or bool(re.search(sanae.DATA.settings["mynames"], message.content)) or isinstance(message.channel, discord.DMChannel):
        prevTime = time.time()
        username = message.author.name.split("#")[0]
        if message.channel != channel:
            try:
                print("チャンネルを移動しました: {}".format(message.channel.name))
                sanae.receive("!command discMove {} | チャンネル名: {}, カテゴリー: {}, トピック: {}".format(message.channel.id, message.channel.name, message.channel.category, message.channel.topic), username)
            except:
                print("チャンネルを移動しました: {}のDM".format(username))
                sanae.receive("!command discMove {} | 誰のDMか: {}".format(message.channel.id, username), username)
            channel = message.channel
            persons = [[sanae.DATA.settings["myname"], 0]]
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


        
        if bool(re.search("沈黙モード|黙っ|だま", message.content)) and bool(re.search(sanae.DATA.settings["mynames"], message.content)):
            setMode(0)
            return
        elif bool(re.search("寡黙モード|静かに|しずかに", message.content)) and bool(re.search(sanae.DATA.settings["mynames"], message.content)):
            setMode(1)
            sanae.receive("!command setMode {}".format(1), username)
            sanae.MEMORY.learnSentence("!command setMode {}".format(1), "!")
            return
        elif bool(re.search("通常モード|喋って|話して|しゃべって|はなして", message.content)) and bool(re.search(sanae.DATA.settings["mynames"], message.content)):
            setMode(2)
            sanae.receive("!command setMode {}".format(2), username)
            sanae.MEMORY.learnSentence("!command setMode {}".format(2), "!")
            return

        elif bool(re.search("じっとしてて|じっとしていて", message.content)) and bool(re.search(sanae.DATA.settings["mynames"], message.content)):
            pin = True
            sanae.receive("!command pin", username)
            sanae.MEMORY.learnSentence("!command pin", "!")
            return

        elif bool(re.search("うごいて|動いて", message.content)) and bool(re.search(sanae.DATA.settings["mynames"], message.content)):
            pin = False
            sanae.receive("!command unpin", username)
            sanae.MEMORY.learnSentence("!command unpin", "!")
            return

        elif bool(re.search("、(ヘルプを表示|ヘルプ表示)して", message.content)) and bool(re.search(sanae.DATA.settings["mynames"], message.content)):
            await channel.send(helpMessage)
            return
        

        ff = False
        xx = re.split('\n', message.content)
        for x in xx:
            if bool(re.search("(.+): (.+)", x)):
                sanae.MEMORY.learnSentence(x.split(": ")[1], x.split(": ")[0])
                ff = True
        if ff:
            return

        
        print("受信: {}, from {}".format(re.sub(r'@(everyone|here|[!&]?[0-9]{17,21})', '@\u200b\\1', message.content), username))
        if len(persons) == 2 or isinstance(message.channel, discord.DMChannel):
            sanae.receive(re.sub(r'@(everyone|here|[!&]?[0-9]{17,21})', '@\u200b\\1', message.content), username, force=True)
        else:
            sanae.receive(re.sub(r'@(everyone|here|[!&]?[0-9]{17,21})', '@\u200b\\1', message.content), username)

        a = []
        for person in persons:
            if person[1] < 6:
                a.append([person[0], person[1]+0.5])
        persons = a
        pss = []
        for ps in persons:
            pss.append(ps[0])
        if sanae.DATA.settings["myname"] not in pss:
            persons.append([sanae.DATA.settings["myname"], 0])



        lastMessage = [message.content, message.author.name]
        lastUsername = username
        prevTime = time.time()
        messages.append([message.content, message.author.name])



i = 0
@tasks.loop(seconds=1)
async def cron():
    global persons, prevTime, lastMessage, i, messages, add
    try:
        if mode == 1:
            if len(messages) != 0:
                i = 0
                if sanae.DATA.myVoice != None:
                    if bool(re.search(sanae.DATA.settings["mynames"], messages[-1][0])):
                        result = sanae.speakFreely()
                        if result == None:
                            messages = []
                        else:
                            await speak(result)
                            messages = []

        elif mode == 2:
            if len(messages) != 0 and lastMessage != None:
                i = 0
                pss = []
                for ps in persons:
                    pss.append(ps[0])
                aaa = ""
                for person in pss:
                    if person[0] == sanae.DATA.settings["myname"]:
                        pass
                    else:
                        aaa = aaa + person[0] + "|"
                aaa = aaa[0:-1]
                if bool(re.search(sanae.DATA.settings["mynames"], lastMessage[0])) or (not bool(re.search(aaa, lastMessage[0])) and (random.random() < 0.4 or len(persons) <= 2) and sanae.DATA.myVoice != None):

                    result = sanae.speakFreely()
                    if result == None:
                        messages = []
                    else:
                        await speak(result)
                        messages = []
                
            

        nowTime = time.time()
        #print(nowTime >= prevTime + 15)
        #print(prevTime + 20 - nowTime)
        if nowTime >= prevTime + 20:
            print("沈黙を検知")

            if i >= 2:
                i = -1
            elif i == -1:
                pass
            else:
                i += 1

            add = True
            if i == -1:
                add = False

            dt_now = datetime.datetime.now()
            sanae.receive(dt_now.strftime('%Y/%m/%d %H:%M:%S'), "!systemClock", add=add)

            a = []
            for person in persons:
                if person[1] < 6:
                    a.append([person[0], person[1]+1])
            persons = a
            pss = []
            for ps in persons:
                pss.append(ps[0])
            if sanae.DATA.settings["myname"] not in pss:
                persons.append([sanae.DATA.settings["myname"], 0])

            if channel != None and lastMessage != []:
                if mode == 2:
                    sanae.receive("!command ignore", lastUsername, add=add)
                    if (sanae.DATA.myVoice != None and random.random() < 0.35):
                        result = sanae.speakFreely()
                        if result == None:
                            messages = []
                        else:
                            await speak(result)
                            messages = []
                if mode <= 1:
                    sanae.receive("!command ignore", lastUsername, add=add)
            prevTime = time.time()

    except:
        import traceback
        traceback.print_exc()



client.run(TOKEN)

