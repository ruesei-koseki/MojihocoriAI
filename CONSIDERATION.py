import DATA
from rapidfuzz.distance import Levenshtein

def looking(x, u, reply=True, force=False):
    #過去の発言をもとに考える
    try:
        x = x.replace(DATA.lastUser, "[I]")
        for myname in DATA.settings["mynames"].split("|"):
            x = x.replace(myname, "[YOU]")
        print("思考中: {}".format(x))

        for kaisu in range(4):
            if kaisu == 0:
                rate = 1
            if kaisu == 1:
                rate = 0.9
            if kaisu == 2:
                rate = 0.8
            if kaisu == 3:
                rate = 0.7
            #今の気持ちから考える
            f = DATA.heart
            t = len(DATA.data["sentence"]) - 1
            i = f
            ii = 0
            for sen in DATA.data["sentence"][f:t]:
                if i >= len(DATA.data["sentence"]) - 1:
                    break
                if Levenshtein.normalized_similarity(x, DATA.data["sentence"][i][0]) >= rate:
                    if i+1 >= len(DATA.data["sentence"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentence"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentence"]) and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentence) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentence"][i+1][1] != "!" and DATA.data["sentence"][i+1][1] != "!input" and DATA.data["sentence"][i+1][0] != "!bad" and DATA.data["sentence"][i+1][0] != "!good" and "!system" not in DATA.data["sentence"][i+1][1] and "!input-" not in DATA.data["sentence"][i+1][1]:
                            flag = False
                            for iiiii in range(3):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "!good":
                                        flag = True
                                        break
                            for iiiii in range(3):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "!bad":
                                        flag = False
                                        break
                            if flag:
                                print("類似: {}, {}, {}".format(DATA.data["sentence"][i][0], i, rate))
                                print("返信: {}, {}".format(DATA.data["sentence"][i+1][0], i+1))
                                DATA.sa = ii
                                DATA.heart = i+1
                                DATA.heartLastSpeaker = DATA.data["sentence"][i+1][1]
                                DATA.rate = rate
                                return DATA.data["sentence"][i+1][0]
                        else:
                            pass
                    else:
                        DATA.heart = i
                        DATA.rate = rate
                        return None
                i += 1
                ii += 1
            #今の気持ちから考える
            f = 0
            t = DATA.heart-1
            i = f
            ii = 0
            for sen in DATA.data["sentence"][f:t]:
                if i >= len(DATA.data["sentence"]) - 1:
                    break
                if Levenshtein.normalized_similarity(x, DATA.data["sentence"][i][0]) >= rate:
                    if i+1 >= len(DATA.data["sentence"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentence"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentence"]) and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentence) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentence"][i+1][1] != "!" and DATA.data["sentence"][i+1][1] != "!input" and DATA.data["sentence"][i+1][0] != "!bad" and DATA.data["sentence"][i+1][0] != "!good" and "!system" not in DATA.data["sentence"][i+1][1] and "!input-" not in DATA.data["sentence"][i+1][1]:
                            flag = False
                            for iiiii in range(3):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "!good":
                                        flag = True
                                        break
                            for iiiii in range(3):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "!bad":
                                        flag = False
                                        break
                            if flag:
                                print("類似: {}, {}, {}".format(DATA.data["sentence"][i][0], i, rate))
                                print("返信: {}, {}".format(DATA.data["sentence"][i+1][0], i+1))
                                DATA.sa = ii
                                DATA.heart = i+1
                                DATA.heartLastSpeaker = DATA.data["sentence"][i+1][1]
                                DATA.rate = rate
                                return DATA.data["sentence"][i+1][0]
                        else:
                            pass
                    else:
                        DATA.heart = i
                        DATA.rate = rate
                        return None
                i += 1
                ii += 1

        for kaisu in range(11):
            if kaisu == 0:
                rate = 1
            if kaisu == 1:
                rate = 0.9
            if kaisu == 2:
                rate = 0.8
            if kaisu == 3:
                rate = 0.7
            if kaisu == 4:
                rate = 0.6
            if kaisu == 5:
                rate = 0.5
            if kaisu == 6:
                rate = 0.4
            if kaisu == 7:
                rate = 0.3
            if kaisu == 8:
                rate = 0.2
            if kaisu == 9:
                rate = 0.1
            if kaisu == 10:
                rate = 0.0
            #今の気持ちから考える
            f = DATA.heart
            t = len(DATA.data["sentence"]) - 1
            i = f
            ii = 0
            for sen in DATA.data["sentence"][f:t]:
                if i >= len(DATA.data["sentence"]) - 1:
                    break
                if Levenshtein.normalized_similarity("{}: {}".format(x, u), "{}: {}".format(DATA.data["sentence"][i][0], DATA.data["sentence"][i][1])) >= rate:
                    if i+1 >= len(DATA.data["sentence"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentence"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentence"]) and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentence) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentence"][i+1][1] != "!" and DATA.data["sentence"][i+1][1] != "!input" and DATA.data["sentence"][i+1][0] != "!bad" and DATA.data["sentence"][i+1][0] != "!good" and "!system" not in DATA.data["sentence"][i+1][1] and "!input-" not in DATA.data["sentence"][i+1][1]:
                            flag = True
                            for iiiii in range(3):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "!bad":
                                        flag = False
                                        break
                            if flag:
                                print("類似: {}, {}, {}".format(DATA.data["sentence"][i][0], i, rate))
                                print("返信: {}, {}".format(DATA.data["sentence"][i+1][0], i+1))
                                DATA.sa = ii
                                DATA.heart = i+1
                                DATA.heartLastSpeaker = DATA.data["sentence"][i+1][1]
                                DATA.rate = rate
                                return DATA.data["sentence"][i+1][0]
                        else:
                            pass
                    else:
                        DATA.heart = i
                        DATA.rate = rate
                        return None
                i += 1
                ii += 1
            #今の気持ちから考える
            f = 0
            t = DATA.heart-1
            i = f
            ii = 0
            for sen in DATA.data["sentence"][f:t]:
                if i >= len(DATA.data["sentence"]) - 1:
                    break
                if Levenshtein.normalized_similarity("{}: {}".format(x, u), "{}: {}".format(DATA.data["sentence"][i][0], DATA.data["sentence"][i][1])) >= rate:
                    if i+1 >= len(DATA.data["sentence"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentence"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentence"]) and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentence) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentence"][i+1][1] != "!" and DATA.data["sentence"][i+1][1] != "!input" and DATA.data["sentence"][i+1][0] != "!bad" and DATA.data["sentence"][i+1][0] != "!good" and "!system" not in DATA.data["sentence"][i+1][1] and "!input-" not in DATA.data["sentence"][i+1][1]:
                            flag = True
                            for iiiii in range(3):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "!bad":
                                        flag = False
                                        break
                            if flag:
                                print("類似: {}, {}, {}".format(DATA.data["sentence"][i][0], i, rate))
                                print("返信: {}, {}".format(DATA.data["sentence"][i+1][0], i+1))
                                DATA.sa = ii
                                DATA.heart = i+1
                                DATA.heartLastSpeaker = DATA.data["sentence"][i+1][1]
                                DATA.rate = rate
                                return DATA.data["sentence"][i+1][0]
                        else:
                            pass
                    else:
                        DATA.heart = i
                        DATA.rate = rate
                        return None
                i += 1
                ii += 1

        for kaisu in range(11):
            if kaisu == 0:
                rate = 1
            if kaisu == 1:
                rate = 0.9
            if kaisu == 2:
                rate = 0.8
            if kaisu == 3:
                rate = 0.7
            if kaisu == 4:
                rate = 0.6
            if kaisu == 5:
                rate = 0.5
            if kaisu == 6:
                rate = 0.4
            if kaisu == 7:
                rate = 0.3
            if kaisu == 8:
                rate = 0.2
            if kaisu == 9:
                rate = 0.1
            if kaisu == 10:
                rate = 0.0
            #今の気持ちから考える
            f = DATA.heart
            t = len(DATA.data["sentence"]) - 1
            i = f
            ii = 0
            for sen in DATA.data["sentence"][f:t]:
                if i >= len(DATA.data["sentence"]) - 1:
                    break
                if Levenshtein.normalized_similarity(x, DATA.data["sentence"][i][0]) >= rate:
                    if i+1 >= len(DATA.data["sentence"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentence"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentence"]) and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentence) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentence"][i+1][1] != "!input" and DATA.data["sentence"][i+1][0] != "!bad" and DATA.data["sentence"][i+1][0] != "!good" and "!system" not in DATA.data["sentence"][i+1][1] and "!input-" not in DATA.data["sentence"][i+1][1]:
                            flag = True
                            for iiiii in range(3):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "!bad":
                                        flag = False
                                        break
                            if flag:
                                print("類似: {}, {}, {}".format(DATA.data["sentence"][i][0], i, rate))
                                print("返信: {}, {}".format(DATA.data["sentence"][i+1][0], i+1))
                                DATA.sa = ii
                                DATA.heart = i+1
                                DATA.heartLastSpeaker = DATA.data["sentence"][i+1][1]
                                DATA.rate = rate
                                return DATA.data["sentence"][i+1][0]
                        else:
                            pass
                    else:
                        DATA.heart = i
                        DATA.rate = rate
                        return None
                i += 1
                ii += 1
            #今の気持ちから考える
            f = 0
            t = DATA.heart-1
            i = f
            ii = 0
            for sen in DATA.data["sentence"][f:t]:
                if i >= len(DATA.data["sentence"]) - 1:
                    break
                if Levenshtein.normalized_similarity(x, DATA.data["sentence"][i][0]) >= rate:
                    if i+1 >= len(DATA.data["sentence"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentence"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentence"]) and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentence) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentence"][i+1][1] != "!input" and DATA.data["sentence"][i+1][0] != "!bad" and DATA.data["sentence"][i+1][0] != "!good" and "!system" not in DATA.data["sentence"][i+1][1] and "!input-" not in DATA.data["sentence"][i+1][1]:
                            flag = True
                            for iiiii in range(3):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "!bad":
                                        flag = False
                                        break
                            if flag:
                                print("類似: {}, {}, {}".format(DATA.data["sentence"][i][0], i, rate))
                                print("返信: {}, {}".format(DATA.data["sentence"][i+1][0], i+1))
                                DATA.sa = ii
                                DATA.heart = i+1
                                DATA.heartLastSpeaker = DATA.data["sentence"][i+1][1]
                                DATA.rate = rate
                                return DATA.data["sentence"][i+1][0]
                        else:
                            pass
                    else:
                        DATA.heart = i
                        DATA.rate = rate
                        return None
                i += 1
                ii += 1

    except:
        import traceback
        traceback.print_exc()
    return None


