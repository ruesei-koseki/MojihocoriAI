import random
import re
import json
import random
import time

import CONSIDERATION
import HCONSIDERATION
import DATA
import MEMORY
import INTELLIGENCE
import FUNCTION


DATA.data = None #別途読み込むデータ
DATA.settings = None #設定
DATA.direc = None #辞書のディレクトリ
DATA.heart = None #今の気持ち(ログの座標で表される)
DATA.lastSentence = "" #最後のbotの言葉
DATA.lastSentenceHeart = "" #最後のbotのベース発言
DATA.lastSentenceInput = "" #最後に聞いた言葉
DATA.heartLastSpeaker = None #過去に似た話をしてたユーザー
DATA.maeheart = 0 #一つ前の気持ち
DATA.interface = 0 #クライアントの種類
DATA.lastUser = "あんた" #最後に話したユーザー
DATA.lastUserReplied = "あんた" #最後に返信したユーザー
DATA.postSpoken = False #自分が喋った直後
DATA.myVoice = None #心の中の声
DATA.rate = 0
DATA.times = 0
DATA.sa = 0

DATA.HheartLastSpeaker = None
DATA.Hheart = None
DATA.Hrate = 0
DATA.Hsa = 0
DATA.Htimes = 0
DATA.userLog = [None] * 10
DATA.mode = 0





def initialize(directory, interface_):
    #初期化
    DATA.direc = directory
    DATA.interface = interface_

    try:
        with open(DATA.direc+"/data.json", "r", encoding="utf8") as f:
            DATA.data = json.load(f)
        with open(DATA.direc+"/settings.json", "r", encoding="utf8") as f:
            DATA.settings = json.load(f)
    except:
        with open(DATA.direc+"/data_backup.json", "r", encoding="utf8") as f:
            DATA.data = json.load(f)
        with open(DATA.direc+"/settings.json", "r", encoding="utf8") as f:
            DATA.settings = json.load(f)
        with open(DATA.direc+"/data.json", "w", encoding="utf8") as f:
            json.dump(DATA.data, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
    DATA.heart = len(DATA.data["sentence"]) - 1
    DATA.Hheart = len(DATA.data["sentenceHumanity"]) - 1

    with open(DATA.direc+"/data_backup.json", "w", encoding="utf8") as f:
        json.dump(DATA.data, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))


def speakFreely(add=True):
    #自由に話す
    
    result = DATA.myVoice

    DATA.postSpoken = True
    if "!" not in DATA.lastUser:
        DATA.lastUserReplied = DATA.lastUser

    DATA.userLog.append("!")
    DATA.userLog.pop(0)

    
    if result != None:
        
        """
        if DATA.rate < 0.4 or len(DATA.data["sentence"]) < 300:
            results = result.split("\n")
            result = ""
            i = 0
            for rslt in results:
                if len(results) - 1 == i:
                    result += rslt + " 😅"
                else:
                    result += rslt + "\n"
                i += 1
        """

        MEMORY.addSentence(result, "!")



    if len(DATA.data["sentence"]) >= 120000:
        i = 0
        while len(DATA.data["sentence"]) >= 120000:
            del DATA.data["sentence"][0]
            DATA.heart -= 1
            DATA.maeheart -= 1
            i += 1
        DATA.heart -= 1
        DATA.maeheart -= 1




    return result








def speakNext(add=True):
    #自由に話す
    
    if DATA.mode == 0:
        if INTELLIGENCE.isNextOk():
            result = DATA.data["sentence"][DATA.heart+1][0]
            DATA.heart += 1

            DATA.postSpoken = True
            if "!" not in DATA.lastUser:
                DATA.lastUserReplied = DATA.lastUser
            DATA.lastSentenceHeart = result


            DATA.userLog.append("!")
            DATA.userLog.pop(0)


            if result != None:
       






                result = result.replace("[YOU]", DATA.lastUser)
                result = result.replace("[I]", DATA.settings["mynames"].split("|")[0])

                MEMORY.addSentence(result, "!")



            return result



    elif DATA.mode == 1:
        if INTELLIGENCE.hIsNextOk():
            result = DATA.data["sentenceHumanity"][DATA.Hheart+1][0]
            DATA.Hheart += 1

            DATA.postSpoken = True
            if "!" not in DATA.lastUser:
                DATA.lastUserReplied = DATA.lastUser
            DATA.lastSentenceHeart = result


            DATA.userLog.append("!")
            DATA.userLog.pop(0)


            if result != None:
                







                result = result.replace("[YOU]", DATA.lastUser)
                result = result.replace("[I]", DATA.settings["mynames"].split("|")[0])

                MEMORY.addSentence(result, "!")



            return result

    else:
        return False




def receive(x, u, add=True, force=False):
    try:
        if x == None or u == None: return
        
        DATA.lastSentenceInput = x
        DATA.lastUser = u

        DATA.userLog.append(u)
        DATA.userLog.pop(0)

        MEMORY.addSentence(x, u)


        if x == "×" or x == "❌":
            DATA.data["sentence"].insert(DATA.heart+1, ["×", "!"])


        result1 = CONSIDERATION.looking(x, u, force=force)
        result2 = HCONSIDERATION.looking(x, u, force=force)
        if DATA.Hrate > DATA.rate:
            result = result2
            print("人格データを採用")
        elif DATA.Hrate < DATA.rate:
            result = result1
            print("経験データを採用")
        else:
            if 0 == random.randint(0,1):
                result = result1
                print("経験データを採用")
            else:
                result = result2
                print("人格データを採用")


        if result == None:
            DATA.myVoice = None

            return



        result = result.replace("[YOU]", DATA.lastUser)
        result = result.replace("[I]", DATA.settings["mynames"].split("|")[0])




        DATA.lastSentenceHeart = result



        DATA.myVoice = result
        DATA.lastSentence = result


        DATA.maeheart = DATA.heart
    

        print("座標: {}".format(DATA.heart))
        print("人格座標: {}".format(DATA.Hheart))
        print("ログ: {}".format(DATA.userLog))

    except:
        import traceback
        traceback.print_exc()
        return None


