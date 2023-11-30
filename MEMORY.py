import DATA
import INTELLIGENCE
import json
import random

def learnSentence(x, u, save=False):
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
    #言葉を脳に記録する
    if u in DATA.settings["mynames"].split("|"):
        DATA.data["sentence"].append([x, "!output"])
    else:
        DATA.data["sentence"].append([x, u])

    if x != "!good":
        flag = False
        for iiiii in range(6):
            if DATA.heart+1+iiiii < len(DATA.data["sentence"]) - 1:
                if DATA.data["sentence"][DATA.heart+1+iiiii][0] == "!good":
                    flag = True
                    break
        if flag:
            DATA.data["sentence"].append(["!good", "!system"])

    if x != "!bad":
        flag = False
        for iiiii in range(6):
            if DATA.heart+1+iiiii < len(DATA.data["sentence"]) - 1:
                if DATA.data["sentence"][DATA.heart+1+iiiii][0] == "!bad":
                    flag = True
                    break
        if flag:
            DATA.data["sentence"].append(["!bad", "!system"])


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
