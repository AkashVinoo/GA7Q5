import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style and context for professional appearance
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic data: engagement scores by day and hour
np.random.seed(42)  # for reproducibility
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
hours = [f"{h}:00" for h in range(24)]

# Simulate customer engagement: higher on weekdays, mid-day
data = []
for day in days:
    if day in ['Saturday', 'Sunday']:
        base = np.random.normal(20, 5, 24)  # low engagement
    else:
        base = np.random.normal(50, 15, 24)  # higher engagement mid-week
        base[10:14] += 20  # peak at mid-day
    data.append(np.clip(base, 0, 100))

# Create DataFrame
engagement_df = pd.DataFrame(data, index=days, columns=hours)

# Set figure size to 8x8 inches at 64 DPI = 512x512 pixels
plt.figure(figsize=(8, 8))

# Create heatmap
ax = sns.heatmap(
    engagement_df,
    cmap="YlGnBu",
    linewidths=0.5,
    linecolor='gray',
    cbar_kws={'label': 'Engagement Score'},
    annot=True,
    fmt=".0f"
)

# Titles and labels
plt.title("Customer Engagement Heatmap", fontsize=16, pad=20)
plt.xlabel("Hour of Day", fontsize=12)
plt.ylabel("Day of Week", fontsize=12)

# Save the chart
plt.tight_layout()
plt.savefig("chart.png", dpi=64, bbox_inches='tight')
plt.close()
