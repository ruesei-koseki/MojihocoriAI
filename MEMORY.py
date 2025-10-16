import DATA
import mojihocori
import json
import random
import INTELLIGENCE
from janome.tokenizer import Tokenizer
t = Tokenizer()

def learnSentence(x, u, save=True, mama=False):
    #if len(DATA.data["sentence"]) >= 1000 or mama:
    
    #mamaがTrueのときに自分の名前以外を無効にする
    if u not in DATA.settings["mynames"].split("|") and mama and u not in ["!input", "!output", "!system"]:
        u = "!input-"+u

    #言葉を脳に記録する
    if u in DATA.settings["mynames"].split("|"):
        DATA.data["sentence"].append([x, "!output"])
    else:
        DATA.data["sentence"].append([x, u])
    findWords(x)

    if len(DATA.data["sentence"]) >= 1600000:
        while len(DATA.data["sentence"]) >= 1600000:
            del DATA.data["sentence"][0]
            if DATA.heart >= 5 or DATA.maeheart >= 5:
                DATA.heart -= 1
                DATA.maeheart -= 1
    if save:
        saveData()

def findWords(x):
    words = x.split()  # スペースで区切られた単語を検出
    for word in words:
        if word not in DATA.data["words"] and word != x and len(word) <= 9:  # 既に記憶されていない単語のみ追加
            if word != "":
                DATA.data["words"].append(word)
    for w in list(t.tokenize(x, wakati=True)):
        if w not in DATA.data["words"]:  # 既に記憶されていない単語のみ追加
            if w != "":
                DATA.data["words"].append(w)
    ws = x
    for w in list(t.tokenize(x, wakati=True)):
        ws = ws.replace(w, "|separator|")
    for ww in ws.split("|separator|"):
        if ww not in DATA.data["words"]:  # 既に記憶されていない単語のみ追加
            if ww != "":
                DATA.data["words"].append(ww)

def saveData():
    with open(DATA.direc+"/data.json", "w", encoding="utf8") as f:
        json.dump(DATA.data, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))

def evalute():
    flag1 = False
    flag2 = False
    if DATA.data["sentence"][len(DATA.data["sentence"])-1][0] != "!bad" and DATA.data["sentence"][len(DATA.data["sentence"])-1][0] != "!good":
        if DATA.heart+1 < len(DATA.data["sentence"]) - 1:
            if DATA.data["sentence"][DATA.heart+1][0] == "!good" and DATA.data["sentence"][-1][0] != "!good":
                flag1 = True
        if flag1:
            print("このメッセージは良い")
            mojihocori.receive("!good", "!system", reply=False)

    if DATA.data["sentence"][len(DATA.data["sentence"])-1][0] != "!bad" and DATA.data["sentence"][len(DATA.data["sentence"])-1][0] != "!good" and not flag1:
        if DATA.heart+1 < len(DATA.data["sentence"]) - 1:
            if DATA.data["sentence"][DATA.heart+1][0] == "!bad" and DATA.data["sentence"][-1][0] != "!bad":
                flag2 = True
        if flag2:
            print("このメッセージは悪い")
            mojihocori.receive("!bad", "!system", reply=False)