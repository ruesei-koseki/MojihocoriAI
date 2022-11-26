
import re
import json
import random
import time

import CONSIDERATION
import DATA
import MEMORY
import INTELLIGENCE
import FUNCTION


DATA.data = None #別途読み込むデータ
DATA.settings = None #設定
DATA.direc = None #辞書のディレクトリ
DATA.heart = None #今の気持ち(ログの座標で表される)
DATA.lastSentence = None #最後のbotの言葉
DATA.lastSentenceInput = None #最後に聞いた言葉
DATA.heartLastSpeaker = None #過去に似た話をしてたユーザー
DATA.maeheart = 0 #一つ前の気持ち
DATA.interface = 0 #クライアントの種類
DATA.lastUser = "あんた" #最後に話したユーザー
DATA.lastUserReplied = "あんた" #最後に返信したユーザー
DATA.postSpoken = False #自分が喋った直後
DATA.myVoice = None #心の中の声
DATA.rate = 0
DATA.sa = 0



def initialize(direcectory, interface_):
    #初期化
    DATA.direc = direcectory
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

    with open(DATA.direc+"/data_backup.json", "w", encoding="utf8") as f:
        json.dump(DATA.data, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))

    try:
        DATA.data["RL"]
    except:
        DATA.data["RL"] = []
    try:
        DATA.data["sentence"]
    except:
        DATA.data["sentence"] = []

def speakFreely(add=True):
    #自由に話す
    
    result = DATA.myVoice

    DATA.postSpoken = True
    DATA.lastUserReplied = DATA.lastUser

    if result != None:
        
        """
        if DATA.rate < 0.4:
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
    if INTELLIGENCE.isNextOk():
        result = DATA.data["sentence"][DATA.heart+1][0]
        DATA.heart += 1

        DATA.postSpoken = True
        DATA.lastUserReplied = DATA.lastUser


        if result != None:
            
            """
            if DATA.rate < 0.4:
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









            for myname in DATA.settings["mynames"].split("|"):
                result = result.replace(myname, DATA.lastUser)

            MEMORY.addSentence(result, "!")



        return result

    else:
        return False




def receive(x, u, add=True, force=False):
    try:
        if x == None or u == None: return
        DATA.lastSentenceInput = x
        DATA.lastUser = u


        MEMORY.addSentence(x, u)


        if x == "×":
            DATA.data["sentence"].insert(DATA.heart+1, ["×", "!"])


        result = CONSIDERATION.looking(x, u, force=force)


        if result == None:
            DATA.myVoice = None

            return





        for myname in DATA.settings["mynames"].split("|"):
            result = result.replace(myname, DATA.lastUser)



        DATA.myVoice = result
        DATA.lastSentence = result


        DATA.maeheart = DATA.heart
    


        print("rate: ", DATA.rate)

    except:
        import traceback
        traceback.print_exc()
        return None


