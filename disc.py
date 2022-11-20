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
messages = []
prevTime = time.time()


from discord.ext import tasks
import discord
import threading
import asyncio


helpMessage = f"""==sanaeAIヘルプ==
このbotはユーザーのメッセージに自分の意思で返信するAIです。
話している人数に応じて返信頻度を下げます。
botの名前を呼ぶとそのチャンネルに来てくれます。
メンションでは呼べません。
=学習について=
このbotはほかのユーザーのメッセージから学習しています。
手動では、この方法で学習します。
```
wadaAkiko: こんにちは
{sanae.DATA.settings["myname"]}: あらこんにちは、wadaAkiko
```
現在のチャンネルに移動させることを覚えさせるには、botを呼んでから
```
{sanae.DATA.settings["myname"]}: !command discMove !this-channel-id
{sanae.DATA.settings["myname"]}: !command discMove !tci
```
沈黙することは
```
{sanae.DATA.settings["myname"]}: !command ignore
```
沈黙に対する反応は
```
wadaAkiko: !command ignore
{sanae.DATA.settings["myname"]}: 沈黙するなしwadaAkiko
```
です。
=配慮コマンドについて=
botに「静かにして」というと「寡黙モード」になり、メッセージにbotの名前が含まれない限り返信しなくなります。
botに「話して」というと「通常モード」になり、メッセージに通常通りbotの名前が含まれてなくても人数に応じて頻度を変えて返信します。
このbotの作成者: 笑いのユートピア#8254
"""



# 自分のBotのアクセストークンに置き換えてください
TOKEN = sanae.DATA.settings["discToken"]

# 接続に必要なオブジェクトを生成
intents = discord.Intents.all()
client = discord.Client(intents=intents)

mode = 2

def setMode(x):
    global mode, channel, restStep
    mode = x
    print("mode: {}".format(mode))

async def speak(result):
    global channel, persons, prevTime
    print("{}: {}".format(sanae.DATA.settings["myname"], result))
    #result = re.sub(r'@(everyone|here|[!&]?[0-9]{17,21})', '@\u200b\\1', result)
    pattern = re.compile(r"^[!/]command")
    print("users: {}".format(persons))
    results = result.split("\n")

    Message = ""
    for result in results:
        if bool(pattern.search(result)):
            com = result.split(" ")
            if com[1] == "discMove":
                if client.get_channel(int(com[2])) != None:
                    channel = client.get_channel(int(com[2]))
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
        print("{}: {}".format(sanae.DATA.settings["myname"], result))
        #result = re.sub(r'@(everyone|here|[!&]?[0-9]{17,21})', '@\u200b\\1', result)
        pattern = re.compile(r"^[!/]command")
        print("users: {}".format(persons))
        results = result.split("\n")

        Message = ""
        for result in results:
            if bool(pattern.search(result)):
                com = result.split(" ")
                if com[1] == "discMove":
                    if client.get_channel(int(com[2])) != None:
                        channel = client.get_channel(int(com[2]))
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







# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    
    game = discord.Game(f'ヘルプ: 「{sanae.DATA.settings["myname"]}、ヘルプを表示して」')
    await client.change_presence(status=discord.Status.online, activity=game)
    
    cron.start()

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    global channel, persons, prevTime, lastMessage, messages, helpMessage, restStep, prevTime
    
    if message.channel == channel or bool(re.search(sanae.DATA.settings["mynames"], message.content)) or isinstance(message.channel, discord.DMChannel):
        nowTime = time.time()
        if message.channel != channel:
            try:
                print("チャンネルを移動しました: {}".format(message.channel.name))
            except:
                print("チャンネルを移動しました: {}のDM".format(message.author.name))
            channel = message.channel
            persons = [[sanae.DATA.settings["myname"], 0]]
            sanae.receive("!command discMove {} | チャンネル名: {}, カテゴリー: {}, トピック: {}".format(message.channel.id, message.channel.name, message.channel.category, message.channel.topic), message.author.name)
        if message.author == client.user:
            return
        pss = []
        for ps in persons:
            pss.append(ps[0])
        if message.author.name not in pss:
            persons.append([message.author.name, 0])
        if message.content == "":
            return
        if message.content == None:
            return

        
        if bool(re.search("沈黙モード|黙|だま", message.content)) and bool(re.search(sanae.DATA.settings["mynames"], message.content)):
            setMode(0)
        if bool(re.search("寡黙モード|静かに|しずかに", message.content)) and bool(re.search(sanae.DATA.settings["mynames"], message.content)):
            setMode(1)
            sanae.receive("!command setMode {}".format(1), message.author.name)
        if bool(re.search("通常モード|喋って|話して|しゃべって|はなして", message.content)) and bool(re.search(sanae.DATA.settings["mynames"], message.content)):
            setMode(2)
            sanae.receive("!command setMode {}".format(2), message.author.name)
        if bool(re.search("セーブして", message.content)) and bool(re.search(sanae.DATA.settings["mynames"], message.content)):
            sanae.receive("!command saveMyData", message.author.name)
            sanae.MEMORY.save()

        if bool(re.search("、(ヘルプを表示|ヘルプ表示)して", message.content)) and bool(re.search(sanae.DATA.settings["mynames"], message.content)):
            await channel.send(helpMessage)
            return
        

        ff = False
        xx = re.split('\n', message.content)
        for x in xx:
            if bool(re.search("(.+): (.+)", x)):
                ff = True
                sanae.MEMORY.addSentence(x.split(": ")[1].replace("!this-channel-id", "{}".format(message.channel.id)).replace("!tci", "{}".format(message.channel.id)), x.split(": ")[0])
            if bool(re.search("(.+); (.+)", x)):
                ff = True
                sanae.MEMORY.addSentence(x.split("; ")[1].replace("!this-channel-id", "{}".format(message.channel.id)).replace("!tci", "{}".format(message.channel.id)), "l:"+x.split("; ")[0])
        if ff:
            return

            

        if nowTime >= prevTime + 15 and lastMessage != None:
            print("沈黙を検知")
            sanae.receive("!command ignore", lastMessage.author.name)
        
        print("受信: {}, from {}".format(re.sub(r'@(everyone|here|[!&]?[0-9]{17,21})', '@\u200b\\1', message.content), message.author.name))
        if len(persons) == 2 or isinstance(message.channel, discord.DMChannel):
            sanae.receive(re.sub(r'@(everyone|here|[!&]?[0-9]{17,21})', '@\u200b\\1', message.content), message.author.name, force=True)
        else:
            sanae.receive(re.sub(r'@(everyone|here|[!&]?[0-9]{17,21})', '@\u200b\\1', message.content), message.author.name)


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



        aaa = ""
        pss = []
        for ps in persons:
            pss.append(ps[0])
        for person in pss:
            if person[0] == sanae.DATA.settings["myname"]:
                pass
            else:
                aaa = aaa + person[0] + "|"
        aaa = aaa[0:-1]
        
        lastMessage = message
        prevTime = time.time()
        messages.append(message)



i = 0
@tasks.loop(seconds=1)
async def cron():
    global persons, prevTime, lastMessage, i, messages, restStep
    try:
        if mode == 1:
            if len(messages) != 0:
                if sanae.DATA.myVoice != None:
                    if bool(re.search(sanae.DATA.settings["mynames"], messages[-1].content)) or "!command" in sanae.DATA.myVoice:
                        result = sanae.speakFreely()
                        if result == None:
                            messages = []
                        else:
                            await speak(result)
                            messages = []

        elif mode == 2:
            if len(messages) != 0:

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
                if (bool(re.search(sanae.DATA.settings["mynames"], lastMessage.content)) or (bool(re.search(aaa, lastMessage.content)) and (random.randint(0, 10) <= 3 or len(persons) <= 2) and len(sanae.DATA.data["sentence"]) >= 3500)) and sanae.DATA.myVoice != None:

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

            """
            if i >= 3:
                persons = [[sanae.DATA.settings["myname"], 0]]
                i = 0
            """

            if channel != None and lastMessage != None:
                if mode == 2:
                    sanae.receive("!command ignore", lastMessage.author.name)
                if (bool(re.search(sanae.DATA.settings["mynames"], lastMessage.content)) or ((random.randint(0, 10) <= 3 or len(persons) <= 2) and len(sanae.DATA.data["sentence"]) >= 3500)) and sanae.DATA.myVoice != None:
                        result = sanae.speakFreely()
                        if result == None:
                            messages = []
                        else:
                            await speak(result)
                            messages = []
                if mode == 1:
                    sanae.receive("!command ignore", lastMessage.author.name)
                    if sanae.DATA.myVoice != None:
                        if "!command" in sanae.DATA.myVoice:
                            
                            result = sanae.speakFreely()
                            if result == None:
                                messages = []
                            else:
                                await speak(result)
                                messages = []


                
            i += 1
            prevTime = time.time()

    except:
        import traceback
        traceback.print_exc()

"""
import assi

listen = threading.Thread(target=assi.listen)
listen.start()
"""
client.run(TOKEN)
