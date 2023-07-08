import DATA
import INTELLIGENCE
import json
import random

countOfMe = 0
isActiveLearn = True
def learnSentence(x, u, save=True):
    global countOfMe, isActiveLearn
    if "!" not in u:
        isActiveLearn == True
        countOfMe = 0
    if isActiveLearn:
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
            DATA.data["sentence"].append([x, "!"])
        else:
            DATA.data["sentence"].append([x, u])
        if u == "!output":
            DATA.data["sentence"].append(["!good", "!system"])

        if countOfMe >= 3:
            isActiveLearn = False

        if "!" in u:
            countOfMe += 1

        if save:
            saveData()

def saveData():
    if len(DATA.data["sentence"]) >= 100000000:
        while len(DATA.data["sentence"]) >= 100000000:
            del DATA.data["sentence"][0]
    with open(DATA.direc+"/data.json", "w", encoding="utf8") as f:
        json.dump(DATA.data, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
