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
        o = ""
        for diff in diffs:
            i += 1
            tag = diff[:2]
            content = diff[2:]

            if tag == "- ":
                if j != "- ":
                    if o:
                        replacements.append((o, o))
                        o = ""
                    j = "- "
                old += content
            elif tag == "+ ":
                if j != "+ ":
                    if o:
                        replacements.append((o, o))
                        o = ""
                    j = "+ "
                new += content
            elif tag == "  ":
                o += content
                if old and new:
                    replacements.append((old, new))
                old = ""
                new = ""
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

    i = 0
    deletes = []
    for old, new in replacements:
        if old == None:
            continue
        for n in range(len(inputsHeart.split("\t"))):
            if old in inputs.split("\t")[n] and old in inputsHeart.split("\t")[n]:
                replacements[i] = (None, None)
                break
        for old2, new2 in replacements:
            if old2 == None:
                continue
            if old in old2 and old2 in x_body and old != old2:
                replacements[i] = (None, None)
                break
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