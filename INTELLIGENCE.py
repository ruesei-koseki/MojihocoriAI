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

    # 差分を取得
    diffs = list(differ.compare(inputsHeart, inputs))

    replacements = []
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
            if old and new:
                replacements.append((old, new))
            old = ""
            new = ""

    # 最後に残ったやつ
    if old and new:
        replacements.append((old, new))

    # 置換処理
    already_used = []
    for old, new in replacements:
        if old in x_body and old not in already_used:
            print(f"{old} => {new}")
            x_body = x_body.replace(old, new)
            already_used.append(new)

    return x_body