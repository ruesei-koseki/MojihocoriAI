import DATA
import re
from janome.tokenizer import Tokenizer

t = Tokenizer(wakati=True)

def wordSyori(x):
    result = list(t.tokenize(x))
    result.sort(key=len, reverse=True)
    i = 0
    for r in result:
        if i >= 2:
            break
        DATA.wordMemory.append(r)
        i += 1
    if len(DATA.wordMemory) > 2:
        DATA.wordMemory = DATA.wordMemory[-2:]
    


def isNextOk():
    if len(DATA.data["sentence"]) - 1 <= DATA.heart:
        return False
    else:
        return DATA.heart != len(DATA.data["sentence"]) and DATA.lastSentenceInput != DATA.data["sentence"][DATA.heart+1][0] and DATA.lastSentence != DATA.data["sentence"][DATA.heart+1][0] and DATA.data["sentence"][DATA.heart+1][1] == DATA.data["sentence"][DATA.heart][1]
                            