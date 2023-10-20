import DATA
import INTELLIGENCE
import json
import random

def learnSentence(x, u, save=True):
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
        DATA.data["sentence"].append(["!good", "!system"])
    else:
        DATA.data["sentence"].append([x, u])
    if u == "!output":
        DATA.data["sentence"].append(["!good", "!system"])

    if len(DATA.data["sentence"]) >= 1000000:
        while len(DATA.data["sentence"]) >= 1000000:
            del DATA.data["sentence"][0]
            if DATA.heart >= 5 or DATA.maeheart >= 5:
                DATA.heart -= 1
                DATA.maeheart -= 1
    if save:
        saveData()

def saveData():
    with open(DATA.direc+"/data.json", "w", encoding="utf8") as f:
        json.dump(DATA.data, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
