import json
import random
import CONSIDERATION
import DATA
import MEMORY
import INTELLIGENCE
import FUNCTION
from rapidfuzz.distance import Levenshtein

DATA.data = None #別途読み込むデータ
DATA.settings = None #設定
DATA.direc = None #辞書のディレクトリ
DATA.heart = None #今の気持ち(ログの座標で表される)
DATA.lastSentence = "" #最後のbotの言葉
DATA.lastSentenceHeart = "" #最後のbotのベース発言
DATA.lastSentenceInput = "" #最後に聞いた言葉
DATA.lastSentenceInputHeart = "" #最後に聞いた言葉
DATA.heartLastSpeaker = "" #過去に似た話をしてたユーザー
DATA.heartLastSpeakerInput = ""
DATA.maeheart = 0 #一つ前の気持ち
DATA.zenkaiHeart = 0
DATA.interface = 0 #クライアントの種類
DATA.lastUser = "あんた" #最後に話したユーザー
DATA.lastUserReplied = "あんた" #最後に返信したユーザー
DATA.myVoice = None #心の中の声
DATA.times = 0
DATA.sa = 0
DATA.skip = 0
DATA.userLog = [None] * 10
DATA.tangoOkikae1 = ""
DATA.tangoOkikae2 = ""
DATA.rate = 1.0


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
    try:
        DATA.data["tangoOkikae1"]
    except:
        DATA.data["tangoOkikae1"] = ""
    try:
        DATA.data["tangoOkikae2"]
    except:
        DATA.data["tangoOkikae2"] = ""

    DATA.tangoOkikae1 = DATA.data["tangoOkikae1"]
    DATA.tangoOkikae2 = DATA.data["tangoOkikae2"]
    
    for message in DATA.data["sentence"]:
        MEMORY.findWords(message[0])
        MEMORY.findWords(message[1])

    DATA.heart = random.randint(0, len(DATA.data["sentence"]) - 1) #今の気持ち(ログの座標で表される)

def speakFreely(add=True):
    #自由に話す
    result = DATA.myVoice
    if "!" not in DATA.lastUser:
        DATA.lastUserReplied = DATA.lastUser
    DATA.userLog.append("!")
    DATA.userLog.pop(0)
    if result != None:
        if len(DATA.tangoOkikae1) >= 1024:
            DATA.tangoOkikae1 = DATA.tangoOkikae1[-1024:]
        DATA.tangoOkikae1 += "\n" + DATA.settings["myname"]+": "+result
        
        if len(DATA.tangoOkikae2) >= 1024:
            DATA.tangoOkikae2 = DATA.tangoOkikae2[-1024:]
        if DATA.heartLastSpeaker == "!":
            DATA.tangoOkikae2 += "\n" + DATA.settings["myname"]+": "+DATA.lastSentenceHeart
        else:
            DATA.tangoOkikae2 += "\n" + DATA.heartLastSpeaker+": "+DATA.lastSentenceHeart

        if add:
            MEMORY.learnSentence(result, "!")

    DATA.lastSentence = result
    return result

def nextNode(add=True):
    #自由に話す
    if INTELLIGENCE.isNextOk():
        DATA.maeheart = DATA.heart
        DATA.heart += 1
        result = DATA.data["sentence"][DATA.heart][0]
        DATA.heartLastSpeaker = DATA.data["sentence"][DATA.heart][1]
        result = INTELLIGENCE.replaceWords(DATA.lastUser+": "+result, DATA.tangoOkikae1, DATA.tangoOkikae2)
        DATA.myVoice = result
        if add:
            MEMORY.learnSentence(result, "!")
        return True
    else:
        return None

def receive(x, u, add=True, force=False):
    try:
        if x == None or u == None: return
        if u not in DATA.data["words"]:
            DATA.data["words"].append(u)
        
        DATA.maeheart = DATA.heart
        DATA.lastSentenceInput = x
        if "!system" not in u:
            DATA.lastUser = u
        DATA.userLog.append(u)
        DATA.userLog.pop(0)
        if add:
            if x == "!bad":
                DATA.data["sentence"].insert(DATA.heart+1, ["!bad", "!"])
            if x == "!good":
                DATA.data["sentence"].insert(DATA.heart+1, ["!good", "!"])
        result = CONSIDERATION.looking(x, u, force=force)
        
        if add:
            MEMORY.learnSentence(x, u)
        else:
            MEMORY.findWords(x)
        
        if result == None:
            DATA.myVoice = None
            return
        if len(DATA.tangoOkikae1) >= 1024:
            DATA.tangoOkikae1 = DATA.tangoOkikae1[-1024:]
        DATA.tangoOkikae1 += "\n" + u+": "+x

        if len(DATA.tangoOkikae2) >= 1024:
            DATA.tangoOkikae2 = DATA.tangoOkikae2[-1024:]
        if DATA.heartLastSpeakerInput == "!":
            DATA.tangoOkikae2 += "\n" + DATA.settings["myname"]+": "+DATA.lastSentenceInputHeart
        else:
            DATA.tangoOkikae2 += "\n" + DATA.heartLastSpeakerInput+": "+DATA.lastSentenceInputHeart
        
        result = INTELLIGENCE.replaceWords(DATA.heartLastSpeaker+": "+result, DATA.tangoOkikae1, DATA.tangoOkikae2)

        DATA.myVoice = result
        print("座標: {}".format(DATA.heart))
        print("ログ: {}".format(DATA.userLog))
    except:
        import traceback
        traceback.print_exc()
        return None