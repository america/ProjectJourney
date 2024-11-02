import json
import matplotlib.pyplot as plt

# progress.jsonファイルを読み込み
with open("progress.json") as f:
    data = json.load(f)

# 円グラフを作成
labels = data.keys()
sizes = data.values()

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
plt.axis("equal")
plt.title("Project Progress")
plt.savefig("progress.png")
