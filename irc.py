import sys, socket, os, signal
import time, datetime

BUF_SIZE = 1024


class IRC(object):
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socketオブジェクトの生成(TCP)

    def connect(self, host, port):
        self.server.connect((host, port)) #接続

    def login(self, password, nickname, username, realname, hostname = "localhost", servername = "*"):
        if password is not None: #中にはパスワードがいらないサーバもある
            pass_message = "PASS " + password + "\n" #PASSメッセージ
            self.server.send(pass_message.encode('utf-8')) #送信
        nick_message = "NICK " + nickname + "\n" #NICKメッセージ
        user_message = "USER %s %s %s :%s\n" % (username, hostname, servername, realname) #USERメッセージ
        self.server.send(nick_message.encode('utf-8')) #送信
        self.server.send(user_message.encode('utf-8')) #送信
        self.nickname = nickname
        self.channel = None

    def join(self, channel):
        join_message = "JOIN " + channel + "\n" #JOINメッセージ
        self.channel = channel
        self.server.send(join_message.encode('utf-8')) #送信

    def part(self, channel):
        part_message = "PART " + channel + "\n" #JOINメッセージ
        self.server.send(part_message.encode('utf-8')) #送信

    def topic(self, channel, topic):
        topic_message = "TOPIC " + channel + " " + topic + "\n"
        self.server.send(topic_message.encode('utf-8')) #送信

    def pong(self, server1, server2 = None):
        pong_message = "PONG %s %s" % (server1, server2) #PONGメッセージ
        pong_message += "\n"
        self.server.send(pong_message.encode('utf-8')) #送信

    def privmsg(self, channel, text):
        privmsg_message = "PRIVMSG %s :%s\n" % (channel, text) #PRIVMSGメッセージ
        self.server.send(privmsg_message.encode('utf-8')) #送信

    def quit(self):
        self.server.send(b"QUIT :bye!") #QUITメッセージ送信

    def wait_message(self, func):
        prevTime = time.time()
        while True:
            if time.time() - prevTime >= 20:
                prevTime = time.time()
                topic_message = "TOPIC " + self.channel + "\n" #JOINメッセージ
                self.server.send(topic_message.encode('utf-8')) #送信


            msg_buf = self.server.recv(BUF_SIZE) #受信
            msg_buf = msg_buf.decode('utf-8', 'ignore').strip()
            print(msg_buf)
            ## ここからメッセージ処理 ##
            prefix = None
            if msg_buf[0] == ":":
                p = msg_buf.find(" ")
                prefix = msg_buf[1:p]
                msg_buf = msg_buf[(p + 1):]

            p = msg_buf.find(":")
            if p != -1: #":"から始まるパラメータがまだあった場合
                last_param = msg_buf[(p + 1):]
                msg_buf = msg_buf[:p]
                msg_buf = msg_buf.strip()

            messages = msg_buf.split()
            ## ここまで ##

            command = messages[0] #コマンド名
            params = messages[1:] #今回は無視

            if command == "PING":
                print(last_param)
                self.pong(last_param) #PINGが来たらすぐPONGを返す
            elif command == "PRIVMSG":
                text = last_param #PRIVMSGコマンドで送られてきたメッセージ

                func(prefix.split("!")[0], text.split("\n")[0], params[0], "PRIVMSG")
            elif command == "INVITE":
                if params[0] == self.nickname:
                    func(prefix.split("!")[0], last_param, "invite", "INVITE")
            elif command == "TOPIC":
                func(prefix.split("!")[0], last_param, params[0], "TOPIC")








import blob
import time
import random
import re
import sys
blob.initialize(sys.argv[1], "irc")


persons = [[blob.DATA.settings["myname"], 0]]
channel = None
lastMessage = None
lastMessage = None
messages = []
prevTime = time.time()


mode = 2

print("mode: {}".format(mode))
print("sentences: {}".format(len(blob.DATA.data["sentence"])))




import threading

irc = IRC()
irc.connect(blob.DATA.settings["irc"]["host"], blob.DATA.settings["irc"]["port"])
irc.login(None, blob.DATA.settings["myname"], blob.DATA.settings["myname"], blob.DATA.settings["myname"])
time.sleep(7)
irc.join(blob.DATA.settings["irc"]["defaultChannel"])
nowChannel = blob.DATA.settings["irc"]["defaultChannel"]




def setMode(x):
    global mode, nowChannel
    mode = x
    print("mode: {}".format(mode))









