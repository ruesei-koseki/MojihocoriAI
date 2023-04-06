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
                    DATA.heart = i
                    DATA.rate = rate
                    return
                i += 1
                ii += 1

    except:
        import traceback
        traceback.print_exc()
    return None