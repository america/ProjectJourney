import json
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import font_manager

# Noto Sans JP フォントを直接指定
font_path = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"  # フォントのパス
rcParams['font.family'] = font_manager.FontProperties(fname=font_path).get_name()

# progress.json を読み込む
with open("progress.json") as f:
    data = json.load(f)

# プロジェクト名と進捗状況を取得
project_names = list(data.keys())
progress_values = list(data.values())

# 横向きの棒グラフを作成
plt.figure(figsize=(10, 6))
plt.barh(project_names, progress_values, color="skyblue", edgecolor="black")
plt.xlabel("Progress (%)", fontsize=12)
plt.title("Project Progress Overview", fontsize=16)
plt.xlim(0, 100)  # X軸の範囲を0〜100%に固定

# プロジェクト名を見やすく調整
plt.gca().invert_yaxis()  # 上位のプロジェクトを上に表示
plt.tight_layout()  # レイアウト調整でラベルの切れを防ぐ

# グラフを画像として保存
plt.savefig("progress_bar_chart.png")
