import re
import json
import random
import time

import DATA
import Levenshtein




def looking(x, u, reply=True, force=False):
    #過去の発言をもとに考える
    try:
        print("思考中...")


        for kaisu in range(4):
            if kaisu == 0:
                rate = 1
            if kaisu == 1:
                rate = 0.9
            if kaisu == 2:
                rate = 0.8
            if kaisu == 3:
                rate = 0.75







            #今の気持ちから考える
            f = DATA.heart+1

            t = len(DATA.data["sentence"]) - 1
            
            i = f
            ii = 0


            for sen in DATA.data["sentence"][f:t]:
                if i >= len(DATA.data["sentence"]) - 1:
                    break
                into = "{}: ".format(u)+x
                if Levenshtein.ratio(into,  "{}: ".format(DATA.data["sentence"][i][1])+DATA.data["sentence"][i][0]) >= rate:
                    print("類似: {}, {}".format(DATA.data["sentence"][i][0], i))
                    if i+1>= len(DATA.data["sentence"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentence"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentence"]) and Levenshtein.ratio(DATA.data["sentence"][i+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.ratio(DATA.data["sentence"][i+1][0], DATA.lastSentence) < 0.75 and Levenshtein.ratio(DATA.data["sentence"][i+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentence"][i][1] != DATA.data["sentence"][i+1][1] and DATA.data["sentence"][i+1][1] != "!" and "!system" not in DATA.data["sentence"][i+1][1]:
                            print("返信: {}, {}".format(DATA.data["sentence"][i+1][0], i+1))
                            flag = True
                            iii = 100
                            for iiiii in range(4):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "×" or DATA.data["sentence"][i+1+iiiii][0] == "❌":
                                        flag = False
                                        iii = iiiii
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
                into = "{}: ".format(u)+x
                if Levenshtein.ratio(into,  "{}: ".format(DATA.data["sentence"][i][1])+DATA.data["sentence"][i][0]) >= rate:
                    print("類似: {}, {}".format(DATA.data["sentence"][i][0], i))
                    if i+1>= len(DATA.data["sentence"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentence"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentence"]) and Levenshtein.ratio(DATA.data["sentence"][i+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.ratio(DATA.data["sentence"][i+1][0], DATA.lastSentence) < 0.75 and Levenshtein.ratio(DATA.data["sentence"][i+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentence"][i][1] != DATA.data["sentence"][i+1][1] and DATA.data["sentence"][i+1][1] != "!" and "!system" not in DATA.data["sentence"][i+1][1]:
                            print("返信: {}, {}".format(DATA.data["sentence"][i+1][0], i+1))
                            flag = True
                            iii = 100
                            for iiiii in range(4):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "×" or DATA.data["sentence"][i+1+iiiii][0] == "❌":
                                        flag = False
                                        iii = iiiii
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

















        for kaisu in range(4):
            if kaisu == 0:
                rate = 1
            if kaisu == 1:
                rate = 0.9
            if kaisu == 2:
                rate = 0.8
            if kaisu == 3:
                rate = 0.75







            #今の気持ちから考える
            f = DATA.heart+1

            t = len(DATA.data["sentence"]) - 1
            
            i = f
            ii = 0


            for sen in DATA.data["sentence"][f:t]:
                if i >= len(DATA.data["sentence"]) - 1:
                    break
                into = "{}: ".format(u)+x
                if Levenshtein.ratio(into,  "{}: ".format(DATA.data["sentence"][i][1])+DATA.data["sentence"][i][0]) >= rate:
                    print("類似: {}, {}".format(DATA.data["sentence"][i][0], i))
                    if i+1>= len(DATA.data["sentence"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentence"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentence"]) and Levenshtein.ratio(DATA.data["sentence"][i+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.ratio(DATA.data["sentence"][i+1][0], DATA.lastSentence) < 0.75 and Levenshtein.ratio(DATA.data["sentence"][i+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentence"][i+1][1] != "!" and "!system" not in DATA.data["sentence"][i+1][1]:
                            print("返信: {}, {}".format(DATA.data["sentence"][i+1][0], i+1))
                            flag = True
                            iii = 100
                            for iiiii in range(4):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "×" or DATA.data["sentence"][i+1+iiiii][0] == "❌":
                                        flag = False
                                        iii = iiiii
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
                into = "{}: ".format(u)+x
                if Levenshtein.ratio(into,  "{}: ".format(DATA.data["sentence"][i][1])+DATA.data["sentence"][i][0]) >= rate:
                    print("類似: {}, {}".format(DATA.data["sentence"][i][0], i))
                    if i+1>= len(DATA.data["sentence"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentence"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentence"]) and Levenshtein.ratio(DATA.data["sentence"][i+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.ratio(DATA.data["sentence"][i+1][0], DATA.lastSentence) < 0.75 and Levenshtein.ratio(DATA.data["sentence"][i+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentence"][i+1][1] != "!" and "!system" not in DATA.data["sentence"][i+1][1]:
                            print("返信: {}, {}".format(DATA.data["sentence"][i+1][0], i+1))
                            flag = True
                            iii = 100
                            for iiiii in range(4):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "×" or DATA.data["sentence"][i+1+iiiii][0] == "❌":
                                        flag = False
                                        iii = iiiii
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





















        for kaisu in range(1):
            if kaisu == 0:
                rate = 0


            #今の気持ちから考える
            f = DATA.heart+1

            t = len(DATA.data["sentence"]) - 1
            
            i = f
            ii = 0

            for sen in DATA.data["sentence"][f:t]:
                if i >= len(DATA.data["sentence"]) - 1:
                    break
                into = "{}: ".format(u)+x
                if Levenshtein.ratio(into,  "{}: ".format(DATA.data["sentence"][i][1])+DATA.data["sentence"][i][0]) >= rate:
                    print("類似: {}, {}".format(DATA.data["sentence"][i][0], i))
                    if i+1>= len(DATA.data["sentence"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentence"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentence"]) and Levenshtein.ratio(DATA.data["sentence"][i+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.ratio(DATA.data["sentence"][i+1][0], DATA.lastSentence) < 0.75 and Levenshtein.ratio(DATA.data["sentence"][i+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentence"][i][1] != DATA.data["sentence"][i+1][1] and DATA.data["sentence"][i+1][1] != "!" and "!system" not in DATA.data["sentence"][i+1][1]:
                            print("返信: {}, {}".format(DATA.data["sentence"][i+1][0], i+1))
                            flag = True
                            iii = 100
                            for iiiii in range(4):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "×" or DATA.data["sentence"][i+1+iiiii][0] == "❌":
                                        flag = False
                                        iii = iiiii
                                        break
                            if flag:
                                DATA.sa = ii
                                DATA.heart = i+1
                                DATA.heartLastSpeaker = DATA.data["sentence"][i+1][1]
                                DATA.rate = rate
                                DATA.times = kaisu
                                return DATA.data["sentence"][i+1][0]
                        else:
                            pass
                    else:
                        DATA.heart = i
                        DATA.rate = rate
                        return
                i += 1
                ii += 1




            #今の気持ちから少し離れる
            f = 0
            
            t = DATA.heart-1

            i = f
            ii = 0
            

            for sen in DATA.data["sentence"][f:t]:
                if i >= len(DATA.data["sentence"]) - 1:
                    break
                into = "{}: ".format(u)+x
                if Levenshtein.ratio(into,  "{}: ".format(DATA.data["sentence"][i][1])+DATA.data["sentence"][i][0]) >= rate:
                    print("類似: {}, {}".format(DATA.data["sentence"][i][0], i))
                    if i+1>= len(DATA.data["sentence"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentence"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentence"]) and Levenshtein.ratio(DATA.data["sentence"][i+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.ratio(DATA.data["sentence"][i+1][0], DATA.lastSentence) < 0.75 and Levenshtein.ratio(DATA.data["sentence"][i+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentence"][i][1] != DATA.data["sentence"][i+1][1] and DATA.data["sentence"][i+1][1] != "!" and "!system" not in DATA.data["sentence"][i+1][1]:
                            print("返信: {}, {}".format(DATA.data["sentence"][i+1][0], i+1))
                            flag = True
                            iii = 100
                            for iiiii in range(4):
                                if i+1+iiiii < len(DATA.data["sentence"]) - 1:
                                    if DATA.data["sentence"][i+1+iiiii][0] == "×" or DATA.data["sentence"][i+1+iiiii][0] == "❌":
                                        flag = False
                                        iii = iiiii
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




