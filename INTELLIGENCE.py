import DATA
import random

def isNextOk():
    for iiiii in range(7):
        if DATA.heart+1+iiiii < len(DATA.data["sentence"]) - 1:
            if DATA.data["sentence"][DATA.heart+1+iiiii][0] == "×":
                return False
    if len(DATA.data["sentence"]) - 1 <= DATA.heart+1:
        return False
    else:
        return DATA.lastSentenceInput != DATA.data["sentence"][DATA.heart+1][0] and DATA.lastSentence != DATA.data["sentence"][DATA.heart+1][0] and DATA.data["sentence"][DATA.heart+1][1] == DATA.data["sentence"][DATA.heart][1] and DATA.data["sentence"][DATA.heart+1][1] != "!" and "!system" not in DATA.data["sentence"][DATA.heart+1][1]

def replaceWords(x, inputs, inputsHeart):
    xx = x
    result = x.split(": ", 1)[1]
    for i in reversed(range(len(inputs))):
        x = xx
        for word in reversed(sorted(DATA.data["words"], key=len)):
            if word in inputs[i] and word not in inputsHeart[i] and word not in x:
                for word2 in reversed(sorted(DATA.data["words"], key=len)):
                    if word2 in x and word2 in inputsHeart[i] and word2 not in inputs[i]:
                        result = result.replace(word2, word)
                        break
                    inputsHeart[i] = inputsHeart[i].replace(word2, "")
                    x = x.replace(word2, "")
            inputs[i] = inputs[i].replace(word, "")
    return result