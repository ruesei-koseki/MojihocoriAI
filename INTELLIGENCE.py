import DATA
import re
from janome.tokenizer import Tokenizer

t = Tokenizer(wakati=True)


def isNextOk():
    if len(DATA.data["sentence"]) - 1 <= DATA.heart:
        return False
    else:
        return DATA.heart != len(DATA.data["sentence"]) and DATA.lastSentenceInput != DATA.data["sentence"][DATA.heart+1][0] and DATA.lastSentence != DATA.data["sentence"][DATA.heart+1][0] and DATA.data["sentence"][DATA.heart+1][1] == DATA.data["sentence"][DATA.heart][1]
                            