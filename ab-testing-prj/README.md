# A/B Testing: Landing Page Conversion Rate Analysis

Analysis of a randomized A/B test comparing an old vs. new landing page,
testing whether the redesign improves conversion rate. Built with a
SQL-first workflow: all data cleaning and aggregation done in SQL,
with Python used only for statistical significance testing and visualization.

**Main result:** see [`04_findings.md`](04_findings.md) for the full write-up.

## Project structure (run in this order)

| File | Purpose |
|------|---------|
| `load_ab_data.py` | Loads raw `ab_data.csv` into SQLite (`ab_data.db`) |
| `01_cleaning.sql` | Removes mismatched group/page rows and duplicate users |
| `02_eda.sql` | Sanity checks: group balance, date range coverage |
| `03_significance_test.py` | Two-proportion z-test (statsmodels) on conversion rates |
| `04_findings.md` | Full write-up: finding, recommendation, caveats, next steps |
| `05_visualisation.py` | Bar chart of conversion rate by group with error bars |

## Dataset
[Udacity A/B Testing dataset](https://www.kaggle.com/datasets) —
294,478 rows, ~290k unique users, Jan 2–24 2017.

## Tools
SQLite (via Python's built-in `sqlite3`), pandas (data loading only),
statsmodels (significance testing), matplotlib (visualization).

## Key finding
No statistically significant difference in conversion rate between the
old and new landing page (control: 12.04%, treatment: 11.88%, p = 0.19).
Recommend **not shipping** the redesign based on this data.