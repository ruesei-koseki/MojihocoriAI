import DATA
import INTELLIGENCE
import json

maeX = ""
maeX2 = ""
def addSentence(x, u, noword=False):
    global maeX
    #言葉を脳に記録する
    if maeX != x:
        #名前置き換え
        if u != "!":
            x = x.replace(u, "[I]")
        for myname in DATA.settings["mynames"].split("|"):
            x = x.replace(myname, "[YOU]")
        #学習
        if u == DATA.lastUserReplied:
            DATA.data["sentence"].append([x, "!"])
        elif u == "!":
            DATA.data["sentence"].append([x, DATA.lastUserReplied])
        elif DATA.lastUserReplied in DATA.userLog:
            DATA.data["sentence"].append([x, u])
    maeX = x

    if len(DATA.data["sentence"]) >= 120000:
        while len(DATA.data["sentence"]) >= 120000:
            del DATA.data["sentence"][0]
            DATA.heart -= 1
            DATA.maeheart -= 1




def learnSentence(x, u, noword=False):
    global maeX2
    #言葉を脳に記録する
    if maeX2 != x:
        if u in DATA.settings["mynames"].split("|"):
            DATA.data["sentence"].append([x, "!"])
        else:
            DATA.data["sentence"].append([x, u])
    maeX2 = x




def save():
    if len(DATA.data["sentence"]) >= 1000000:
        while len(DATA.data["sentence"]) >= 1000000:
            del DATA.data["sentence"][0]
    with open(DATA.direc+"/data.json", "w", encoding="utf8") as f:
        json.dump(DATA.data, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))

