import DATA
import INTELLIGENCE
import json

maeX = ""
def addSentence(x, u, noword=False):
    global maeX
    #言葉を脳に記録する
    if maeX == x:
        pass
    else:
        DATA.data["sentence"].append([x, u])
        maeX = x

    if len(DATA.data["sentence"]) >= 120000:
        while len(DATA.data["sentence"]) >= 120000:
            del DATA.data["sentence"][0]
            DATA.heart -= 1
            DATA.maeheart -= 1





def save():
    if len(DATA.data["sentence"]) >= 100000:
        while len(DATA.data["sentence"]) >= 100000:
            del DATA.data["sentence"][0]
    with open(DATA.direc+"/data.json", "w", encoding="utf8") as f:
        json.dump(DATA.data, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))

