import DATA
import random
import operator
import re
import difflib
differ = difflib.Differ()

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
    x_body = x.split("\t", 1)[1] if "\t" in x and not ignoreTab else x
    numberToWord = []
    replacements = []
    
    # 差分を取得
    for n in range(len(inputsHeart.split("\t"))):
        diffs = list(differ.compare(inputsHeart.split("\t")[n].replace("!input-", ""), inputs.split("\t")[n]))
        old = ""
        new = ""

        i = 0
        j = ""
        k = 0
        l = ""
        m = False
        o = ""
        for diff in diffs:
            i += 1
            tag = diff[:2]
            content = diff[2:]

            if tag == "- ":
                m = True
                if j != "- ":
                    if o:
                        replacements.append((o, o))
                        o = ""
                    old += l
                    new += l
                    j = "- "
                    k = 0
                    l = ""
                old += content
            elif tag == "+ ":
                m = True
                if j != "+ ":
                    if o:
                        replacements.append((o, o))
                        o = ""
                    old += l
                    new += l
                    j = "+ "
                    k = 0
                    l = ""
                new += content
            elif tag == "  ":
                if m:
                    k += 1
                    l += content
                    if k >= 2 or i >= len(inputs) - 1:
                        if old and new:
                            replacements.append((old, new))
                        old = ""
                        new = ""
                        k = 0
                        l = ""
                j = "  "

        if o:
            replacements.append((o, o))
        if old and new:
            replacements.append((old, new))
        old = ""
        new = ""
        j = ""
        k = 0
        l = ""
        o = ""

    i = 0
    j = 0
    k = False
    for old, new in replacements:
        if old == None:
            continue
        for n in range(len(inputsHeart.split("\t"))):
            if old not in inputsHeart.split("\t")[n].replace("!input-", "") or new not in inputs.split("\t")[n]:
                if k:
                    j -= 1
            else:
                if not k:
                    k =  True
                j = 4
        if j <= 0:
            replacements[i] = (None, None)
        j = 0
        i += 1


    # 置換処理
    for old, new in reversed(replacements):
        if old == None:
            continue
        if old in x_body:
            if not bool(re.search("\[(.*?){}(.*?)\]".format(re.escape(old)), x_body)):
                print(f"{old} => {new}")
                wordNumber = "[word_"+str(random.randint(0, 1000000))+"]"
                x_body = x_body.replace(old, wordNumber)
                numberToWord.append([wordNumber, new])
    for ntw in numberToWord:
        x_body = x_body.replace(ntw[0], ntw[1])

    return x_body