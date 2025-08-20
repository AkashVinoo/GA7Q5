import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Seaborn styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Create synthetic data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
hours = [f"{h}:00" for h in range(24)]
np.random.seed(42)
data = []

for day in days:
    base = np.random.normal(50 if day not in ['Saturday', 'Sunday'] else 20, 10, 24)
    if day not in ['Saturday', 'Sunday']:
        base[10:14] += 20  # Simulate midday peak
    data.append(np.clip(base, 0, 100))

df = pd.DataFrame(data, index=days, columns=hours)

# Set figure size to 512x512 pixels => 8x8 inches @ 64 dpi
plt.figure(figsize=(8, 8), dpi=64)

# Create heatmap
sns.heatmap(df, cmap="YlGnBu", linewidths=0.5, linecolor='gray',
            cbar_kws={'label': 'Engagement Score'}, annot=True, fmt=".0f")

plt.title("Customer Engagement Heatmap", fontsize=16, pad=20)
plt.xlabel("Hour of Day")
plt.ylabel("Day of Week")

# Save with exact size
plt.tight_layout()
plt.savefig("chart.png", dpi=64, bbox_inches='tight')
plt.close()
