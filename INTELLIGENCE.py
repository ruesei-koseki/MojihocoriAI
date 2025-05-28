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

def replaceWords(x, inputs, inputsHeart, ignoreTab=False):
    # 本体を取り出す
    x_body = x.split("\t", 1)[1] if "\t" in x and not ignoreTab else x

    already_used = []
    for i in range(len(inputs)):
        # 差分を取得
        diffs = list(differ.compare(inputsHeart[i], inputs[i]))

        replacements = []
        old = ""
        new = ""

        j = ""
        k = 0
        l = ""
        m = False
        for diff in diffs:
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
        x_body_copy = x_body
        inputsHeart_copy = inputsHeart[i]
        for old, new in replacements:
            if old in x_body and old not in already_used:
                if inputsHeart[i].replace(old, new) == inputs[i]:
                    print(f"{old} => {new}")
                    inputsHeart_copy = inputsHeart_copy.replace(old, new)
                    x_body_copy = x_body_copy.replace(old, new)
                    already_used.append(new)
        if inputsHeart_copy == inputs[i]:
            x_body = x_body_copy

    return x_body