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
    # 差分を取得
    diffs = list(differ.compare(inputsHeart, inputs))

    replacements = []
    old = ""
    new = ""

    i = 0
    j = ""
    k = 0
    l = ""
    m = False
    for diff in diffs:
        i += 1
        tag = diff[:2]
        content = diff[2:]

        if content == "\t":
            m = False
            if old and new:
                replacements.append((old, new))
            old = ""
            new = ""
            j = ""
            k = 0
            l = ""
            continue
        if tag == "- ":
            m = True
            if j != "- ":
                old += l
                new += l
                j = "- "
                k = 0
                l = ""
            old += content
        elif tag == "+ ":
            m = True
            if j != "+ ":
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
                if k >= 3 or i >= len(inputs) - 1:
                    if old and new:
                        replacements.append((old, new))
                    old = ""
                    new = ""
                    k = 0
                    l = ""
            j = "  "

    # 置換処理
    inputsHeart_copy = inputsHeart
    for old, new in replacements:
        if old in x_body:
            if not bool(re.search("\[word\_(.*?){}(.*?)\]".format(old), x_body)) and not bool(re.search("\[word\_(.*?){}(.*?)\]".format(old), inputsHeart_copy)):
                print(f"{old} => {new}")
                wordNumber = "[word_"+str(random.randint(0, 1000000))+"]"
                inputsHeart_copy = inputsHeart_copy.replace(old, wordNumber)
                x_body = x_body.replace(old, wordNumber)
                numberToWord.append([wordNumber, new])
    for ntw in numberToWord:
        inputsHeart_copy = inputsHeart_copy.replace(ntw[0], ntw[1])
        x_body = x_body.replace(ntw[0], ntw[1])

    return x_body