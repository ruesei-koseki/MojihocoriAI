
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
DATA.actualUser = ["None", "None", "None", "None", "None"] #今話してる人
DATA.brainUser = ["None", "None", "None", "None", "None"] #過去に似た話をしてたユーザー
DATA.wordMemory = ["None"]*2 #重要な単語
DATA.heart = None #今の気持ち(ログの座標で表される)
DATA.replaceWords = True #単語を置き換えるか
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

    """
    for i in range(len(DATA.data["sentence"])):
        try:
            if "😅" in DATA.data["sentence"][i][0]:
                del DATA.data["sentence"][i]
        except:
            pass
    """

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
        INTELLIGENCE.wordSyori(result)


    #名前置き換え用
    DATA.brainUser.append(DATA.data["sentence"][DATA.heart][1].replace("l:", ""))
    if len(DATA.brainUser) > 5:
        DATA.brainUser = [DATA.brainUser[-5], DATA.brainUser[-4], DATA.brainUser[-3], DATA.brainUser[-2], DATA.brainUser[-1]]

    DATA.actualUser.append("!")
    if len(DATA.actualUser) > 5:
        DATA.actualUser = [DATA.actualUser[-5], DATA.actualUser[-4], DATA.actualUser[-3], DATA.actualUser[-2], DATA.actualUser[-1]]


    print("DATA.brainUser: {}".format(DATA.brainUser))
    print("DATA.actualUser: {}".format(DATA.actualUser))


    return result








def speakNext(add=True):
    #自由に話す
    if INTELLIGENCE.isNextOk():
        result = DATA.data["sentence"][DATA.heart+1][0]

        DATA.postSpoken = True
        DATA.lastUserReplied = DATA.lastUser

        print("単語: ", DATA.wordMemory)

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



            knockout = []
            for i in reversed(range(len(DATA.actualUser))):
                if DATA.actualUser[i] != "!" and DATA.actualUser[i] != "_BRAIN_" and DATA.actualUser[i] != "None" and DATA.brainUser[i] not in knockout:
                    knockout.append(DATA.actualUser[i])
                    if DATA.brainUser[i] == "!" or DATA.brainUser[i] == DATA.settings["myname"]:
                        for myname in DATA.settings["mynames"].split("|"):
                            result = result.replace(myname, DATA.actualUser[i])
                    else:
                        result = result.replace(DATA.brainUser[i], DATA.actualUser[i])



            #重要な単語を最大5個置き換える
            try:
                if DATA.replaceWords:
                    i = len(DATA.data["sentence"][DATA.heart][2])
                    knockout = []
                    ii = 0
                    while True:
                        if ii == i:
                            break
                        if DATA.wordMemory[ii] != "None" and DATA.data["sentence"][DATA.heart][2][ii] != "None" and DATA.data["sentence"][DATA.heart][2][ii] not in knockout:
                            result = result.replace(DATA.data["sentence"][DATA.heart][2][ii], DATA.wordMemory[ii])
                            knockout.append(DATA.wordMemory[ii])
                        ii += 1
            except:
                pass

            MEMORY.addSentence(result, "!")
            INTELLIGENCE.wordSyori(result)



        print("DATA.brainUser: {}".format(DATA.brainUser))
        print("DATA.actualUser: {}".format(DATA.actualUser))


        #名前置き換え用
        DATA.brainUser.append(DATA.data["sentence"][DATA.heart][1].replace("l:", ""))
        if len(DATA.brainUser) > 5:
            DATA.brainUser = [DATA.brainUser[-5], DATA.brainUser[-4], DATA.brainUser[-3], DATA.brainUser[-2], DATA.brainUser[-1]]

        DATA.actualUser.append("!")
        if len(DATA.actualUser) > 5:
            DATA.actualUser = [DATA.actualUser[-5], DATA.actualUser[-4], DATA.actualUser[-3], DATA.actualUser[-2], DATA.actualUser[-1]]



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
            DATA.data["sentence"].insert(DATA.heart+1, ["×", "!", DATA.wordMemory])


        INTELLIGENCE.wordSyori(x)
        result = CONSIDERATION.looking(x, u, force=force)



        if result == None:
            DATA.myVoice = None
        
            #名前置き換え用
            DATA.brainUser.append(DATA.data["sentence"][DATA.heart][1].replace("l:", ""))
            if len(DATA.brainUser) > 5:
                DATA.brainUser = [DATA.brainUser[-5], DATA.brainUser[-4], DATA.brainUser[-3], DATA.brainUser[-2], DATA.brainUser[-1]]

            DATA.actualUser.append(u)
            if len(DATA.actualUser) > 5:
                DATA.actualUser = [DATA.actualUser[-5], DATA.actualUser[-4], DATA.actualUser[-3], DATA.actualUser[-2], DATA.actualUser[-1]]


            return

        else:

            #名前置き換え用
            DATA.brainUser.append(DATA.data["sentence"][DATA.heart-1][1].replace("l:", ""))
            if len(DATA.brainUser) > 5:
                DATA.brainUser = [DATA.brainUser[-5], DATA.brainUser[-4], DATA.brainUser[-3], DATA.brainUser[-2], DATA.brainUser[-1]]

            DATA.actualUser.append(u)
            if len(DATA.actualUser) > 5:
                DATA.actualUser = [DATA.actualUser[-5], DATA.actualUser[-4], DATA.actualUser[-3], DATA.actualUser[-2], DATA.actualUser[-1]]


        knockout = []
        for i in reversed(range(len(DATA.actualUser))):
            if DATA.actualUser[i] != "!" and DATA.actualUser[i] != "_BRAIN_" and DATA.actualUser[i] != "None" and DATA.brainUser[i] not in knockout:
                knockout.append(DATA.actualUser[i])
                if DATA.brainUser[i] == "!" or DATA.brainUser[i] == DATA.settings["myname"]:
                    for myname in DATA.settings["mynames"].split("|"):
                        result = result.replace(myname, DATA.actualUser[i])
                else:
                    result = result.replace(DATA.brainUser[i], DATA.actualUser[i])



        #重要な単語を最大5個置き換える
        try:
            if DATA.replaceWords:
                i = len(DATA.data["sentence"][DATA.heart][2])
                knockout = []
                ii = 0
                while True:
                    if ii == i:
                        break
                    if DATA.wordMemory[ii] != "None" and DATA.data["sentence"][DATA.heart][2][ii] != "None" and DATA.data["sentence"][DATA.heart][2][ii] not in knockout:
                        result = result.replace(DATA.data["sentence"][DATA.heart][2][ii], DATA.wordMemory[ii])
                        knockout.append(DATA.wordMemory[ii])
                    ii += 1
        except:
            pass

        DATA.myVoice = result
        DATA.lastSentence = result


        DATA.maeheart = DATA.heart
    


        print("rate: ", DATA.rate)
        print("単語: ", DATA.wordMemory)

    except:
        import traceback
        traceback.print_exc()
        return None


