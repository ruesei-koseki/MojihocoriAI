import DATA
import re
import random

def isNextOk():
    for iiiii in range(7):
        if DATA.heart+1+iiiii < len(DATA.data["sentence"]) - 1:
            if DATA.data["sentence"][DATA.heart+1+iiiii][0] == "×":
                return False        
    if len(DATA.data["sentence"]) - 1 <= DATA.heart+1:
        return False
    else:
        return DATA.heart != len(DATA.data["sentence"]) - 1 and DATA.lastSentenceInput != DATA.data["sentence"][DATA.heart+1][0] and DATA.lastSentence != DATA.data["sentence"][DATA.heart+1][0] and DATA.data["sentence"][DATA.heart+1][1] == DATA.data["sentence"][DATA.heart][1] and DATA.data["sentence"][i+1][0] != "☓" and DATA.data["sentence"][i+1][0] != "×" and DATA.data["sentence"][i+1][0] != "❌" and DATA.data["sentence"][i+1][0] != "⭕" and DATA.data["sentence"][i+1][0] != "○"

def replaceWords(x1, x2):
    result = x2
    for afterWord in random.sample(DATA.data["words"], len(DATA.data["words"])):
        if afterWord[0] in x1:
            for beforeWord in random.sample(DATA.data["words"], len(DATA.data["words"])):
                if beforeWord[0] in x2:
                    result = result.replace(beforeWord[0], afterWord[0])
    return result