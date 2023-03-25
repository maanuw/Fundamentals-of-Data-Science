import pandas as pd
import numpy as np

# Define the path to the CSV file
file_path = 'C:/Users/yfmad/Fundamentals-of-Data-Science/Physical-Design-Deliverable-2/assets/game/vgsales.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Define the WIN1252 character set
WIN1252 = 'cp1252'

# Define a function to encode a string into WIN1252 and replace any problematic characters with a replacement value
def encode_string(value, replacement=''):
    try:
        encoded_value = value.encode(WIN1252)
    except UnicodeEncodeError as e:
        encoded_value = value.encode(WIN1252, errors='ignore').decode(WIN1252)
        if not encoded_value:
            encoded_value = replacement
    return encoded_value

# Encode all string columns in the DataFrame into WIN1252
for col in df.select_dtypes(include='object'):
    df[col] = df[col].apply(encode_string)

# Drop rows where the 'Name' column is empty or NaN
df = df.dropna(subset=['Name'])
df['Name'] = df['Name'].astype(str)

# Drop rows where the 'Platform' column is empty or NaN
df = df.dropna(subset=['Platform'])
df['Name'] = df['Name'].astype(str)

df['Genre'] = df['Genre'].fillna('unknown').astype(str)

df['Publisher'] = df['Publisher'].fillna('unknown').astype(str)

# Handle missing values in the 'NA_Sales' column
na_sales_mean = df['NA_Sales'].mean()
df['NA_Sales'] = df['NA_Sales'].fillna(na_sales_mean).astype(float)

# Handle missing values in the 'EU_Sales' column
na_sales_mean = df['EU_Sales'].mean()
df['EU_Sales'] = df['EU_Sales'].fillna(na_sales_mean).astype(float)

# Handle missing values in the 'JP_Sales' column
na_sales_mean = df['JP_Sales'].mean()
df['JP_Sales'] = df['JP_Sales'].fillna(na_sales_mean).astype(float)

# Handle missing values in the 'Other_Sales' column
na_sales_mean = df['Other_Sales'].mean()
df['Other_Sales'] = df['Other_Sales'].fillna(na_sales_mean).astype(float)

# Handle missing values in the 'Global_Sales' column
na_sales_mean = df['Global_Sales'].mean()
df['Global_Sales'] = df['Global_Sales'].fillna(na_sales_mean).astype(float)

# Print the original number of rows
print("Original number of rows:", len(df))

# Delete the row where Rank is 16130
df = df.drop(df[df['Rank'] == 16130].index)
df = df.drop(df[df['Rank'] == 15002].index)
df = df.drop(df[df['Rank'] == 4147].index)

# Calculate the mean value of the 'Year' column
mean_year = df['Year'].mean()

# Replace missing values and non-finite values with the mean value
df['Year'] = df['Year'].fillna(mean_year).astype(int)

# Print the number of rows after deleting the row
print("Number of rows after deletion:", len(df))

# Write the cleaned data back to the CSV file
df.to_csv(file_path, index=False)
