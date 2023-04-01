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
        print("思考中...")
        
        for kaisu in range(6):
            if kaisu == 0:
                rate = 1
            if kaisu == 1:
                rate = 0.9
            if kaisu == 2:
                rate = 0.8
            if kaisu == 3:
                rate = 0.7
            if kaisu == 4:
                rate = 0.65
            if kaisu == 5:
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
                    for iiiiii in range(3):
                        #print("類似: {}, {}".format(DATA.data["sentence"][i][0], i))
                        if i+iiiiii+1>= len(DATA.data["sentence"]):
                            break
                        if reply:
                            isMine = False
                            for myname in DATA.settings["mynames"].split("|"):
                                if DATA.data["sentence"][i+iiiiii+1][1] == myname:
                                    isMine = True
                            if i != len(DATA.data["sentence"]) and Levenshtein.normalized_similarity(DATA.data["sentence"][i+iiiiii+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+iiiiii+1][0], DATA.lastSentence) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+iiiiii+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentence"][i+iiiiii+1][1] != DATA.data["sentence"][i][1] and DATA.data["sentence"][i+iiiiii+1][1] != "!" and "!system" not in DATA.data["sentence"][i+iiiiii+1][1]:
                                print("返信: {}, {}".format(DATA.data["sentence"][i+iiiiii+1][0], i+iiiiii+1))
                                flag = True
                                for iiiii in range(4):
                                    if i+iiiiii+1+iiiii < len(DATA.data["sentence"]) - 1:
                                        if DATA.data["sentence"][i+iiiiii+1+iiiii][0] == "☓" or DATA.data["sentence"][i+iiiiii+1+iiiii][0] == "×" or DATA.data["sentence"][i+iiiiii+1+iiiii][0] == "❌":
                                            flag = False
                                            if iiiii == 0:
                                                return "×"
                                            break
                                if flag:
                                    DATA.sa = ii
                                    DATA.heart = i+iiiiii+1
                                    DATA.heartLastSpeaker = DATA.data["sentence"][i+iiiiii+1][1]
                                    DATA.rate = rate
                                    return DATA.data["sentence"][i+iiiiii+1][0]
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
                    for iiiiii in range(3):
                        #print("類似: {}, {}".format(DATA.data["sentence"][i][0], i))
                        if i+iiiiii+1>= len(DATA.data["sentence"]):
                            break
                        if reply:
                            isMine = False
                            for myname in DATA.settings["mynames"].split("|"):
                                if DATA.data["sentence"][i+iiiiii+1][1] == myname:
                                    isMine = True
                            if i != len(DATA.data["sentence"]) and Levenshtein.normalized_similarity(DATA.data["sentence"][i+iiiiii+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+iiiiii+1][0], DATA.lastSentence) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+iiiiii+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentence"][i+iiiiii+1][1] != DATA.data["sentence"][i][1] and DATA.data["sentence"][i+iiiiii+1][1] != "!" and "!system" not in DATA.data["sentence"][i+iiiiii+1][1]:
                                print("返信: {}, {}".format(DATA.data["sentence"][i+iiiiii+1][0], i+iiiiii+1))
                                flag = True
                                for iiiii in range(4):
                                    if i+iiiiii+1+iiiii < len(DATA.data["sentence"]) - 1:
                                        if DATA.data["sentence"][i+iiiiii+1+iiiii][0] == "☓" or DATA.data["sentence"][i+iiiiii+1+iiiii][0] == "×" or DATA.data["sentence"][i+iiiiii+1+iiiii][0] == "❌":
                                            flag = False
                                            if iiiii == 0:
                                                return "×"
                                            break
                                if flag:
                                    DATA.sa = ii
                                    DATA.heart = i+iiiiii+1
                                    DATA.heartLastSpeaker = DATA.data["sentence"][i+iiiiii+1][1]
                                    DATA.rate = rate
                                    return DATA.data["sentence"][i+iiiiii+1][0]
                            else:
                                pass
                        else:
                            DATA.heart = i
                            DATA.rate = rate
                            return
                i += 1
                ii += 1
        
        for kaisu in range(6):
            if kaisu == 0:
                rate = 1
            if kaisu == 1:
                rate = 0.9
            if kaisu == 2:
                rate = 0.8
            if kaisu == 3:
                rate = 0.7
            if kaisu == 4:
                rate = 0.65
            if kaisu == 5:
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
                    for iiiiii in range(3):
                        #print("類似: {}, {}".format(DATA.data["sentence"][i][0], i))
                        if i+iiiiii+1>= len(DATA.data["sentence"]):
                            break
                        if reply:
                            isMine = False
                            for myname in DATA.settings["mynames"].split("|"):
                                if DATA.data["sentence"][i+iiiiii+1][1] == myname:
                                    isMine = True
                            if i != len(DATA.data["sentence"]) and Levenshtein.normalized_similarity(DATA.data["sentence"][i+iiiiii+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+iiiiii+1][0], DATA.lastSentence) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+iiiiii+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentence"][i+iiiiii+1][1] != "!" and "!system" not in DATA.data["sentence"][i+iiiiii+1][1]:
                                print("返信: {}, {}".format(DATA.data["sentence"][i+iiiiii+1][0], i+iiiiii+1))
                                flag = True
                                for iiiii in range(4):
                                    if i+iiiiii+1+iiiii < len(DATA.data["sentence"]) - 1:
                                        if DATA.data["sentence"][i+iiiiii+1+iiiii][0] == "☓" or DATA.data["sentence"][i+iiiiii+1+iiiii][0] == "×" or DATA.data["sentence"][i+iiiiii+1+iiiii][0] == "❌":
                                            flag = False
                                            if iiiii == 0:
                                                return "×"
                                            break
                                if flag:
                                    DATA.sa = ii
                                    DATA.heart = i+iiiiii+1
                                    DATA.heartLastSpeaker = DATA.data["sentence"][i+iiiiii+1][1]
                                    DATA.rate = rate
                                    return DATA.data["sentence"][i+iiiiii+1][0]
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
                    for iiiiii in range(3):
                        #print("類似: {}, {}".format(DATA.data["sentence"][i][0], i))
                        if i+iiiiii+1>= len(DATA.data["sentence"]):
                            break
                        if reply:
                            isMine = False
                            for myname in DATA.settings["mynames"].split("|"):
                                if DATA.data["sentence"][i+iiiiii+1][1] == myname:
                                    isMine = True
                            if i != len(DATA.data["sentence"]) and Levenshtein.normalized_similarity(DATA.data["sentence"][i+iiiiii+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+iiiiii+1][0], DATA.lastSentence) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+iiiiii+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentence"][i+iiiiii+1][1] != "!" and "!system" not in DATA.data["sentence"][i+iiiiii+1][1]:
                                print("返信: {}, {}".format(DATA.data["sentence"][i+iiiiii+1][0], i+iiiiii+1))
                                flag = True
                                for iiiii in range(4):
                                    if i+iiiiii+1+iiiii < len(DATA.data["sentence"]) - 1:
                                        if DATA.data["sentence"][i+iiiiii+1+iiiii][0] == "☓" or DATA.data["sentence"][i+iiiiii+1+iiiii][0] == "×" or DATA.data["sentence"][i+iiiiii+1+iiiii][0] == "❌":
                                            flag = False
                                            if iiiii == 0:
                                                return "×"
                                            break
                                if flag:
                                    DATA.sa = ii
                                    DATA.heart = i+iiiiii+1
                                    DATA.heartLastSpeaker = DATA.data["sentence"][i+iiiiii+1][1]
                                    DATA.rate = rate
                                    return DATA.data["sentence"][i+iiiiii+1][0]
                            else:
                                pass
                        else:
                            DATA.heart = i
                            DATA.rate = rate
                            return
                i += 1
                ii += 1

        for kaisu in range(6):
            if kaisu == 0:
                rate = 1
            if kaisu == 1:
                rate = 0.9
            if kaisu == 2:
                rate = 0.8
            if kaisu == 3:
                rate = 0.7
            if kaisu == 4:
                rate = 0.65
            if kaisu == 5:
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
                    for iiiiii in range(3):
                        #print("類似: {}, {}".format(DATA.data["sentence"][i][0], i))
                        if i+iiiiii+1>= len(DATA.data["sentence"]):
                            break
                        if reply:
                            isMine = False
                            for myname in DATA.settings["mynames"].split("|"):
                                if DATA.data["sentence"][i+iiiiii+1][1] == myname:
                                    isMine = True
                            if i != len(DATA.data["sentence"]) and Levenshtein.normalized_similarity(DATA.data["sentence"][i+iiiiii+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+iiiiii+1][0], DATA.lastSentence) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+iiiiii+1][0], DATA.lastSentenceHeart) < 0.75 and "!system" not in DATA.data["sentence"][i+iiiiii+1][1]:
                                print("返信: {}, {}".format(DATA.data["sentence"][i+iiiiii+1][0], i+iiiiii+1))
                                flag = True
                                for iiiii in range(4):
                                    if i+iiiiii+1+iiiii < len(DATA.data["sentence"]) - 1:
                                        if DATA.data["sentence"][i+iiiiii+1+iiiii][0] == "☓" or DATA.data["sentence"][i+iiiiii+1+iiiii][0] == "×" or DATA.data["sentence"][i+iiiiii+1+iiiii][0] == "❌":
                                            flag = False
                                            if iiiii == 0:
                                                return "×"
                                            break
                                if flag:
                                    DATA.sa = ii
                                    DATA.heart = i+iiiiii+1
                                    DATA.heartLastSpeaker = DATA.data["sentence"][i+iiiiii+1][1]
                                    DATA.rate = rate
                                    return DATA.data["sentence"][i+iiiiii+1][0]
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
                    for iiiiii in range(3):
                        #print("類似: {}, {}".format(DATA.data["sentence"][i][0], i))
                        if i+iiiiii+1>= len(DATA.data["sentence"]):
                            break
                        if reply:
                            isMine = False
                            for myname in DATA.settings["mynames"].split("|"):
                                if DATA.data["sentence"][i+iiiiii+1][1] == myname:
                                    isMine = True
                            if i != len(DATA.data["sentence"]) and Levenshtein.normalized_similarity(DATA.data["sentence"][i+iiiiii+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+iiiiii+1][0], DATA.lastSentence) < 0.75 and Levenshtein.normalized_similarity(DATA.data["sentence"][i+iiiiii+1][0], DATA.lastSentenceHeart) < 0.75 and "!system" not in DATA.data["sentence"][i+iiiiii+1][1]:
                                print("返信: {}, {}".format(DATA.data["sentence"][i+iiiiii+1][0], i+iiiiii+1))
                                flag = True
                                for iiiii in range(4):
                                    if i+iiiiii+1+iiiii < len(DATA.data["sentence"]) - 1:
                                        if DATA.data["sentence"][i+iiiiii+1+iiiii][0] == "☓" or DATA.data["sentence"][i+iiiiii+1+iiiii][0] == "×" or DATA.data["sentence"][i+iiiiii+1+iiiii][0] == "❌":
                                            flag = False
                                            if iiiii == 0:
                                                return "×"
                                            break
                                if flag:
                                    DATA.sa = ii
                                    DATA.heart = i+iiiiii+1
                                    DATA.heartLastSpeaker = DATA.data["sentence"][i+iiiiii+1][1]
                                    DATA.rate = rate
                                    return DATA.data["sentence"][i+iiiiii+1][0]
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