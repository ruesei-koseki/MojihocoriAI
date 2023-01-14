import sanae
import sys
if sys.argv[1] and sys.argv[2]:
    sanae.initialize(sys.argv[1], "discord")
else:
    print("人格フォルダとコーパスを指定してください。")
    exit()
data = []
with open(sys.argv[2], "r", encoding="utf-8") as f:
    for line in f:
        data.append([line.split(",")[0].replace("-br ", "\n"), line.split(",")[1]])
for d in data:
    sanae.MEMORY.learnSentence(d[1], d[0])
sanae.MEMORY.save()