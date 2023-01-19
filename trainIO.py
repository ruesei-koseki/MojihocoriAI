import blob
import sys
if sys.argv[1] and sys.argv[2]:
    blob.initialize(sys.argv[1], "discord")
else:
    print("人格フォルダとコーパスを指定してください。")
    exit()
into = []
out = []
with open(sys.argv[2], "r", encoding="utf-8") as f:
    for line in f:
        into.append(line.split(",")[0])
        out.append(line.split(",")[1])
for i in range(len(into)):
    blob.MEMORY.learnSentence(into[i], "!input")
    blob.MEMORY.learnSentence(out[i], "!")
blob.MEMORY.save()