import random
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
DATA.lastSentence = "" #最後のbotの言葉
DATA.lastSentenceHeart = "" #最後のbotのベース発言
DATA.lastSentenceInput = "" #最後に聞いた言葉
DATA.heartLastSpeaker = None #過去に似た話をしてたユーザー
DATA.maeheart = 0 #一つ前の気持ち
DATA.interface = 0 #クライアントの種類
DATA.lastUser = "あんた" #最後に話したユーザー
DATA.lastUserReplied = "あんた" #最後に返信したユーザー
DATA.myVoice = None #心の中の声
DATA.times = 0
DATA.sa = 0
DATA.userLog = [None] * 10

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

    with open(DATA.direc+"/data_backup.json", "w", encoding="utf8") as f:
        json.dump(DATA.data, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
    try:
        DATA.data["words"]
    except:
        DATA.data["words"] = []


def speakFreely(add=True):
    #自由に話す
    result = DATA.myVoice
    DATA.lastSentenceHeart = result
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
        if add:
            MEMORY.learnSentence(result, "!")

    DATA.lastSentence = result
    return result

def nextNode(add=True, force=False):
    #自由に話す
    if len(DATA.data["sentence"]) >= 2000:
        if INTELLIGENCE.isNextOk() or force:
            DATA.maeheart = DATA.heart
            if random.randint(0,2) == 0 or DATA.heart >= len(DATA.data["sentence"]) - 1:
                print("組み合わせました")
                DATA.heart = random.randint(0, len(DATA.data["sentence"]) - 1)
                result = CONSIDERATION.lookingForNext(DATA.lastSentenceHeart, DATA.heartLastSpeaker)
            else:
                result = CONSIDERATION.lookingForNext(DATA.lastSentenceHeart, DATA.heartLastSpeaker)
            DATA.heartLastSpeaker = DATA.data["sentence"][DATA.heart][1]
            DATA.lastSentenceHeart = result
            result = result.replace("[YOU]", DATA.lastUser)
            result = result.replace("[I]", DATA.settings["mynames"].split("|")[0])
            DATA.myVoice = result
            return True
        else:
            return None
    else:
        return None


def receive(x, u, add=True, force=False):
    try:
        if x == None or u == None: return
        DATA.maeheart = DATA.heart
        DATA.lastSentenceInput = x
        if "!system" not in u:
            DATA.lastUser = u
        DATA.userLog.append(u)
        DATA.userLog.pop(0)
        if add:
            MEMORY.learnSentence(x, u)
        if x == "!bad":
            DATA.data["sentence"].insert(DATA.heart+1, ["!bad", "!"])
        if x == "!good":
            DATA.data["sentence"].insert(DATA.heart+1, ["!good", "!"])
        if random.randint(0,2) == 0:
            print("組み合わせました")
            DATA.heart = random.randint(0, len(DATA.data["sentence"]) - 1)
        result = CONSIDERATION.looking(x, u, force=force)
        if result == None:
            DATA.myVoice = None
            return
        DATA.heartLastSpeaker = DATA.data["sentence"][DATA.heart][1]
        result = result.replace("[YOU]", DATA.lastUser)
        result = result.replace("[I]", DATA.settings["mynames"].split("|")[0])
        DATA.lastSentenceHeart = result
        DATA.myVoice = result
        print("座標: {}".format(DATA.heart))
        print("ログ: {}".format(DATA.userLog))
    except:
        import traceback
        traceback.print_exc()
        return None