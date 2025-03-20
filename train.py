import mojihocori
import sys
if sys.argv[1] and sys.argv[2]:
    mojihocori.initialize(sys.argv[1], "discord")
else:
    print("人格フォルダとコーパスを指定してください。")
    exit()
data = []
with open(sys.argv[2], "r", encoding="utf-8") as f:
    for line in f:
        try:
            data.append([line.split(",", 1)[0], line.split(",", 1)[1]])
        except:
            pass
for d in data:
    mojihocori.MEMORY.learnSentence(d[1].replace("-br", "\n").strip(), d[0], save=False)
mojihocori.MEMORY.saveData()