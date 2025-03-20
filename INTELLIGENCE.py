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
    x = x.split(": ", 1)[1]
    word1_ = []
    word2_ = []
    word3_ = []
    ipts = inputs
    iptsh = inputsHeart
    xx = x
    for word in sorted(DATA.data["words"], key=len, reverse=True):
        if word in ipts:
            word1_.append(word)
            ipts = ipts.replace(word, "")
    for word in sorted(DATA.data["words"], key=len, reverse=True):
        if word in iptsh:
            word2_.append(word)
            iptsh = iptsh.replace(word, "")
    for word in sorted(DATA.data["words"], key=len, reverse=True):
        if word in xx:
            word3_.append(word)
            xx = xx.replace(word, " ")
    for w in xx.split():
        word3_.append(w)
    ipts = inputs
    iptsh = inputsHeart
    xx = x
    word1 = []
    word2 = []
    word3 = []
    while True:
        a = []
        for w1 in word1_:
            if w1 in ipts:
                a.append([w1, ipts.find(w1)])
        if a == []:
            break
        a = sorted(a, key=lambda x: (x[1], -len(x[0])))
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
        a = sorted(a, key=lambda x: (x[1], -len(x[0])))
        if a[0][0] not in [" ", "", "　"]:
            word2.append(a[0])
        iptsh = iptsh[iptsh.find(a[0][0])+len(a[0][0]):]
    while True:
        a = []
        for w3 in word3_:
            if w3 in xx:
                a.append([w3, xx.find(w3)])
        if a == []:
            break
        a = sorted(a, key=lambda x: (x[1], -len(x[0])))
        word3.append(a[0][0])
        xx = xx[xx.find(a[0][0])+len(a[0][0]):]
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
    used = []
    i = 2
    l = len(word1) - 3
    while True:
        j = 2
        m = len(word2) - 3
        if i > l:
            break
        while True:
            if j > m:
                break
            if word2[j][0] not in used and word1[i-1][0] == word2[j-1][0] and word1[i+1][0] == word2[j+1][0]:
                for k in range(len(word3)):
                    if word3[k] == word2[j][0]:
                        word3[k] = word1[i][0]
                used.append(word1[i][0])
            j += 1
        i += 1
    return "".join(word3)