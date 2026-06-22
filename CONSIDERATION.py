import DATA
from rapidfuzz.distance import Levenshtein

a = 0.2
def looking(x, u, reply=True, force=False):
    global a
    #過去の発言をもとに考える
    try:
        print("思考中: {}".format(x))

        #今の気持ちから考える
        f = DATA.heart+1
        t = len(DATA.data["sentence"]) - 1
        i = f
        d = 0
        b = 0
        for sen in DATA.data["sentence"][f:t]:
            c = Levenshtein.normalized_similarity(x, sen[0]) 
            if d > c:
                if (i != len(DATA.data["sentence"]) and
                    Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceInput) < 0.85 and
                    Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentence) < 0.85 and
                    Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceHeart) < 0.85 and
                    "!system" not in DATA.data["sentence"][i+1][1] and
                    "!input" not in DATA.data["sentence"][i+1][1] and
                    DATA.data["sentence"][i+1][0] != "!bad" and
                    DATA.data["sentence"][i+1][0] != "!good" and
                    DATA.data["sentence"][i+1][1] != "!" and
                    DATA.data["sentence"][i+1][1] != DATA.data["sentence"][i][1]):
                    d = c
                    b = i
            i += 1
        f = 0
        t = DATA.heart-1
        i = f
        for sen in DATA.data["sentence"][f:t]:
            c = Levenshtein.normalized_similarity(x, sen[0]) 
            if d > c:
                if (i != len(DATA.data["sentence"]) and
                    Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceInput) < 0.85 and
                    Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentence) < 0.85 and
                    Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceHeart) < 0.85 and
                    "!system" not in DATA.data["sentence"][i+1][1] and
                    "!input" not in DATA.data["sentence"][i+1][1] and
                    DATA.data["sentence"][i+1][0] != "!bad" and
                    DATA.data["sentence"][i+1][0] != "!good" and
                    DATA.data["sentence"][i+1][1] != "!" and
                    DATA.data["sentence"][i+1][1] != DATA.data["sentence"][i][1]):
                    d = c
                    b = i
            i += 1
        flag = False
        for iiiii in range(1):
            if b+2+iiiii < len(DATA.data["sentence"]) - 1:
                if DATA.data["sentence"][b+2+iiiii][0] == "!good":
                    flag = True
                    break
        for iiiii in range(1):
            if b+2+iiiii < len(DATA.data["sentence"]) - 1:
                if DATA.data["sentence"][b+2+iiiii][0] == "!bad":
                    flag = False
                    break
        if flag and b and d >= 0.6:
            print("類似: {}, {}, {}".format(DATA.data["sentence"][b][0], b, d))
            print("返信: {}, {}".format(DATA.data["sentence"][b+1][0], b+1))
            DATA.lastSentenceInputHeart = DATA.data["sentence"][b][0]
            DATA.heartLastSpeakerInput = DATA.data["sentence"][b][1]
            DATA.heart = b+1
            DATA.heartLastSpeaker = DATA.data["sentence"][b+1][1]
            DATA.lastSentenceHeart = DATA.data["sentence"][b+1][0]
            return DATA.data["sentence"][b+1][0]



        #今の気持ちから考える
        f = DATA.heart+1
        t = len(DATA.data["sentence"]) - 1
        i = f
        d = 0
        b = 0
        for sen in DATA.data["sentence"][f:t]:
            c = Levenshtein.normalized_similarity(u+": "+x, sen[1]+": "+sen[0]) 
            if d > c:
                if (i != len(DATA.data["sentence"]) and
                    Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceInput) < 0.85 and
                    Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentence) < 0.85 and
                    Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceHeart) < 0.85 and
                    "!system" not in DATA.data["sentence"][i+1][1] and
                    "!input" not in DATA.data["sentence"][i+1][1] and
                    DATA.data["sentence"][i+1][0] != "!bad" and
                    DATA.data["sentence"][i+1][0] != "!good" and
                    DATA.data["sentence"][i+1][1] != "!" and
                    DATA.data["sentence"][i+1][1] != DATA.data["sentence"][i][1]):
                    d = c
                    b = i
            i += 1
        f = 0
        t = DATA.heart-1
        i = f
        for sen in DATA.data["sentence"][f:t]:
            c = Levenshtein.normalized_similarity(u+": "+x, sen[1]+": "+sen[0]) 
            if d > c:
                if (i != len(DATA.data["sentence"]) and
                    Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceInput) < 0.85 and
                    Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentence) < 0.85 and
                    Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceHeart) < 0.85 and
                    "!system" not in DATA.data["sentence"][i+1][1] and
                    "!input" not in DATA.data["sentence"][i+1][1] and
                    DATA.data["sentence"][i+1][0] != "!bad" and
                    DATA.data["sentence"][i+1][0] != "!good" and
                    DATA.data["sentence"][i+1][1] != "!" and
                    DATA.data["sentence"][i+1][1] != DATA.data["sentence"][i][1]):
                    d = c
                    b = i
            i += 1
        flag = True
        for iiiii in range(1):
            if b+2+iiiii < len(DATA.data["sentence"]) - 1:
                if DATA.data["sentence"][b+2+iiiii][0] == "!bad":
                    flag = False
                    break
        if flag and b:
            print("類似: {}, {}, {}".format(DATA.data["sentence"][b][0], b, d))
            print("返信: {}, {}".format(DATA.data["sentence"][b+1][0], b+1))
            DATA.lastSentenceInputHeart = DATA.data["sentence"][b][0]
            DATA.heartLastSpeakerInput = DATA.data["sentence"][b][1]
            DATA.heart = b+1
            DATA.heartLastSpeaker = DATA.data["sentence"][b+1][1]
            DATA.lastSentenceHeart = DATA.data["sentence"][b+1][0]
            return DATA.data["sentence"][b+1][0]


        #今の気持ちから考える
        f = DATA.heart+1
        t = len(DATA.data["sentence"]) - 1
        i = f
        d = 0
        b = None
        for sen in DATA.data["sentence"][f:t]:
            c = Levenshtein.normalized_similarity(u+": "+x, sen[1]+": "+sen[0]) 
            if d < c:
                if (i != len(DATA.data["sentence"]) and
                    Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceInput) < 0.85 and
                    Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentence) < 0.85 and
                    Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceHeart) < 0.85 and
                    "!system" not in DATA.data["sentence"][i+1][1] and
                    "!input" not in DATA.data["sentence"][i+1][1] and
                    DATA.data["sentence"][i+1][0] != "!bad" and
                    DATA.data["sentence"][i+1][0] != "!good"):
                    d = c
                    b = i
            i += 1
        f = 0
        t = DATA.heart-1
        i = f
        ii = 0
        for sen in DATA.data["sentence"][f:t]:
            c = Levenshtein.normalized_similarity(u+": "+x, sen[1]+": "+sen[0]) 
            if d < c:
                if (i != len(DATA.data["sentence"]) and
                    Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceInput) < 0.85 and
                    Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentence) < 0.85 and
                    Levenshtein.normalized_similarity(DATA.data["sentence"][i+1][0], DATA.lastSentenceHeart) < 0.85 and
                    "!system" not in DATA.data["sentence"][i+1][1] and
                    "!input" not in DATA.data["sentence"][i+1][1] and
                    DATA.data["sentence"][i+1][0] != "!bad" and
                    DATA.data["sentence"][i+1][0] != "!good"):
                    d = c
                    b = i
            i += 1
        flag = True
        for iiiii in range(1):
            if b+2+iiiii < len(DATA.data["sentence"]) - 1:
                if DATA.data["sentence"][b+2+iiiii][0] == "!bad":
                    flag = False
                    break
        if flag and b:
            print("類似: {}, {}, {}".format(DATA.data["sentence"][b][0], b, d))
            print("返信: {}, {}".format(DATA.data["sentence"][b+1][0], b+1))
            DATA.lastSentenceInputHeart = DATA.data["sentence"][b][0]
            DATA.heartLastSpeakerInput = DATA.data["sentence"][b][1]
            DATA.heart = b+1
            DATA.heartLastSpeaker = DATA.data["sentence"][b+1][1]
            DATA.lastSentenceHeart = DATA.data["sentence"][b+1][0]
            return DATA.data["sentence"][b+1][0]


    except:
        import traceback
        traceback.print_exc()
    return None