import DATA
import re


def isNextOk():
    for iiiii in range(7):
        if DATA.heart+1+iiiii < len(DATA.data["sentence"]) - 1:
            if DATA.data["sentence"][DATA.heart+1+iiiii][0] == "×":
                return False        
    if len(DATA.data["sentence"]) - 1 <= DATA.heart+1:
        return False
    else:
        return DATA.heart != len(DATA.data["sentence"]) - 1 and DATA.lastSentenceInput != DATA.data["sentence"][DATA.heart+1][0] and DATA.lastSentence != DATA.data["sentence"][DATA.heart+1][0] and DATA.data["sentence"][DATA.heart+1][1] == DATA.data["sentence"][DATA.heart][1]
                            
def hIsNextOk():
    for iiiii in range(7):
        if DATA.Hheart+1+iiiii < len(DATA.data["sentenceHumanity"]) - 1:
            if DATA.data["sentenceHumanity"][DATA.Hheart+1+iiiii][0] == "×":
                return False        
    if len(DATA.data["sentenceHumanity"]) - 1 <= DATA.Hheart+1:
        return False
    else:
        return DATA.Hheart != len(DATA.data["sentenceHumanity"]) - 1 and DATA.lastSentenceInput != DATA.data["sentenceHumanity"][DATA.Hheart+1][0] and DATA.lastSentence != DATA.data["sentenceHumanity"][DATA.Hheart+1][0] and DATA.data["sentenceHumanity"][DATA.Hheart+1][1] == DATA.data["sentenceHumanity"][DATA.Hheart][1]
                            