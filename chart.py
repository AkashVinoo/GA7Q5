import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style and context for professional look
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic customer engagement data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
hours = [f"{h}:00" for h in range(24)]
np.random.seed(42)

data = []
for day in days:
    # Weekdays have higher baseline engagement, weekends lower
    base = np.random.normal(50 if day not in ['Saturday', 'Sunday'] else 20, 10, 24)
    # Higher engagement around lunch hours (10am-2pm) on weekdays
    if day not in ['Saturday', 'Sunday']:
        base[10:14] += 20
    data.append(np.clip(base, 0, 100))

df = pd.DataFrame(data, index=days, columns=hours)

# Set DPI and figure size to get exactly 512x512 pixels
dpi = 100
figsize = (512 / dpi, 512 / dpi)  # (5.12, 5.12) inches

plt.figure(figsize=figsize, dpi=dpi)

# Create heatmap
sns.heatmap(df, cmap="YlGnBu", linewidths=0.5, linecolor='gray',
            cbar_kws={'label': 'Engagement Score'}, annot=True, fmt=".0f")

plt.title("Customer Engagement Heatmap", fontsize=16, pad=20)
plt.xlabel("Hour of Day")
plt.ylabel("Day of Week")

plt.tight_layout(pad=1)

# Save image WITHOUT bbox_inches or pad_inches to keep exact canvas size
plt.savefig("chart.png", dpi=dpi)
plt.close()
