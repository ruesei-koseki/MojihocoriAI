import DATA
from rapidfuzz.distance import Levenshtein

a = 0.1

def looking(x, u, reply=True, force=False):
    global a
    #過去の発言をもとに考える
    try:
        print("思考中: {}".format(x))

        rate = 1
        while True:
            if rate <= 0:
                break
            rate -= a
            #今の気持ちから考える
            f = DATA.heart
            t = len(DATA.data["sentence"]) - 1
            i = f
            ii = 0
            for sen in DATA.data["sentence"][f:t]:
                if i >= len(DATA.data["sentence"]) - 1:
                    break
                if Levenshtein.normalized_similarity("{}: {}".format(u, x*16), "{}: {}".format(DATA.data["sentence"][i][1], DATA.data["sentence"][i][0]*16)) >= rate:
                    for iiii in range(1):
                        if i+iiii+1 >= len(DATA.data["sentence"]):
                            break
                        if reply:
                            if (i != len(DATA.data["sentence"]) and
                                Levenshtein.normalized_similarity(DATA.data["sentence"][i + iiii + 1][0], DATA.lastSentenceInput) < 0.85 and
                                Levenshtein.normalized_similarity(DATA.data["sentence"][i + iiii + 1][0], DATA.lastSentence) < 0.85 and
                                Levenshtein.normalized_similarity(DATA.data["sentence"][i + iiii + 1][0], DATA.lastSentenceHeart) < 0.85 and
                                "!system" not in DATA.data["sentence"][i + iiii + 1][1] and
                                DATA.data["sentence"][i + iiii + 1][1] != "!"):
                                flag = True
                                for iiiii in range(1):
                                    if i+iiii+2+iiiii < len(DATA.data["sentence"]) - 1:
                                        if DATA.data["sentence"][i+iiii+2+iiiii][0] == "!bad":
                                            flag = False
                                            break
                                if flag:
                                    print("類似: {}, {}, {}".format(DATA.data["sentence"][i][0], i, rate))
                                    print("返信: {}, {}".format(DATA.data["sentence"][i+iiii+1][0], i+iiii+1))
                                    DATA.lastSentenceInputHeart = DATA.data["sentence"][i][0]
                                    DATA.heartLastSpeakerInput = DATA.data["sentence"][i][1]
                                    DATA.sa = ii
                                    DATA.skip = iiii
                                    DATA.heart = i+iiii+1
                                    DATA.heartLastSpeaker = DATA.data["sentence"][i+iiii+1][1]
                                    DATA.lastSentenceHeart = DATA.data["sentence"][i+iiii+1][0]
                                    DATA.rate = rate
                                    return DATA.data["sentence"][i+iiii+1][0]
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
                if Levenshtein.normalized_similarity("{}: {}".format(u, x*16), "{}: {}".format(DATA.data["sentence"][i][1], DATA.data["sentence"][i][0]*16)) >= rate:
                    for iiii in range(1):
                        if i+iiii+1 >= len(DATA.data["sentence"]):
                            break
                        if reply:
                            if (i != len(DATA.data["sentence"]) and
                                Levenshtein.normalized_similarity(DATA.data["sentence"][i + iiii + 1][0], DATA.lastSentenceInput) < 0.85 and
                                Levenshtein.normalized_similarity(DATA.data["sentence"][i + iiii + 1][0], DATA.lastSentence) < 0.85 and
                                Levenshtein.normalized_similarity(DATA.data["sentence"][i + iiii + 1][0], DATA.lastSentenceHeart) < 0.85 and
                                "!system" not in DATA.data["sentence"][i + iiii + 1][1] and
                                DATA.data["sentence"][i + iiii + 1][1] != "!"):
                                flag = True
                                for iiiii in range(1):
                                    if i+iiii+2+iiiii < len(DATA.data["sentence"]) - 1:
                                        if DATA.data["sentence"][i+iiii+2+iiiii][0] == "!bad":
                                            flag = False
                                            break
                                if flag:
                                    print("類似: {}, {}, {}".format(DATA.data["sentence"][i][0], i, rate))
                                    print("返信: {}, {}".format(DATA.data["sentence"][i+iiii+1][0], i+iiii+1))
                                    DATA.lastSentenceInputHeart = DATA.data["sentence"][i][0]
                                    DATA.heartLastSpeakerInput = DATA.data["sentence"][i][1]
                                    DATA.sa = ii
                                    DATA.skip = iiii
                                    DATA.heart = i+iiii+1
                                    DATA.heartLastSpeaker = DATA.data["sentence"][i+iiii+1][1]
                                    DATA.lastSentenceHeart = DATA.data["sentence"][i+iiii+1][0]
                                    DATA.rate = rate
                                    return DATA.data["sentence"][i+iiii+1][0]
                            else:
                                pass
                        else:
                            DATA.heart = i
                            DATA.rate = rate
                            return None
                i += 1
                ii += 1

        rate = 1
        while True:
            if rate <= 0:
                break
            rate -= a
            #今の気持ちから考える
            f = DATA.heart
            t = len(DATA.data["sentence"]) - 1
            i = f
            ii = 0
            for sen in DATA.data["sentence"][f:t]:
                if i >= len(DATA.data["sentence"]) - 1:
                    break
                if Levenshtein.normalized_similarity("{}: {}".format(u, x), "{}: {}".format(DATA.data["sentence"][i][1], DATA.data["sentence"][i][0])) >= rate:
                    for iiii in range(1):
                        if i+iiii+1 >= len(DATA.data["sentence"]):
                            break
                        if reply:
                            if (i != len(DATA.data["sentence"]) and
                                Levenshtein.normalized_similarity(DATA.data["sentence"][i + iiii + 1][0], DATA.lastSentenceInput) < 0.85 and
                                Levenshtein.normalized_similarity(DATA.data["sentence"][i + iiii + 1][0], DATA.lastSentence) < 0.85 and
                                Levenshtein.normalized_similarity(DATA.data["sentence"][i + iiii + 1][0], DATA.lastSentenceHeart) < 0.85 and
                                "!system" not in DATA.data["sentence"][i + iiii + 1][1]):
                                flag = True
                                for iiiii in range(1):
                                    if i+iiii+2+iiiii < len(DATA.data["sentence"]) - 1:
                                        if DATA.data["sentence"][i+iiii+2+iiiii][0] == "!bad":
                                            flag = False
                                            break
                                if flag:
                                    print("類似: {}, {}, {}".format(DATA.data["sentence"][i][0], i, rate))
                                    print("返信: {}, {}".format(DATA.data["sentence"][i+iiii+1][0], i+iiii+1))
                                    DATA.lastSentenceInputHeart = DATA.data["sentence"][i][0]
                                    DATA.heartLastSpeakerInput = DATA.data["sentence"][i][1]
                                    DATA.sa = ii
                                    DATA.skip = iiii
                                    DATA.heart = i+iiii+1
                                    DATA.heartLastSpeaker = DATA.data["sentence"][i+iiii+1][1]
                                    DATA.lastSentenceHeart = DATA.data["sentence"][i+iiii+1][0]
                                    DATA.rate = rate
                                    return DATA.data["sentence"][i+iiii+1][0]
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
                if Levenshtein.normalized_similarity("{}: {}".format(u, x), "{}: {}".format(DATA.data["sentence"][i][1], DATA.data["sentence"][i][0])) >= rate:
                    for iiii in range(1):
                        if i+iiii+1 >= len(DATA.data["sentence"]):
                            break
                        if reply:
                            if (i != len(DATA.data["sentence"]) and
                                Levenshtein.normalized_similarity(DATA.data["sentence"][i + iiii + 1][0], DATA.lastSentenceInput) < 0.85 and
                                Levenshtein.normalized_similarity(DATA.data["sentence"][i + iiii + 1][0], DATA.lastSentence) < 0.85 and
                                Levenshtein.normalized_similarity(DATA.data["sentence"][i + iiii + 1][0], DATA.lastSentenceHeart) < 0.85 and
                                "!system" not in DATA.data["sentence"][i + iiii + 1][1]):
                                flag = True
                                for iiiii in range(1):
                                    if i+iiii+2+iiiii < len(DATA.data["sentence"]) - 1:
                                        if DATA.data["sentence"][i+iiii+2+iiiii][0] == "!bad":
                                            flag = False
                                            break
                                if flag:
                                    print("類似: {}, {}, {}".format(DATA.data["sentence"][i][0], i, rate))
                                    print("返信: {}, {}".format(DATA.data["sentence"][i+iiii+1][0], i+iiii+1))
                                    DATA.lastSentenceInputHeart = DATA.data["sentence"][i][0]
                                    DATA.heartLastSpeakerInput = DATA.data["sentence"][i][1]
                                    DATA.sa = ii
                                    DATA.skip = iiii
                                    DATA.heart = i+iiii+1
                                    DATA.heartLastSpeaker = DATA.data["sentence"][i+iiii+1][1]
                                    DATA.lastSentenceHeart = DATA.data["sentence"][i+iiii+1][0]
                                    DATA.rate = rate
                                    return DATA.data["sentence"][i+iiii+1][0]
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
