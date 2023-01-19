import DATA
import INTELLIGENCE
import json
import copy
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
def save():
    if len(DATA.data["sentence"]) >= 10000000:
        while len(DATA.data["sentence"]) >= 10000000:
            del DATA.data["sentence"][0]
    with open(DATA.direc+"/data.json", "w", encoding="utf8") as f:
        json.dump(DATA.data, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))