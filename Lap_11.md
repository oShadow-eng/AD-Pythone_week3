"""Day 11 Activity: Outlier Strategies
Tasks:
1) Load numeric data with outliers
2) Implement percentile capping (winsorization)
3) Implement removal strategy
4) Compare summary stats before/after
"""

import pandas as pd
import numpy as np

#Task 1: Load numeric data with outliers
data = pd.read_csv(r"C:\Users\GAMER\OneDrive\سطح المكتب\Video\Photo\day11_income.csv")
df = pd.DataFrame(data)

#Task 2: Implement percentile capping (winsorization)
def winsorize_series(s, lower_q, upper_q):
    lower = s.quantile(lower_q)
    upper = s.quantile(upper_q)
    return s.clip(lower=lower, upper=upper)

#Task 3: Implement removal strategy
def remove_upper_tail(s, upper_q):
    upper = s.quantile(upper_q)
    return s[s <= upper]

#Task 4: Compare summary stats before/after

#Summary stats before
print("Summary stats before: ")
print(df['income'].describe())
#Summary stats after
print("Summary stats after winsorization: ")
print(winsorize_series(df['income'], 0.05, 0.95).describe())
#Summary stats after removal
print("Summary stats after removal: ")
print(remove_upper_tail(df['income'], 0.95).describe())