import Levenshtein
def speak(result):
    global nowChannel, persons, restStep, restStep
    if result:
        print("users: {}".format(persons))
        pattern = re.compile(r"^!command")
        if bool(pattern.search(result)):
            try:
                com = result.split(" ", 2)
                if com[1] == "discMove":
                    pass
                elif com[1] == "ircMove":
                    irc.part(nowChannel)
                    irc.join(com[2])
                    nowChannel = com[2]
                    print("チャンネルを移動しました: {}".format(com[2]))
                elif com[1] == "ircTopic":
                    irc.topic(nowChannel, com[2])
                    print("トピックを変更しました: {}".format(com[2]))
                elif com[1] == "ignore":
                    pass
                elif com[1] == "modeChange":
                    setMode(int(com[2]))
                elif com[1] == "saveMyData":
                    blob.MEMORY.save()
            except:
                pass
        else:
            time.sleep(3)
            irc.privmsg(nowChannel, result)
                
        result = blob.speakNext()
        if result:
            speak(result)
            #pass








i = 0
add = True
def cron():
    global persons, prevTime, lastMessage, i, messages, restStep, mode, restTime, add
    while True:
        try:
            if mode == 1:
                if len(messages) != 0:
                    if blob.DATA.myVoice != None:
                        if bool(re.search(blob.DATA.settings["mynames"], messages[-1][0])):
                            result = blob.speakFreely()
                            if result == None:
                                messages = []
                            else:
                                speak(result)
                                messages = []

            elif mode == 2:
                if len(messages) != 0 and lastMessage != None:

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
                            messages = []
                        else:
                            speak(result)
                            messages = []
                    
                

            nowTime = time.time()
            if nowTime >= prevTime + 5:
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
                blob.receive(dt_now.strftime('%Y/%m/%d %H:%M:%S'), "!systemClock", add=add)
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

                if channel != None and lastMessage != []:
                    if mode == 2:
                        blob.receive("!command ignore", lastUsername, add=add)
                        if bool(re.search(blob.DATA.settings["mynames"], lastMessage[0])) or (blob.DATA.myVoice != None and random.random() < 0.35):
                                result = blob.speakFreely()
                                if result == None:
                                    messages = []
                                else:
                                    speak(result)
                                    messages = []
                    if mode == 1:
                        blob.receive("!command ignore", lastUsername, add=add)
                prevTime = time.time()
        except:
            import traceback
            traceback.print_exc()
        time.sleep(1)











cronThread1 = threading.Thread(target=cron, daemon=True)
cronThread1.start()








##########################################


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
            audio = r.listen(source, phrase_time_limit=60)

        print ("解析中...")

        try:
            into = r.recognize_google(audio, language=blob.DATA.settings["languageHear"])
            print(into)

            if Levenshtein.ratio(into, blob.DATA.lastSentence) < 0.85:


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

cronThread2 = threading.Thread(target=listen, daemon=True)
cronThread2.start()






##########################################














@irc.wait_message
def onMessage(user, message, channel, a):
    global nowChannel, messages, persons, prevTime, lastMessage
    if a == "INVITE":
        persons = [[blob.DATA.settings["myname"], 0]]
        blob.receive("!command ircMove {}".format(message), user)
        irc.part(nowChannel)
        time.sleep(1)
        irc.join(message)
        nowChannel = message
        print("チャンネルを移動しました: {}".format(message))
    elif a == "TOPIC":
        blob.receive("!command ircTopic {}".format(message), user)
        messages.append(["!command ircTopic {}".format(message), user])
        print("トピックを変更されました: {}".format(message))
    elif a == "PRIVMSG":
        
        if bool(re.search("(.+)\(discord\): (.+)", message)):
            user = message.split("(discord): ", 1)[0]
            message = message.split("(discord): ", 1)[1]

        a = []
        for person in persons:
            print(persons)
            if person[1] < 6:
                a.append([person[0], person[1]+0.5])
        persons = a
        pss = []
        for ps in persons:
            pss.append(ps[0])
        if blob.DATA.settings["myname"] not in pss:
            persons.append([blob.DATA.settings["myname"], 0])
        if user not in pss:
            persons.append([user, 0])





        ff = False
        xx = re.split('\n', message)
        for x in xx:
            if bool(re.search("(.+): (.+)", x)):
                blob.MEMORY.learnSentence(x.split(": ")[1], x.split(": ")[0])
                ff = True
        if ff:
            return


        if bool(re.search("沈黙モード|黙|だま", message)) and bool(re.search(blob.DATA.settings["mynames"], message)):
            setMode(0)
            return
        if bool(re.search("寡黙モード|静かに|しずかに", message)) and bool(re.search(blob.DATA.settings["mynames"], message)):
            setMode(1)
            return
        if bool(re.search("通常モード|喋って|話して|しゃべって|はなして", message)) and bool(re.search(blob.DATA.settings["mynames"], message)):
            setMode(2)
            return
        if bool(re.search("セーブして", message)) and bool(re.search(blob.DATA.settings["mynames"], message)):
            blob.receive("!command saveMyData", user)
            print("セーブします")
            blob.MEMORY.save()
            print("完了")
            return




        lastMessage = [message, user]
        prevTime = time.time()
        print("受信: {}, from {}".format(message, user))
        blob.receive(message, user)
        messages.append([message, user])




