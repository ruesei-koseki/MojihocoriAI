import DATA
import INTELLIGENCE
import json
import CONSIDERATION

def learnSentence(x, u, save=True, mama=False):
    #if len(DATA.data["sentence"]) >= 1000 or mama:
        
    #名前置き換え
    if u == "!input":
        for myname in DATA.settings["mynames"].split("|"):
            x = x.replace(myname, "[YOU]")
    elif u == "!output":
        for myname in DATA.settings["mynames"].split("|"):
            x = x.replace(myname, "[I]")
    elif u != "!":
        x = x.replace(DATA.lastUser, "[I]")
        for myname in DATA.settings["mynames"].split("|"):
            x = x.replace(myname, "[YOU]")
    else:
        for myname in DATA.settings["mynames"].split("|"):
            x = x.replace(myname, "[I]")
        x = x.replace(DATA.lastUser, "[YOU]")
    #mamaがTrueのときに自分の名前以外を無効にする
    if u not in DATA.settings["mynames"].split("|") and mama and u not in ["!input", "!output", "!system"]:
        u = "!input-"+u
    #言葉を脳に記録する
    if u in DATA.settings["mynames"].split("|"):
        DATA.data["sentence"].append([x, "!output"])
    else:
        DATA.data["sentence"].append([x, u])

    flag1 = False
    flag2 = False
    if "!" in u[0] and not mama:
        if x != "!bad" and x != "!good":
            if DATA.heart+1 < len(DATA.data["sentence"]) - 1:
                if DATA.data["sentence"][DATA.heart+1][0] == "!good":
                    flag1 = True
            if flag1:
                print("このメッセージは良い")
                DATA.data["sentence"].append(["!good", "!system"])
                result = CONSIDERATION.looking("!good", "!system")

        if x != "!bad" and x != "!good" and not flag1:
            if DATA.heart+1 < len(DATA.data["sentence"]) - 1:
                if DATA.data["sentence"][DATA.heart+1][0] == "!bad":
                    flag2 = True
            if flag2:
                print("このメッセージは悪い")
                DATA.data["sentence"].append(["!bad", "!system"])
                result = CONSIDERATION.looking("!bad", "!system")
        

    if len(DATA.data["sentence"]) >= 1600000:
        while len(DATA.data["sentence"]) >= 1600000:
            del DATA.data["sentence"][0]
            if DATA.heart >= 5 or DATA.maeheart >= 5:
                DATA.heart -= 1
                DATA.maeheart -= 1
    if save:
        saveData()

def saveData():
    with open(DATA.direc+"/data.json", "w", encoding="utf8") as f:
        json.dump(DATA.data, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
