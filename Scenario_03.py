# Missing Value Handling
# Task: A dataset has missing values in the "income" column. Write code to:

# 1. Replace missing values with the median if the data is normally distributed.

# 2. Replace with the mode if skewed.
# Use Pandas and a skewness threshold of 0.5.


import pandas as pd #importing the Pandas library as pd
from scipy.stats import skew    #It tells you whether your data is normal, left-skewed, or right-skewed.

def handle_missing_values(df, column='income', skewness_threshold=0.5):

    # If there are no missing values, nothing to fix
    if df[column].isnull().sum() == 0:
        return df
    
    # Calculate how skewed the income data is (ignore missing values)
    data_skewness = skew(df[column].dropna())
    
    if abs(data_skewness) < skewness_threshold:  # If skewness is low, data looks normal
        replacement_value = df[column].median() # Use median to fill missing values
    else:
        if not df[column].mode().empty: # Data is skewed, so use the most common value
            replacement_value = df[column].mode()[0]
        else:
            replacement_value = df[column].median()   # If mode is not found, use median as backup
    
    # Replace all missing income values with the chosen value
    df[column].fillna(replacement_value, inplace=True)

    return df

# Sample data with one missing income value 
df = pd.DataFrame({'income': [50000, 60000, None, 70000, 80000]})

df = handle_missing_values(df)  # Fix missing values

print(df)   # here Showing final data

