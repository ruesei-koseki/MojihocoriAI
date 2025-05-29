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
    numberToWord = []
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
    x_body_copy = x_body
    inputsHeart_copy = inputsHeart
    for old, new in replacements:
        if old in x_body:
            print(f"{old} => {new}")
            wordNumber = "[word_"+str(random.randint(0, 1000000))+"]"
            inputsHeart_copy = inputsHeart_copy.replace(old, wordNumber)
            x_body_copy = x_body_copy.replace(old, wordNumber)
            numberToWord.append([wordNumber, new])
    for ntw in reversed(numberToWord):
        inputsHeart_copy = inputsHeart_copy.replace(ntw[0], ntw[1])
    for ntw in reversed(numberToWord):
        x_body_copy = x_body_copy.replace(ntw[0], ntw[1])
    x_body = x_body_copy

    return x_body