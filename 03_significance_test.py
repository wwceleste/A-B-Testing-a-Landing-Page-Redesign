"""
03_significance_test.py
Two-proportion z-test comparing control vs treatment conversion rates.
Numbers below come directly from the SQL aggregation in 01_cleaning.sql.
"""

from statsmodels.stats.proportion import proportions_ztest

# counts of conversions in each group: [control, treatment]
conversions = [17489, 17264]
# total users in each group: [control, treatment]
totals = [145274, 145310]

z_stat, p_value = proportions_ztest(count=conversions, nobs=totals)

control_rate = conversions[0] / totals[0]
treatment_rate = conversions[1] / totals[1]

print(f"Control CVR:   {control_rate:.4f}")
print(f"Treatment CVR: {treatment_rate:.4f}")
print(f"z-statistic:   {z_stat:.4f}")
print(f"p-value:       {p_value:.4f}")

if p_value < 0.05:
    print("\nResult: statistically significant difference (p < 0.05)")
else:
    print("\nResult: NOT statistically significant (p >= 0.05) — gap could be due to chance")