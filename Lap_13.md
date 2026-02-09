"""
Day 13 Activity: Large Dataset Cleaning
Tasks:
1) Read CSV in chunks
2) Clean each chunk (e.g., numeric conversion)
3) Append cleaned chunks to output CSV
4) Track basic performance metrics
"""

import pandas as pd
import time
#Task 1: Read CSV in chunks
df = pd.read_csv('day13_large_users.csv', chunksize=100)
#Task 2: Clean each chunk (e.g., numeric conversion)
def clean_chunk(df):
    # Convert 'age' to numeric, coercing errors to NaN
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    # Fill NaN values in 'age' with the median age
    df['age'].fillna(df['age'].median())
    return df
#Task 3: Append cleaned chunks to output CSV
def process_large_file(path_in, path_out, chunksize):
    start_time = time.time()
    for i, chunk in enumerate(pd.read_csv(path_in, chunksize=chunksize)):
        cleaned_chunk = clean_chunk(chunk)
        if i == 0:
            cleaned_chunk.to_csv(path_out, index=False)
        else:
            cleaned_chunk.to_csv(path_out, mode='a', header=False, index=False)
    end_time = time.time()
    print(f"Processing completed in {end_time - start_time:.2f} seconds.")

print(clean_chunk(df.get_chunk(100)))  # Example of cleaning a single chunk
# TODO: Implement clean_chunk(df)
# TODO: Implement process_large_file(path_in, path_out, chunksize)

