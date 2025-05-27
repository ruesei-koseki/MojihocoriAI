import DATA
import random
import operator
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

def replaceWords(x, inputs, inputsHeart):
    # 本体を取り出す
    x_body = x.split("\t", 1)[1] if "\t" in x else x

    already_used = []
    for i in reversed(range(len(inputs))):
        # 差分を取得
        diffs = list(differ.compare(inputsHeart[i], inputs[i]))

        replacements = []
        old = ""
        new = ""

        i = 0
        j = ""
        k = 0
        l = ""
        for diff in diffs:
            tag = diff[:2]
            content = diff[2:]

            if tag == "- ":
                if j != "- ":
                    old += l
                    new += l
                    if i >= 2:
                        if old and new:
                            replacements.append((old, new))
                        old = ""
                        new = ""
                        i = 0
                        j = ""
                    i += 1
                    j = "- "
                    k = 0
                    l = ""
                old += content
            elif tag == "+ ":
                if j != "+ ":
                    old += l
                    new += l
                    if i >= 2:
                        if old and new:
                            replacements.append((old, new))
                        old = ""
                        new = ""
                        i = 0
                        j = ""
                    i += 1
                    j = "+ "
                    k = 0
                    l = ""
                new += content
            elif tag == "  ":
                k += 1
                l += content
                if k >= 3 or content == "\t":
                    if old and new:
                        replacements.append((old, new))
                    old = ""
                    new = ""
                    i = 0
                    j = ""
                    k = 0
                    l = ""

        # 置換処理
        for old, new in replacements:
            if old in x_body and [new, old] not in already_used:
                print(f"{old} => {new}")
                x_body = x_body.replace(old, new)
                already_used.append([old, new])

    return x_body