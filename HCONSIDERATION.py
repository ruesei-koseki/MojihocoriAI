import re
import json
import random
import time

import DATA
import Levenshtein




def looking(x, u, reply=True, force=False):
    #過去の発言をもとに考える
    try:
        print("人格思考中...")


















        for kaisu in range(5):
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






            #今の気持ちから考える
            f = DATA.Hheart+1

            t = len(DATA.data["sentenceHumanity"]) - 1
            
            i = f
            ii = 0


            for sen in DATA.data["sentenceHumanity"][f:t]:
                if i >= len(DATA.data["sentenceHumanity"]) - 1:
                    break
                into = "{}: ".format(u)+x
                if Levenshtein.ratio(into,  "{}: ".format(DATA.data["sentenceHumanity"][i][1])+DATA.data["sentenceHumanity"][i][0]) >= rate:
                    #print("類似: {}, {}".format(DATA.data["sentenceHumanity"][i][0], i))
                    if i+1>= len(DATA.data["sentenceHumanity"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentenceHumanity"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentenceHumanity"]) and Levenshtein.ratio(DATA.data["sentenceHumanity"][i+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.ratio(DATA.data["sentenceHumanity"][i+1][0], DATA.lastSentence) < 0.75 and Levenshtein.ratio(DATA.data["sentenceHumanity"][i+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentenceHumanity"][i][1] != DATA.data["sentenceHumanity"][i+1][1] and DATA.data["sentenceHumanity"][i+1][1] == "!" and "!system" not in DATA.data["sentence"][i+1][1]:
                            #print("返信: {}, {}".format(DATA.data["sentenceHumanity"][i+1][0], i+1))
                            flag = True
                            for iiiii in range(7):
                                if i+1+iiiii < len(DATA.data["sentenceHumanity"]) - 1:
                                    if DATA.data["sentenceHumanity"][i+1+iiiii][0] == "×":
                                        flag = False
                                        break
                            if flag:
                                DATA.Hsa = ii
                                DATA.Hheart = i+1
                                DATA.HheartLastSpeaker = DATA.data["sentenceHumanity"][i+1][1]
                                DATA.Hrate = rate
                                DATA.mode = 1
                                return DATA.data["sentenceHumanity"][i+1][0]
                        else:
                            pass
                    else:
                        DATA.Hheart = i
                        return
                i += 1
                ii += 1







            #今の気持ちから考える
            f = 0
            
            t = DATA.Hheart-1

            i = f
            ii = 0

            for sen in DATA.data["sentenceHumanity"][f:t]:
                if i >= len(DATA.data["sentenceHumanity"]) - 1:
                    break
                into = "{}: ".format(u)+x
                if Levenshtein.ratio(into,  "{}: ".format(DATA.data["sentenceHumanity"][i][1])+DATA.data["sentenceHumanity"][i][0]) >= rate:
                    #print("類似: {}, {}".format(DATA.data["sentenceHumanity"][i][0], i))
                    if i+1>= len(DATA.data["sentenceHumanity"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentenceHumanity"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentenceHumanity"]) and Levenshtein.ratio(DATA.data["sentenceHumanity"][i+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.ratio(DATA.data["sentenceHumanity"][i+1][0], DATA.lastSentence) < 0.75 and Levenshtein.ratio(DATA.data["sentenceHumanity"][i+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentenceHumanity"][i][1] != DATA.data["sentenceHumanity"][i+1][1] and DATA.data["sentenceHumanity"][i+1][1] == "!" and "!system" not in DATA.data["sentence"][i+1][1]:
                            #print("返信: {}, {}".format(DATA.data["sentenceHumanity"][i+1][0], i+1))
                            flag = True
                            for iiiii in range(7):
                                if i+1+iiiii < len(DATA.data["sentenceHumanity"]) - 1:
                                    if DATA.data["sentenceHumanity"][i+1+iiiii][0] == "×":
                                        flag = False
                                        break
                            if flag:
                                DATA.Hsa = ii
                                DATA.Hheart = i+1
                                DATA.HheartLastSpeaker = DATA.data["sentenceHumanity"][i+1][1]
                                DATA.Hrate = rate
                                DATA.mode = 1
                                return DATA.data["sentenceHumanity"][i+1][0]
                        else:
                            pass
                    else:
                        DATA.Hheart = i
                        return
                i += 1
                ii += 1

















        for kaisu in range(5):
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







            #今の気持ちから考える
            f = DATA.Hheart+1

            t = len(DATA.data["sentenceHumanity"]) - 1
            
            i = f
            ii = 0


            for sen in DATA.data["sentenceHumanity"][f:t]:
                if i >= len(DATA.data["sentenceHumanity"]) - 1:
                    break
                into = "{}: ".format(u)+x
                if Levenshtein.ratio(into,  "{}: ".format(DATA.data["sentenceHumanity"][i][1])+DATA.data["sentenceHumanity"][i][0]) >= rate:
                    #print("類似: {}, {}".format(DATA.data["sentenceHumanity"][i][0], i))
                    if i+1>= len(DATA.data["sentenceHumanity"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentenceHumanity"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentenceHumanity"]) and Levenshtein.ratio(DATA.data["sentenceHumanity"][i+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.ratio(DATA.data["sentenceHumanity"][i+1][0], DATA.lastSentence) < 0.75 and Levenshtein.ratio(DATA.data["sentenceHumanity"][i+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentenceHumanity"][i+1][1] == "!" and "!system" not in DATA.data["sentence"][i+1][1]:
                            #print("返信: {}, {}".format(DATA.data["sentenceHumanity"][i+1][0], i+1))
                            flag = True
                            for iiiii in range(7):
                                if i+1+iiiii < len(DATA.data["sentenceHumanity"]) - 1:
                                    if DATA.data["sentenceHumanity"][i+1+iiiii][0] == "×":
                                        flag = False
                                        break
                            if flag:
                                DATA.Hsa = ii
                                DATA.Hheart = i+1
                                DATA.HheartLastSpeaker = DATA.data["sentenceHumanity"][i+1][1]
                                DATA.Hrate = rate
                                DATA.mode = 1
                                return DATA.data["sentenceHumanity"][i+1][0]
                        else:
                            pass
                    else:
                        DATA.Hheart = i
                        return
                i += 1
                ii += 1







            #今の気持ちから考える
            f = 0
            
            t = DATA.Hheart-1

            i = f
            ii = 0

            for sen in DATA.data["sentenceHumanity"][f:t]:
                if i >= len(DATA.data["sentenceHumanity"]) - 1:
                    break
                into = "{}: ".format(u)+x
                if Levenshtein.ratio(into,  "{}: ".format(DATA.data["sentenceHumanity"][i][1])+DATA.data["sentenceHumanity"][i][0]) >= rate:
                    #print("類似: {}, {}".format(DATA.data["sentenceHumanity"][i][0], i))
                    if i+1>= len(DATA.data["sentenceHumanity"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentenceHumanity"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentenceHumanity"]) and Levenshtein.ratio(DATA.data["sentenceHumanity"][i+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.ratio(DATA.data["sentenceHumanity"][i+1][0], DATA.lastSentence) < 0.75 and Levenshtein.ratio(DATA.data["sentenceHumanity"][i+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentenceHumanity"][i+1][1] == "!" and "!system" not in DATA.data["sentence"][i+1][1]:
                            #print("返信: {}, {}".format(DATA.data["sentenceHumanity"][i+1][0], i+1))
                            flag = True
                            for iiiii in range(7):
                                if i+1+iiiii < len(DATA.data["sentenceHumanity"]) - 1:
                                    if DATA.data["sentenceHumanity"][i+1+iiiii][0] == "×":
                                        flag = False
                                        break
                            if flag:
                                DATA.Hsa = ii
                                DATA.Hheart = i+1
                                DATA.HheartLastSpeaker = DATA.data["sentenceHumanity"][i+1][1]
                                DATA.Hrate = rate
                                DATA.mode = 1
                                return DATA.data["sentenceHumanity"][i+1][0]
                        else:
                            pass
                    else:
                        DATA.Hheart = i
                        return
                i += 1
                ii += 1





















        for kaisu in range(1):
            if kaisu == 0:
                rate = 0


            #今の気持ちから考える
            f = DATA.Hheart+1

            t = len(DATA.data["sentenceHumanity"]) - 1
            
            i = f
            ii = 0

            for sen in DATA.data["sentenceHumanity"][f:t]:
                if i >= len(DATA.data["sentenceHumanity"]) - 1:
                    break
                into = "{}: ".format(u)+x
                if Levenshtein.ratio(into,  "{}: ".format(DATA.data["sentenceHumanity"][i][1])+DATA.data["sentenceHumanity"][i][0]) >= rate:
                    #print("類似: {}, {}".format(DATA.data["sentenceHumanity"][i][0], i))
                    if i+1>= len(DATA.data["sentenceHumanity"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentenceHumanity"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentenceHumanity"]) and Levenshtein.ratio(DATA.data["sentenceHumanity"][i+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.ratio(DATA.data["sentenceHumanity"][i+1][0], DATA.lastSentence) < 0.75 and Levenshtein.ratio(DATA.data["sentenceHumanity"][i+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentenceHumanity"][i][1] != DATA.data["sentenceHumanity"][i+1][1] and DATA.data["sentenceHumanity"][i+1][1] == "!" and "!system" not in DATA.data["sentence"][i+1][1]:
                            #print("返信: {}, {}".format(DATA.data["sentenceHumanity"][i+1][0], i+1))
                            flag = True
                            for iiiii in range(7):
                                if i+1+iiiii < len(DATA.data["sentenceHumanity"]) - 1:
                                    if DATA.data["sentenceHumanity"][i+1+iiiii][0] == "×":
                                        flag = False
                                        break
                            if flag:
                                DATA.Hsa = ii
                                DATA.Hheart = i+1
                                DATA.HheartLastSpeaker = DATA.data["sentenceHumanity"][i+1][1]
                                DATA.Hrate = rate
                                DATA.Htimes = kaisu
                                DATA.mode = 1
                                return DATA.data["sentenceHumanity"][i+1][0]
                        else:
                            pass
                    else:
                        DATA.Hheart = i
                        return
                i += 1
                ii += 1




            #今の気持ちから少し離れる
            f = 0
            
            t = DATA.Hheart-1

            i = f
            ii = 0
            

            for sen in DATA.data["sentenceHumanity"][f:t]:
                if i >= len(DATA.data["sentenceHumanity"]) - 1:
                    break
                into = "{}: ".format(u)+x
                if Levenshtein.ratio(into,  "{}: ".format(DATA.data["sentenceHumanity"][i][1])+DATA.data["sentenceHumanity"][i][0]) >= rate:
                    #print("類似: {}, {}".format(DATA.data["sentenceHumanity"][i][0], i))
                    if i+1>= len(DATA.data["sentenceHumanity"]):
                        break
                    if reply:
                        isMine = False
                        for myname in DATA.settings["mynames"].split("|"):
                            if DATA.data["sentenceHumanity"][i+1][1] == myname:
                                isMine = True
                        if i != len(DATA.data["sentenceHumanity"]) and Levenshtein.ratio(DATA.data["sentenceHumanity"][i+1][0], DATA.lastSentenceInput) < 0.75 and Levenshtein.ratio(DATA.data["sentenceHumanity"][i+1][0], DATA.lastSentence) < 0.75 and Levenshtein.ratio(DATA.data["sentenceHumanity"][i+1][0], DATA.lastSentenceHeart) < 0.75 and DATA.data["sentenceHumanity"][i][1] != DATA.data["sentenceHumanity"][i+1][1] and DATA.data["sentenceHumanity"][i+1][1] == "!" and "!system" not in DATA.data["sentence"][i+1][1]:
                            #print("返信: {}, {}".format(DATA.data["sentenceHumanity"][i+1][0], i+1))
                            flag = True
                            for iiiii in range(7):
                                if i+1+iiiii < len(DATA.data["sentenceHumanity"]) - 1:
                                    if DATA.data["sentenceHumanity"][i+1+iiiii][0] == "×":
                                        flag = False
                                        break
                            if flag:
                                DATA.Hsa = ii
                                DATA.Hheart = i+1
                                DATA.HheartLastSpeaker = DATA.data["sentenceHumanity"][i+1][1]
                                DATA.Hrate = rate
                                DATA.mode = 1
                                return DATA.data["sentenceHumanity"][i+1][0]
                        else:
                            pass
                    else:
                        DATA.Hheart = i
                        return
                i += 1
                ii += 1















    except:
        import traceback
        traceback.print_exc()





    return None




