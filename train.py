import blob
import sys
if sys.argv[1] and sys.argv[2]:
    blob.initialize(sys.argv[1], "discord")
else:
    print("人格フォルダとコーパスを指定してください。")
    exit()
data = []
with open(sys.argv[2], "r", encoding="utf-8") as f:
    state = 0
    memo = ""
    memoUser = ""
    i = 0
    for line in f:
        try:
            if line == "":
                continue
            if state == 0 and line.split(",", 1)[1][0] == "\"":
                state = 1
            if state == 1 and line[-2] == "\"":
                memo += line.replace("\"\n", "")
                data.append([memoUser, memo])
                state = 0
                memo = ""
                memoUser = ""
                i = 0
            elif state == 1 and i == 0:
                memo += line.split(",", 1)[1][1:]
                memoUser = line.split(",", 1)[0]
                i += 1
            elif state == 1:
                memo += line
                i += 1
            else:
                data.append([line.split(",", 1)[0], line.split(",", 1)[1]])
        except:
            pass
for d in data:
    blob.MEMORY.learnSentence(d[1].replace("-br", "\n").strip(), d[0], save=False)
blob.MEMORY.saveData()