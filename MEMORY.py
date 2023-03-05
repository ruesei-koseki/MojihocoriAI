import DATA
import INTELLIGENCE
import json
import random

def learnSentence(x, u):
    #名前置き換え
    if u != "!":
        x = x.replace(u, "[I]")
    for myname in DATA.settings["mynames"].split("|"):
        x = x.replace(myname, "[YOU]")
    #言葉を脳に記録する
    if u in DATA.settings["mynames"].split("|"):
        DATA.data["sentence"].append([x, "!"])
    else:
        DATA.data["sentence"].append([x, u])
    
    save()

def save():
    if len(DATA.data["sentence"]) >= 10000000:
        while len(DATA.data["sentence"]) >= 10000000:
            del DATA.data["sentence"][0]
    with open(DATA.direc+"/data.json", "w", encoding="utf8") as f:
        json.dump(DATA.data, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))

def learnWord(x):
    a = False
    for word in DATA.data["words"]:
        if word[0] == x:
            a = True
    if a:
        DATA.data["words"].append([x, [DATA.heart]])
        print("新しい単語: {}".format(x))
        save()