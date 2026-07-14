"""
05_visualisation.py
Bar chart comparing control vs treatment conversion rate, with error bars
representing the standard error of each proportion.
"""

import matplotlib.pyplot as plt
import numpy as np

# Same numbers used in the significance test
conversions = [17489, 17264]   # [control, treatment]
totals = [145274, 145310]      # [control, treatment]

rates = [c / t for c, t in zip(conversions, totals)]

# Standard error for each proportion: sqrt( p*(1-p) / n )
errors = [np.sqrt(p * (1 - p) / n) for p, n in zip(rates, totals)]

labels = ["Control (old page)", "Treatment (new page)"]
colors = ["#4C72B0", "#DD8452"]

fig, ax = plt.subplots(figsize=(6, 5))
bars = ax.bar(labels, rates, yerr=errors, capsize=8, color=colors)

# Add percentage labels on top of each bar
for bar, rate in zip(bars, rates):
    ax.text(bar.get_x() + bar.get_width() / 2, rate + 0.003,
             f"{rate:.2%}", ha="center", fontsize=11, fontweight="bold")

ax.set_ylabel("Conversion Rate")
ax.set_title("Conversion Rate by Group (± standard error)\np = 0.19, not statistically significant")
ax.set_ylim(0, max(rates) + 0.03)

plt.tight_layout()
plt.savefig("cvr_by_group.png", dpi=150)
plt.show()

print("Saved chart to cvr_by_group.png")