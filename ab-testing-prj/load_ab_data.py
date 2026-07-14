"""
Loads ab_data.csv into a SQLite database (ab_data.db).
This is the ONLY place pandas is used for "analysis" purposes --
it's just a bridge to get the raw CSV into a queryable SQL database.
All actual cleaning / aggregation happens in SQL from here on.
"""

import pandas as pd
import sqlite3

# 1. Load the raw CSV
df = pd.read_csv("ab_data.csv")

print(f"Loaded {len(df)} rows from ab_data.csv")
print(df.head())

# 2. Connect to (or create) the SQLite database
conn = sqlite3.connect("ab_data.db")

# 3. Write the raw data into a table called 'ab_data_raw'
#    We keep this as the untouched raw table -- cleaning happens
#    in a separate SQL step that creates 'ab_data_clean'
df.to_sql("ab_data_raw", conn, if_exists="replace", index=False)

conn.close()

print("\nDone! Created ab_data.db with table 'ab_data_raw'")