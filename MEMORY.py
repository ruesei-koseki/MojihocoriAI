import DATA
import INTELLIGENCE
import json
def learnSentence(x, u, noword=False):
    #名前置き換え
    if u != "!":
        x = x.replace(u, "[I]")
    for myname in DATA.settings["mynames"].split("|"):
        x = x.replace(myname, "[YOU]")
def save():
    if len(DATA.data["sentence"]) >= 10000000:
        while len(DATA.data["sentence"]) >= 10000000:
            del DATA.data["sentence"][0]
    with open(DATA.direc+"/data.json", "w", encoding="utf8") as f:
        json.dump(DATA.data, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))