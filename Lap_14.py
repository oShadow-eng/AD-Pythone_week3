"""
Day 14 Activity: Full Cleaning Pipeline
Tasks:
1) Build clean_data() that orchestrates type, missing, outliers, strings/dates
2) Add basic validation checks
3) Run end-to-end and inspect
"""

import pandas as pd
import numpy as np

data = pd.read_csv('day14_users_raw.csv')
df = pd.DataFrame(data)

#Task 1: Build clean_data() that orchestrates type, missing, outliers, strings/dates
def clean_types(df):
    # Convert 'age' to numeric, coercing errors to NaN
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    
    # Convert 'signup_time' to datetime, coercing errors to NaT
    df['signup_time'] = pd.to_datetime(df['signup_time'], errors='coerce')
    
    return df

#Task 2: Add basic validation checks
def validate_cleaned(df):
    # Check for negative ages
    if (df['age'] < 0).any():
        print("Warning: Negative ages found.")
    
    # Check for future signup dates
    if (df['signup_time'] > pd.Timestamp.now()).any():
        print("Warning: Future signup dates found.")
    
    return df

def clean_missing(df):
    # Fill missing ages with the median age
    df['age'] = df['age'].fillna(df['age'].median())
    
    # Fill missing signup times with the mode
    df['signup_time'] = df['signup_time'].fillna(df['signup_time'].mode()[0])#for example, fill missing signup times with the most common signup time
    
    return df

def handle_outliers(df):
    # Cap ages at 100
    df['age'] = np.where(df['age'] > 100, 100, df['age'])
    df['age'] = np.where(df['age'] < 0, 0, df['age'])  # Ensure no negative ages
    df['age'] = np.where(df['age'] == 0, np.nan, df['age'])#becouse 0 is not a valid age, we can set it to NaN and then handle it in the missing value step  
    return df

def clean_timestamp(df):
    df = df.copy()
    df['signup_time'] = pd.to_datetime(df['signup_time'], errors='coerce', utc=True)#for example, convert to datetime and set timezone to UTC
    return df

def clean_city(df):
    df = df.copy()
    df['city'] = df['city'].str.strip().str.lower()#for example, standardize case and remove extra spaces 
    df['city'] = df['city'].replace({'ny': 'New York', 'nyc': 'New York City', 'sf': 'San Francisco', 'la': 'Los Angeles'})#for example, standardize common city abbreviations
    df['city'] = df['city'].fillna('unknown')#for example, fill missing city values with 'unknown'
    return df
#Task 3: Run end-to-end and inspect
def clean_data(df):
    df = clean_types(df)# Placeholder for type cleaning function
    df = validate_cleaned(df)# Placeholder for validation function
    df = clean_missing(df)# Placeholder for missing value handling function
    df = handle_outliers(df)# Placeholder for outlier handling function
    df = clean_timestamp(df)# Placeholder for timestamp cleaning function
    df = clean_city(df)  # Placeholder for string/date cleaning function
    return df

print("Before cleaning:")
print(df)
df_cleaned = clean_data(df)
print("\nAfter cleaning:")  
print(df_cleaned)

# TODO: Implement clean_types(df)
# TODO: Implement clean_missing(df)
# TODO: Implement handle_outliers(df)
# TODO: Implement clean_strings_and_dates(df)
# TODO: Implement validate_cleaned(df)
# TODO: Implement clean_data(df) that calls the above in order
