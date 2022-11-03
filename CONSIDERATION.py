import re
import json
import random
import time

import DATA

def looking(x, u, reply=True, force=False):
    #過去の発言をもとに考える
    try:





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
            kon = -1
            zen = -1

            cc = [0]
            for sen in DATA.data["sentence"][f:t]:
                into = u+": "+x
                a = -1
                b = 1
                c = 0
                while True:
                    zen = kon
                    kon = i
                    if into in sen[1]+": "+sen[0]:
                        c += 1
                    if len(x) == b:
                        cc[-1] = cc[-1] / ((len(x) + len(sen[0])) / 2)
                        c = c / ((len(x) + len(sen[0])) / 2)
                        
                        if len(cc) >= 2:
                            if (cc[-1] - cc[-2] >= rate or c >= rate) and "l:" in DATA.data["sentence"][i][1]:
                                print("類似: {}, {}".format(DATA.data["sentence"][i][0], i))
                                for iii in range(1):
                                    if i+1+iii >= len(DATA.data["sentence"]):
                                        break
                                    if reply:
                                        isMine = False
                                        for myname in DATA.settings["mynames"].split("|"):
                                            if DATA.data["sentence"][i+1+iii][1][2:] == myname:
                                                isMine = True
                                        if i != len(DATA.data["sentence"]) and DATA.data["sentence"][i][1] != DATA.data["sentence"][i+1+iii][1] and DATA.lastSentenceInput != DATA.data["sentence"][i+1+iii][0] and DATA.lastSentence != DATA.data["sentence"][i+1+iii][0] and (DATA.data["sentence"][i+1+iii][1] == "!" or DATA.data["sentence"][i+1+iii][1] == DATA.settings["myname"] or isMine):
                                            print("返信: {}, {}".format(DATA.data["sentence"][i+1+iii][0], i+1+iii))
                                            flag = True
                                            for iiiii in range(1):
                                                if i+1+iii+iiiii < len(DATA.data["sentence"]) - 1:
                                                    if DATA.data["sentence"][i+1+iii+iiiii][0] == "×":
                                                        flag = False
                                                        break
                                            if flag:
                                                DATA.sa = ii
                                                DATA.heart = i+1+iii
                                                DATA.skip = iii
                                                DATA.heartLastSpeaker = DATA.data["sentence"][i+1+iii][1]
                                                DATA.rate = rate
                                                return DATA.data["sentence"][i+1+iii][0]
                                        else:
                                            if not bool(re.search(DATA.settings["mynames"], DATA.lastSentenceInput)) and not force:
                                                DATA.sa = ii
                                                DATA.heart = i
                                                DATA.rate = rate
                                                return None
                                    else:
                                        DATA.sa = ii
                                        DATA.heart = i
                                        return
                        break
                    a += 1
                    b += 1
                    into = x[a:b]
                    if kon != zen:
                        cc.append(c)
                    cc[-1] = c
                    if len(cc) >= 2:
                        cc = cc[-2:]
                        cc[1] = c
                    else:
                        cc[-1] = c
                i += 1
                ii += 1




            #今の気持ちから少し離れる
            f = 0
            
            t = DATA.heart

            i = f
            ii = 0
            kon = -1
            zen = -1

            cc = [0]
            for sen in DATA.data["sentence"][f:t]:
                into = u+": "+x
                a = -1
                b = 1
                c = 0
                while True:
                    zen = kon
                    kon = i
                    if into in sen[1]+": "+sen[0]:
                        c += 1
                    if len(x) == b:
                        cc[-1] = cc[-1] / ((len(x) + len(sen[0])) / 2)
                        c = c / ((len(x) + len(sen[0])) / 2)
                        
                        if len(cc) >= 2:
                            if (cc[-1] - cc[-2] >= rate or c >= rate) and "l:" in DATA.data["sentence"][i][1]:
                                print("類似: {}, {}".format(DATA.data["sentence"][i][0], i))
                                for iii in range(1):
                                    if i+1+iii >= len(DATA.data["sentence"]):
                                        break
                                    if reply:
                                        isMine = False
                                        for myname in DATA.settings["mynames"].split("|"):
                                            if DATA.data["sentence"][i+1+iii][1][2:] == myname:
                                                isMine = True
                                        if i != len(DATA.data["sentence"]) and DATA.data["sentence"][i][1] != DATA.data["sentence"][i+1+iii][1] and DATA.lastSentenceInput != DATA.data["sentence"][i+1+iii][0] and DATA.lastSentence != DATA.data["sentence"][i+1+iii][0] and (DATA.data["sentence"][i+1+iii][1] == "!" or DATA.data["sentence"][i+1+iii][1] == DATA.settings["myname"] or isMine):
                                            print("返信: {}, {}".format(DATA.data["sentence"][i+1+iii][0], i+1+iii))
                                            flag = True
                                            for iiiii in range(1):
                                                if i+1+iii+iiiii < len(DATA.data["sentence"]) - 1:
                                                    if DATA.data["sentence"][i+1+iii+iiiii][0] == "×":
                                                        flag = False
                                                        break
                                            if flag:
                                                DATA.sa = ii
                                                DATA.heart = i+1+iii
                                                DATA.skip = iii
                                                DATA.heartLastSpeaker = DATA.data["sentence"][i+1+iii][1]
                                                DATA.rate = rate
                                                return DATA.data["sentence"][i+1+iii][0]
                                        else:
                                            if not bool(re.search(DATA.settings["mynames"], DATA.lastSentenceInput)) and not force:
                                                DATA.sa = ii
                                                DATA.heart = i
                                                DATA.rate = rate
                                                return None
                                    else:
                                        DATA.sa = ii
                                        DATA.heart = i
                                        return
                        break
                    a += 1
                    b += 1
                    into = x[a:b]
                    if kon != zen:
                        cc.append(c)
                    cc[-1] = c
                    if len(cc) >= 2:
                        cc = cc[-2:]
                        cc[1] = c
                    else:
                        cc[-1] = c
                i += 1
                ii += 1














        for kaisu in range(6):
            if kaisu == 0:
                rate = 1
            if kaisu == 1:
                rate = 0.8
            if kaisu == 2:
                rate = 0.6
            if kaisu == 3:
                rate = 0.4
            if kaisu == 4:
                rate = 0.2
            if kaisu == 5:
                rate = 0.0







            #今の気持ちから考える
            f = DATA.heart+1

            t = len(DATA.data["sentence"]) - 1
            
            i = f
            ii = 0
            kon = -1
            zen = -1

            cc = [0]
            for sen in DATA.data["sentence"][f:t]:
                into = u+": "+x
                a = -1
                b = 1
                c = 0
                while True:
                    zen = kon
                    kon = i
                    if into in sen[1]+": "+sen[0]:
                        c += 1
                    if len(x) == b:
                        cc[-1] = cc[-1] / ((len(x) + len(sen[0])) / 2)
                        c = c / ((len(x) + len(sen[0])) / 2)
                        
                        if len(cc) >= 2:
                            if cc[-1] - cc[-2] >= rate or c >= rate:
                                print("類似: {}, {}".format(DATA.data["sentence"][i][0], i))
                                for iii in range(1):
                                    if i+1+iii >= len(DATA.data["sentence"]):
                                        break
                                    if reply:
                                        isMine = False
                                        for myname in DATA.settings["mynames"].split("|"):
                                            if DATA.data["sentence"][i+1+iii][1] == myname:
                                                isMine = True
                                        if i != len(DATA.data["sentence"]) and DATA.data["sentence"][i][1] != DATA.data["sentence"][i+1+iii][1] and DATA.lastSentenceInput != DATA.data["sentence"][i+1+iii][0] and DATA.lastSentence != DATA.data["sentence"][i+1+iii][0] and (DATA.data["sentence"][i+1+iii][1] == "!" or DATA.data["sentence"][i+1+iii][1] == DATA.settings["myname"] or isMine):
                                            print("返信: {}, {}".format(DATA.data["sentence"][i+1+iii][0], i+1+iii))
                                            flag = True
                                            for iiiii in range(1):
                                                if i+1+iii+iiiii < len(DATA.data["sentence"]) - 1:
                                                    if DATA.data["sentence"][i+1+iii+iiiii][0] == "×":
                                                        flag = False
                                                        break
                                            if flag:
                                                DATA.sa = ii
                                                DATA.heart = i+1+iii
                                                DATA.skip = iii
                                                DATA.heartLastSpeaker = DATA.data["sentence"][i+1+iii][1]
                                                DATA.rate = rate
                                                return DATA.data["sentence"][i+1+iii][0]
                                        else:
                                            if not bool(re.search(DATA.settings["mynames"], DATA.lastSentenceInput)) and not force:
                                                DATA.sa = ii
                                                DATA.heart = i
                                                DATA.rate = rate
                                                return None
                                    else:
                                        DATA.heart = i
                                        return
                        break
                    a += 1
                    b += 1
                    into = x[a:b]
                    if kon != zen:
                        cc.append(c)
                    cc[-1] = c
                    if len(cc) >= 2:
                        cc = cc[-2:]
                        cc[1] = c
                    else:
                        cc[-1] = c
                i += 1
                ii += 1




            #今の気持ちから少し離れる
            f = 0
            
            t = DATA.heart

            i = f
            ii = 0
            kon = -1
            zen = -1

            cc = [0]
            for sen in DATA.data["sentence"][f:t]:
                into = u+": "+x
                a = -1
                b = 1
                c = 0
                while True:
                    zen = kon
                    kon = i
                    if into in sen[1]+": "+sen[0]:
                        c += 1
                    if len(x) == b:
                        cc[-1] = cc[-1] / ((len(x) + len(sen[0])) / 2)
                        c = c / ((len(x) + len(sen[0])) / 2)
                        
                        if len(cc) >= 2:
                            if cc[-1] - cc[-2] >= rate or c >= rate:
                                print("類似: {}, {}".format(DATA.data["sentence"][i][0], i))
                                for iii in range(1):
                                    if i+1+iii >= len(DATA.data["sentence"]):
                                        break
                                    if reply:
                                        isMine = False
                                        for myname in DATA.settings["mynames"].split("|"):
                                            if DATA.data["sentence"][i+1+iii][1] == myname:
                                                isMine = True
                                        if i != len(DATA.data["sentence"]) and DATA.data["sentence"][i][1] != DATA.data["sentence"][i+1+iii][1] and DATA.lastSentenceInput != DATA.data["sentence"][i+1+iii][0] and DATA.lastSentence != DATA.data["sentence"][i+1+iii][0] and (DATA.data["sentence"][i+1+iii][1] == "!" or DATA.data["sentence"][i+1+iii][1] == DATA.settings["myname"] or isMine):
                                            print("返信: {}, {}".format(DATA.data["sentence"][i+1+iii][0], i+1+iii))
                                            flag = True
                                            for iiiii in range(1):
                                                if i+1+iii+iiiii < len(DATA.data["sentence"]) - 1:
                                                    if DATA.data["sentence"][i+1+iii+iiiii][0] == "×":
                                                        flag = False
                                                        break
                                            if flag:
                                                DATA.sa = ii
                                                DATA.heart = i+1+iii
                                                DATA.skip = iii
                                                DATA.heartLastSpeaker = DATA.data["sentence"][i+1+iii][1]
                                                DATA.rate = rate
                                                return DATA.data["sentence"][i+1+iii][0]
                                        else:
                                            if not bool(re.search(DATA.settings["mynames"], DATA.lastSentenceInput)) and not force:
                                                DATA.sa = ii
                                                DATA.heart = i
                                                DATA.rate = rate
                                                return None
                                    else:
                                        DATA.heart = i
                                        return
                        break
                    a += 1
                    b += 1
                    into = x[a:b]
                    if kon != zen:
                        cc.append(c)
                    cc[-1] = c
                    if len(cc) >= 2:
                        cc = cc[-2:]
                        cc[1] = c
                    else:
                        cc[-1] = c
                i += 1
                ii += 1





    except:
        import traceback
        traceback.print_exc()





    return None

