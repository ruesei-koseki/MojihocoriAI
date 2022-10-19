import DATA
import re

def wordSyori(x):
    if len(DATA.wordMemory) > 8:
        DATA.wordMemory = DATA.wordMemory[-7:]


def isNextOk():
    if len(DATA.data["sentence"]) - 1 <= DATA.heart:
        return False
    else:
        return DATA.data["sentence"][DATA.heart+1][1] == DATA.data["sentence"][DATA.heart][1] and not bool(re.search(DATA.settings["mynames"], DATA.data["sentence"][DATA.heart+1][0]))
