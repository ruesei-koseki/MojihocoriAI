import DATA
import random
import operator

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
    result = x.split(": ", 1)[1]
    used = []
    word1_ = []
    word2_ = []
    ipts = inputs
    iptsh = inputsHeart
    for word in reversed(sorted(DATA.data["words"], key=len)):
        if word in ipts:
            word1_.append(word)
            ipts = ipts.replace(word, "")
    for word in reversed(sorted(DATA.data["words"], key=len)):
        if word in iptsh:
            word2_.append(word)
            iptsh = iptsh.replace(word, "")
    ipts = inputs
    iptsh = inputsHeart
    word1 = []
    word2 = []
    while True:
        a = []
        for w1 in word1_:
            if w1 in ipts:
                a.append([w1, ipts.find(w1)])
        if a == []:
            break
        a = sorted(a, key=operator.itemgetter(1))
        if a[0][0] not in [" ", "", "　"]:
            word1.append(a[0])
        ipts = ipts[ipts.find(a[0][0])+len(a[0][0]):]
    while True:
        a = []
        for w2 in word2_:
            if w2 in iptsh:
                a.append([w2, iptsh.find(w2)])
        if a == []:
            break
        a = sorted(a, key=operator.itemgetter(1))
        if a[0][0] not in [" ", "", "　"]:
            word2.append(a[0])
        iptsh = iptsh[iptsh.find(a[0][0])+len(a[0][0]):]
    word1 = list(reversed(word1))
    word2 = list(reversed(word2))
    word1.insert(0, ["_BOS_", 0])
    word1.insert(0, ["_BOS_", 0])
    word1.append(["_EOS_", 0])
    word1.append(["_EOS_", 0])
    word2.insert(0, ["_BOS_", 0])
    word2.insert(0, ["_BOS_", 0])
    word2.append(["_EOS_", 0])
    word2.append(["_EOS_", 0])
    i = 2
    while True:
        j = 2
        l = len(word1) - 3
        m = len(word2) - 3
        if i > l:
            break
        while True:
            if j > m:
                break
            if word1[i] != word2[j] and word1[i-1][0] == word2[j-1][0] and word1[i+1][0] == word2[j+1][0]:
                result = result.replace(word2[j][0], "_/_".join(word1[i][0]))
            j += 1
        i += 1
    result = result.replace("_/_", "")
    return result