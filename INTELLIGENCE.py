import DATA
import difflib

def isNextOk():
    for iiiii in range(7):
        if DATA.heart+1+iiiii < len(DATA.data["sentence"]) - 1:
            if DATA.data["sentence"][DATA.heart+1+iiiii][0] == "×":
                return False
    if len(DATA.data["sentence"]) - 1 <= DATA.heart+1:
        return False
    else:
        return DATA.lastSentenceInput != DATA.data["sentence"][DATA.heart+1][0] and DATA.lastSentence != DATA.data["sentence"][DATA.heart+1][0] and DATA.data["sentence"][DATA.heart+1][1] == DATA.data["sentence"][DATA.heart][1] and DATA.data["sentence"][DATA.heart+1][1] != "!" and "!system" not in DATA.data["sentence"][DATA.heart+1][1]

def replaceWords(x, inputs, inputsHeart, ignoreTab=False):
    # 本体を取り出す
    replacements = []

    word3 = []
    word3_ = []
    xx = x
    for word in sorted(DATA.data["words"], key=len, reverse=True):
        if word in xx:
            word3_.append(word)
            xx = xx.replace(word, " ")
    for w in xx.split():
        word3_.append(w)
    xx = x
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
        
    for i in range(0, len(inputs)):
        word1_ = []
        word2_ = []
        ipts = inputs[i]
        iptsh = inputsHeart[i]
        for word in sorted(DATA.data["words"], key=len, reverse=True):
            if word in ipts:
                word1_.append(word)
                ipts = ipts.replace(word, "")
        for w in ipts.split():
            word1_.append(w)
        for word in sorted(DATA.data["words"], key=len, reverse=True):
            if word in iptsh:
                word2_.append(word)
                iptsh = iptsh.replace(word, "")
        for w in iptsh.split():
            word2_.append(w)
        ipts = inputs[i]
        iptsh = inputsHeart[i]
        word1 = []
        word2 = []
        while True:
            a = []
            for w1 in word1_:
                if w1 in ipts:
                    a.append([w1, ipts.find(w1)])
            if a == []:
                break
            a = sorted(a, key=lambda x: (x[1], -len(x[0])))
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
            word2.append(a[0])
            iptsh = iptsh[iptsh.find(a[0][0])+len(a[0][0]):]
        word1 = list(word1)
        word2 = list(word2)

        w1 = []
        for wo1 in word1:
            w1.append(wo1[0])
        w2 = []
        for wo2 in word2:
            w2.append(wo2[0])

        # 差分を取得
        diffs = list(difflib.ndiff(w2, w1))
        old = ""
        new = ""
        for diff in diffs:
            tag = diff[:2]
            content = diff[2:]

            if tag == "- ":
                old += content
            elif tag == "+ ":
                new += content
            elif tag == "  ":
                if old or new:
                    replacements.append((old, new))
                    old = ""
                    new = ""
                replacements.append((content, content))
        if old or new:
            replacements.append((old, new))  # 最後に残ったやつ

    # 置換処理
    i = 0
    temp = ""
    temp2 = ""
    temp3 = []
    for wo3 in word3:
        for old, new in reversed(replacements):
            if wo3 == old:
                print("{} => {}".format(old, new))
                word3[i] = new
                temp = ""
                temp2 = ""
                break
            elif wo3 == temp:
                print("{} => {}".format(temp, temp2))
                for t3 in temp3:
                    word3[t3] = ""
                word3[i] = temp2
                temp = ""
                temp2 = ""
                break
            elif wo3 in old:
                temp = old.replace(wo3, "")
                temp2 = new
                temp3.append(i)
                break
            elif wo3 in temp:
                temp = temp.replace(wo3, "")
                temp3.append(i)
                break
        i += 1
    result = "".join(word3)
    return result