def lookingForNext(x, u, reply=True, force=False):
    #過去の発言をもとに考える
    try:
        x = x.replace(DATA.lastUser, "[I]")
        for myname in DATA.settings["mynames"].split("|"):
            x = x.replace(myname, "[YOU]")
        print("思考中: {}".format(x))

        for kaisu in range(4):
            if kaisu == 0:
                rate = 1
            if kaisu == 1:
                rate = 0.9
            if kaisu == 2:
                rate = 0.8
            if kaisu == 3:
                rate = 0.7
            #今の気持ちから考える
            f = DATA.heart
            t = len(DATA.data["sentence"]) - 1
            i = f
            ii = 0
            for sen in DATA.data["sentence"][f:t]:
                if i >= len(DATA.data["sentence"]) - 1:
                    break
                if Levenshtein.normalized_similarity(x, DATA.data["sentence"][i][0]) >= rate:
                    if i+1 >= len(DATA.data["sentence"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentence"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentence"]) and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentence) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentence"][i+1][1] == DATA.data["sentence"][i][1] and DATA.data["sentence"][i+1][1] != "!" and DATA.data["sentence"][i+1][1] != "!input" and DATA.data["sentence"][i+1][0] != "!bad" and DATA.data["sentence"][i+1][0] != "!good" and "!system" not in DATA.data["sentence"][i+1][1] and "!input-" not in DATA.data["sentence"][i+1][1]:
                            flag = False
                            for iiiii in range(3):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "!good":
                                        flag = True
                                        break
                            for iiiii in range(3):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "!bad":
                                        flag = False
                                        break
                            if flag:
                                print("類似: {}, {}, {}".format(DATA.data["sentence"][i][0], i, rate))
                                print("返信: {}, {}".format(DATA.data["sentence"][i+1][0], i+1))
                                DATA.sa = ii
                                DATA.heart = i+1
                                DATA.heartLastSpeaker = DATA.data["sentence"][i+1][1]
                                DATA.rate = rate
                                return DATA.data["sentence"][i+1][0]
                        else:
                            pass
                    else:
                        DATA.heart = i
                        DATA.rate = rate
                        return None
                i += 1
                ii += 1
            #今の気持ちから考える
            f = 0
            t = DATA.heart-1
            i = f
            ii = 0
            for sen in DATA.data["sentence"][f:t]:
                if i >= len(DATA.data["sentence"]) - 1:
                    break
                if Levenshtein.normalized_similarity(x, DATA.data["sentence"][i][0]) >= rate:
                    if i+1 >= len(DATA.data["sentence"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentence"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentence"]) and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentence) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentence"][i+1][1] == DATA.data["sentence"][i][1] and DATA.data["sentence"][i+1][1] != "!" and DATA.data["sentence"][i+1][1] != "!input" and DATA.data["sentence"][i+1][0] != "!bad" and DATA.data["sentence"][i+1][0] != "!good" and "!system" not in DATA.data["sentence"][i+1][1] and "!input-" not in DATA.data["sentence"][i+1][1]:
                            flag = False
                            for iiiii in range(3):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "!good":
                                        flag = True
                                        break
                            for iiiii in range(3):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "!bad":
                                        flag = False
                                        break
                            if flag:
                                print("類似: {}, {}, {}".format(DATA.data["sentence"][i][0], i, rate))
                                print("返信: {}, {}".format(DATA.data["sentence"][i+1][0], i+1))
                                DATA.sa = ii
                                DATA.heart = i+1
                                DATA.heartLastSpeaker = DATA.data["sentence"][i+1][1]
                                DATA.rate = rate
                                return DATA.data["sentence"][i+1][0]
                        else:
                            pass
                    else:
                        DATA.heart = i
                        DATA.rate = rate
                        return None
                i += 1
                ii += 1

        for kaisu in range(11):
            if kaisu == 0:
                rate = 1
            if kaisu == 1:
                rate = 0.9
            if kaisu == 2:
                rate = 0.8
            if kaisu == 3:
                rate = 0.7
            if kaisu == 4:
                rate = 0.6
            if kaisu == 5:
                rate = 0.5
            if kaisu == 6:
                rate = 0.4
            if kaisu == 7:
                rate = 0.3
            if kaisu == 8:
                rate = 0.2
            if kaisu == 9:
                rate = 0.1
            if kaisu == 10:
                rate = 0.0
            #今の気持ちから考える
            f = DATA.heart
            t = len(DATA.data["sentence"]) - 1
            i = f
            ii = 0
            for sen in DATA.data["sentence"][f:t]:
                if i >= len(DATA.data["sentence"]) - 1:
                    break
                if Levenshtein.normalized_similarity("{}: {}".format(x, u), "{}: {}".format(DATA.data["sentence"][i][0], DATA.data["sentence"][i][1])) >= rate:
                    if i+1 >= len(DATA.data["sentence"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentence"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentence"]) and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentence) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentence"][i+1][1] == DATA.data["sentence"][i][1] and DATA.data["sentence"][i+1][1] != "!input" and DATA.data["sentence"][i+1][0] != "!bad" and DATA.data["sentence"][i+1][0] != "!good" and "!system" not in DATA.data["sentence"][i+1][1] and "!input-" not in DATA.data["sentence"][i+1][1]:
                            flag = True
                            for iiiii in range(3):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "!bad":
                                        flag = False
                                        break
                            if flag:
                                print("類似: {}, {}, {}".format(DATA.data["sentence"][i][0], i, rate))
                                print("返信: {}, {}".format(DATA.data["sentence"][i+1][0], i+1))
                                DATA.sa = ii
                                DATA.heart = i+1
                                DATA.heartLastSpeaker = DATA.data["sentence"][i+1][1]
                                DATA.rate = rate
                                return DATA.data["sentence"][i+1][0]
                        else:
                            pass
                    else:
                        DATA.heart = i
                        DATA.rate = rate
                        return None
                i += 1
                ii += 1
            #今の気持ちから考える
            f = 0
            t = DATA.heart-1
            i = f
            ii = 0
            for sen in DATA.data["sentence"][f:t]:
                if i >= len(DATA.data["sentence"]) - 1:
                    break
                if Levenshtein.normalized_similarity("{}: {}".format(x, u), "{}: {}".format(DATA.data["sentence"][i][0], DATA.data["sentence"][i][1])) >= rate:
                    if i+1 >= len(DATA.data["sentence"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentence"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentence"]) and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentence) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentence"][i+1][1] == DATA.data["sentence"][i][1] and DATA.data["sentence"][i+1][1] != "!input" and DATA.data["sentence"][i+1][0] != "!bad" and DATA.data["sentence"][i+1][0] != "!good" and "!system" not in DATA.data["sentence"][i+1][1] and "!input-" not in DATA.data["sentence"][i+1][1]:
                            flag = True
                            for iiiii in range(3):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "!bad":
                                        flag = False
                                        break
                            if flag:
                                print("類似: {}, {}, {}".format(DATA.data["sentence"][i][0], i, rate))
                                print("返信: {}, {}".format(DATA.data["sentence"][i+1][0], i+1))
                                DATA.sa = ii
                                DATA.heart = i+1
                                DATA.heartLastSpeaker = DATA.data["sentence"][i+1][1]
                                DATA.rate = rate
                                return DATA.data["sentence"][i+1][0]
                        else:
                            pass
                    else:
                        DATA.heart = i
                        DATA.rate = rate
                        return None
                i += 1
                ii += 1

        for kaisu in range(11):
            if kaisu == 0:
                rate = 1
            if kaisu == 1:
                rate = 0.9
            if kaisu == 2:
                rate = 0.8
            if kaisu == 3:
                rate = 0.7
            if kaisu == 4:
                rate = 0.6
            if kaisu == 5:
                rate = 0.5
            if kaisu == 6:
                rate = 0.4
            if kaisu == 7:
                rate = 0.3
            if kaisu == 8:
                rate = 0.2
            if kaisu == 9:
                rate = 0.1
            if kaisu == 10:
                rate = 0.0
            #今の気持ちから考える
            f = DATA.heart
            t = len(DATA.data["sentence"]) - 1
            i = f
            ii = 0
            for sen in DATA.data["sentence"][f:t]:
                if i >= len(DATA.data["sentence"]) - 1:
                    break
                if Levenshtein.normalized_similarity(x, DATA.data["sentence"][i][0]) >= rate:
                    if i+1 >= len(DATA.data["sentence"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentence"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentence"]) and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentence) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentence"][i+1][1] != "!input" and DATA.data["sentence"][i+1][0] != "!bad" and DATA.data["sentence"][i+1][0] != "!good" and "!system" not in DATA.data["sentence"][i+1][1] and "!input-" not in DATA.data["sentence"][i+1][1]:
                            flag = True
                            for iiiii in range(3):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "!bad":
                                        flag = False
                                        break
                            if flag:
                                print("類似: {}, {}, {}".format(DATA.data["sentence"][i][0], i, rate))
                                print("返信: {}, {}".format(DATA.data["sentence"][i+1][0], i+1))
                                DATA.sa = ii
                                DATA.heart = i+1
                                DATA.heartLastSpeaker = DATA.data["sentence"][i+1][1]
                                DATA.rate = rate
                                return DATA.data["sentence"][i+1][0]
                        else:
                            pass
                    else:
                        DATA.heart = i
                        DATA.rate = rate
                        return None
                i += 1
                ii += 1
            #今の気持ちから考える
            f = 0
            t = DATA.heart-1
            i = f
            ii = 0
            for sen in DATA.data["sentence"][f:t]:
                if i >= len(DATA.data["sentence"]) - 1:
                    break
                if Levenshtein.normalized_similarity(x, DATA.data["sentence"][i][0]) >= rate:
                    if i+1 >= len(DATA.data["sentence"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentence"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentence"]) and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentence) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentence"][i+1][1] != "!input" and DATA.data["sentence"][i+1][0] != "!bad" and DATA.data["sentence"][i+1][0] != "!good" and "!system" not in DATA.data["sentence"][i+1][1] and "!input-" not in DATA.data["sentence"][i+1][1]:
                            flag = True
                            for iiiii in range(3):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "!bad":
                                        flag = False
                                        break
                            if flag:
                                print("類似: {}, {}, {}".format(DATA.data["sentence"][i][0], i, rate))
                                print("返信: {}, {}".format(DATA.data["sentence"][i+1][0], i+1))
                                DATA.sa = ii
                                DATA.heart = i+1
                                DATA.heartLastSpeaker = DATA.data["sentence"][i+1][1]
                                DATA.rate = rate
                                return DATA.data["sentence"][i+1][0]
                        else:
                            pass
                    else:
                        DATA.heart = i
                        DATA.rate = rate
                        return None
                i += 1
                ii += 1

    except:
        import traceback
        traceback.print_exc()
    return None