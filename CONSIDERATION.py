import re
import json
import random
import time
import DATA
from rapidfuzz.distance import Levenshtein
import INTELLIGENCE

def looking(x, u, reply=True, force=False):
    #過去の発言をもとに考える
    try:
        #print("思考中: {}".format(x))

        for kaisu in range(5):
            if kaisu == 0:
                rate = 1
            if kaisu == 1:
                rate = 0.5
            if kaisu == 2:
                rate = 0.5
            if kaisu == 3:
                rate = 0.25
            if kaisu == 4:
                rate = 0
            #今の気持ちから考える
            f = DATA.heart+1
            t = len(DATA.data["sentence"]) - 1
            i = f
            ii = 0
            for sen in DATA.data["sentence"][f:t]:
                if i >= len(DATA.data["sentence"]) - 1:
                    break
                into = x
                if Levenshtein.normalized_similarity(into, DATA.data["sentence"][i][0]) >= rate:
                    if i+1>= len(DATA.data["sentence"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentence"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentence"]) and DATA.data["sentence"][i+1][1] != "!" and DATA.data["sentence"][i+1][1] != "!input" and "!system" not in DATA.data["sentence"][i+1][1]:
                            #print("類似: {}, {}, {}".format(DATA.data["sentence"][i][0], i, rate))
                            #print("返信: {}, {}".format(DATA.data["sentence"][i+1][0], i+1))
                            flag = True
                            for iiiii in range(4):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "☓" or DATA.data["sentence"][i+1+iiiii][0] == "×" or DATA.data["sentence"][i+1+iiiii][0] == "❌":
                                        flag = False
                                        if iiiii == 0:
                                            return "×"
                                        break
                            if flag:
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
                        return
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
                into = x
                if Levenshtein.normalized_similarity(into, DATA.data["sentence"][i][0]) >= rate:
                    if i+1>= len(DATA.data["sentence"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentence"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentence"]) and DATA.data["sentence"][i+1][1] != "!" and DATA.data["sentence"][i+1][1] != "!input" and "!system" not in DATA.data["sentence"][i+1][1]:
                            #print("類似: {}, {}, {}".format(DATA.data["sentence"][i][0], i, rate))
                            #print("返信: {}, {}".format(DATA.data["sentence"][i+1][0], i+1))
                            flag = True
                            for iiiii in range(4):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "☓" or DATA.data["sentence"][i+1+iiiii][0] == "×" or DATA.data["sentence"][i+1+iiiii][0] == "❌":
                                        flag = False
                                        if iiiii == 0:
                                            return "×"
                                        break
                            if flag:
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
                        return
                i += 1
                ii += 1

        for kaisu in range(5):
            if kaisu == 0:
                rate = 1
            if kaisu == 1:
                rate = 0.75
            if kaisu == 2:
                rate = 0.5
            if kaisu == 3:
                rate = 0.25
            if kaisu == 4:
                rate = 0
            #今の気持ちから考える
            f = DATA.heart+1
            t = len(DATA.data["sentence"]) - 1
            i = f
            ii = 0
            for sen in DATA.data["sentence"][f:t]:
                if i >= len(DATA.data["sentence"]) - 1:
                    break
                into = "{}: {}".format(u, x)
                if Levenshtein.normalized_similarity(into, "{}: {}".format(DATA.data["sentence"][i][1], DATA.data["sentence"][i][0])) >= rate:
                    if i+1>= len(DATA.data["sentence"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentence"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentence"]) and DATA.data["sentence"][i+1][1] != "!" and DATA.data["sentence"][i+1][1] != "!input" and "!system" not in DATA.data["sentence"][i+1][1]:
                            #print("類似: {}, {}, {}".format(DATA.data["sentence"][i][0], i, rate))
                            #print("返信: {}, {}".format(DATA.data["sentence"][i+1][0], i+1))
                            flag = True
                            for iiiii in range(4):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "☓" or DATA.data["sentence"][i+1+iiiii][0] == "×" or DATA.data["sentence"][i+1+iiiii][0] == "❌":
                                        flag = False
                                        if iiiii == 0:
                                            return "×"
                                        break
                            if flag:
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
                        return
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
                into = "{}: {}".format(u, x)
                if Levenshtein.normalized_similarity(into, "{}: {}".format(DATA.data["sentence"][i][1], DATA.data["sentence"][i][0])) >= rate:
                    if i+1>= len(DATA.data["sentence"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentence"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentence"]) and DATA.data["sentence"][i+1][1] != "!" and DATA.data["sentence"][i+1][1] != "!input" and "!system" not in DATA.data["sentence"][i+1][1]:
                            #print("類似: {}, {}, {}".format(DATA.data["sentence"][i][0], i, rate))
                            #print("返信: {}, {}".format(DATA.data["sentence"][i+1][0], i+1))
                            flag = True
                            for iiiii in range(4):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "☓" or DATA.data["sentence"][i+1+iiiii][0] == "×" or DATA.data["sentence"][i+1+iiiii][0] == "❌":
                                        flag = False
                                        if iiiii == 0:
                                            return "×"
                                        break
                            if flag:
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
                        return
                i += 1
                ii += 1

        for kaisu in range(5):
            if kaisu == 0:
                rate = 1
            if kaisu == 1:
                rate = 0.75
            if kaisu == 2:
                rate = 0.5
            if kaisu == 3:
                rate = 0.25
            if kaisu == 4:
                rate = 0
            #今の気持ちから考える
            f = DATA.heart+1
            t = len(DATA.data["sentence"]) - 1
            i = f
            ii = 0
            for sen in DATA.data["sentence"][f:t]:
                if i >= len(DATA.data["sentence"]) - 1:
                    break
                into = "{}: {}".format(u, x)
                if Levenshtein.normalized_similarity(into, "{}: {}".format(DATA.data["sentence"][i][1], DATA.data["sentence"][i][0])) >= rate:
                    if i+1>= len(DATA.data["sentence"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentence"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentence"]) and DATA.data["sentence"][i+1][1] != "!" and DATA.data["sentence"][i+1][1] != "!input" and "!system" not in DATA.data["sentence"][i+1][1]:
                            #print("類似: {}, {}, {}".format(DATA.data["sentence"][i][0], i, rate))
                            #print("返信: {}, {}".format(DATA.data["sentence"][i+1][0], i+1))
                            flag = True
                            for iiiii in range(4):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "☓" or DATA.data["sentence"][i+1+iiiii][0] == "×" or DATA.data["sentence"][i+1+iiiii][0] == "❌":
                                        flag = False
                                        if iiiii == 0:
                                            return "×"
                                        break
                            if flag:
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
                        return
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
                into = "{}: {}".format(u, x)
                if Levenshtein.normalized_similarity(into, "{}: {}".format(DATA.data["sentence"][i][1], DATA.data["sentence"][i][0])) >= rate:
                    if i+1>= len(DATA.data["sentence"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentence"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentence"]) and DATA.data["sentence"][i+1][1] != "!" and DATA.data["sentence"][i+1][1] != "!input" and "!system" not in DATA.data["sentence"][i+1][1]:
                            #print("類似: {}, {}, {}".format(DATA.data["sentence"][i][0], i, rate))
                            #print("返信: {}, {}".format(DATA.data["sentence"][i+1][0], i+1))
                            flag = True
                            for iiiii in range(4):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "☓" or DATA.data["sentence"][i+1+iiiii][0] == "×" or DATA.data["sentence"][i+1+iiiii][0] == "❌":
                                        flag = False
                                        if iiiii == 0:
                                            return "×"
                                        break
                            if flag:
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
                        return
                i += 1
                ii += 1

        for kaisu in range(5):
            if kaisu == 0:
                rate = 1
            if kaisu == 1:
                rate = 0.75
            if kaisu == 2:
                rate = 0.5
            if kaisu == 3:
                rate = 0.25
            if kaisu == 4:
                rate = 0
            #今の気持ちから考える
            f = DATA.heart+1
            t = len(DATA.data["sentence"]) - 1
            i = f
            ii = 0
            for sen in DATA.data["sentence"][f:t]:
                if i >= len(DATA.data["sentence"]) - 1:
                    break
                into = "{}: {}".format(u, x)
                if Levenshtein.normalized_similarity(into, "{}: {}".format(DATA.data["sentence"][i][1], DATA.data["sentence"][i][0])) >= rate:
                    if i+1>= len(DATA.data["sentence"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentence"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentence"]) and DATA.data["sentence"][i+1][1] != "!input" and "!system" not in DATA.data["sentence"][i+1][1]:
                            #print("類似: {}, {}, {}".format(DATA.data["sentence"][i][0], i, rate))
                            #print("返信: {}, {}".format(DATA.data["sentence"][i+1][0], i+1))
                            flag = True
                            for iiiii in range(4):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "☓" or DATA.data["sentence"][i+1+iiiii][0] == "×" or DATA.data["sentence"][i+1+iiiii][0] == "❌":
                                        flag = False
                                        if iiiii == 0:
                                            return "×"
                                        break
                            if flag:
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
                        return
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
                into = "{}: {}".format(u, x)
                if Levenshtein.normalized_similarity(into, "{}: {}".format(DATA.data["sentence"][i][1], DATA.data["sentence"][i][0])) >= rate:
                    if i+1>= len(DATA.data["sentence"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentence"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentence"]) and DATA.data["sentence"][i+1][1] != "!input" and "!system" not in DATA.data["sentence"][i+1][1]:
                            #print("類似: {}, {}, {}".format(DATA.data["sentence"][i][0], i, rate))
                            #print("返信: {}, {}".format(DATA.data["sentence"][i+1][0], i+1))
                            flag = True
                            for iiiii in range(4):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "☓" or DATA.data["sentence"][i+1+iiiii][0] == "×" or DATA.data["sentence"][i+1+iiiii][0] == "❌":
                                        flag = False
                                        if iiiii == 0:
                                            return "×"
                                        break
                            if flag:
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
                        return
                i += 1
                ii += 1

    except:
        import traceback
        traceback.print_exc()
    return None