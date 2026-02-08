"""Day 12 Activity: String & Date Cleaning
Tasks:
1) Clean city strings (strip, lower, remove punctuation)
2) Map synonyms to canonical values
3) Parse mixed-format timestamps and localize to UTC
"""

import pandas as pd

data = (r"C:\Users\GAMER\OneDrive\سطح المكتب\Video\Photo\day12_users.csv")
df = pd.read_csv(data)

#Task 1: Clean city strings
def clean_city(df):
    df = df.copy()  # Make a copy to avoid modifying the original DataFrame
    df['city'] = df['city'].str.replace('-', ' ', regex=False)  # Replace hyphens with spaces
    df['city'] = df['city'].str.replace(r'^\s+|\s+$', '', regex=True)  # Remove leading/trailing whitespace
    df['city'] = df['city'].str.replace(r'[^\w\s]', '', regex=True)  # Remove punctuation
    df['city'] = df['city'].str.lower()  # Convert to lowercase
    return df

#Task 2: Map synonyms to canonical values
def clean_name(df):
    df = df.copy()
    synonym_map = {
        'NYC': 'New York',
        'SF': 'San Francisco'
    }
    df['city'] = df['city'].replace(synonym_map)
    return df

#Task 3: Parse mixed-format timestamps and localize to UTC
def clean_timestamp(df):
    df = df.copy()
    df['signup_time'] = pd.to_datetime(df['signup_time'], errors='coerce', utc=True)
    return df

df_cleaned = clean_city(df)
df_cleaned = clean_name(df_cleaned)
df_cleaned = clean_timestamp(df_cleaned)
print(df_cleaned[['city', 'signup_time']])
# TODO: Implement standardize_city(df)
# TODO: Implement parse_and_localize(df)
# TODO: Print cleaned columns for inspectio
