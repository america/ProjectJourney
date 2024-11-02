import json
import matplotlib.pyplot as plt

# Load progress data from progress.json
with open("progress.json") as f:
    data = json.load(f)

# Extracting project names and progress values
project_names = list(data.keys())
progress_values = list(data.values())

# Create bar chart
plt.figure(figsize=(10, 6))
plt.barh(project_names, progress_values)
plt.xlabel("Progress (%)")
plt.title("Project Progress Overview")
plt.xlim(0, 100)  # Limit x-axis to 100%

# Save chart as image
plt.savefig("progress_bar_chart.png")
