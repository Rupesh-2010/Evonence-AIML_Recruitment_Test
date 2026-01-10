# Scenario 4: Text Pre-processing
# Task: Clean a text column in a DataFrame by:
#     1. Converting to lowercase.
#     2. Removing special characters (e.g., !, @).

#     3. Tokenizing the text.



#####################################    ANSWER   #####################################


import pandas as pd #importing the Pandas library as pd
import re

def clean_and_tokenize(df, text_col="text"):

    if text_col not in df.columns:    # Check if the given text column exists in the data
        raise ValueError(f"Column '{text_col}' not found.")

    df[text_col] = df[text_col].str.lower()     # Convert all text to lowercase

    # Remove symbols like !, @, # and keep only letters, numbers and spaces
    df[text_col] = df[text_col].apply(lambda x: re.sub(r"[^a-z0-9\s]", " ", x))

    df["tokens"] = df[text_col].str.split() # Split each sentence into words

    return df

# Take sample Data for test.
df = pd.DataFrame({"text": ["Hello, World!","i a@m R-upe/sh.!", "AI@ML is great!!!"]})

# Clean the text and show tokens
print(clean_and_tokenize(df))
