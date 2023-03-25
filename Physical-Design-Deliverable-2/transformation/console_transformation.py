import pandas as pd
import numpy as np

# Define the path to the CSV file
file_path = 'C:/Users/yfmad/Fundamentals-of-Data-Science/Physical-Design-Deliverable-2/assets/console/console.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Cleaning Release_Year column

# Calculate the average value of the "Release_Year" column
avg_release_year = df['Release_Year'].mean()

# Replace any release year value that is inferior to 1940 and superior to 2023 with the average value of the column
df.loc[df['Release_Year'] < 1940, 'Release_Year'] = avg_release_year
df.loc[df['Release_Year'] > 2023, 'Release_Year'] = avg_release_year

# Replace any empty or missing release year value with the average value of the column
df['Release_Year'] = df['Release_Year'].replace('', np.nan)
df['Release_Year'] = df['Release_Year'].fillna(avg_release_year)

# Convert Release_Year column to integer values
df['Release_Year'] = df['Release_Year'].astype(int)

# Cleaning Sales column

# Calculate the average value of the "Sales" column
avg_sales_year = df['Sales'].mean()

# Replace any sales value that is inferior to 0 with the average value of the column
df.loc[df['Sales'] < 0, 'Sales'] = avg_sales_year

# Convert Sales column to integer values
df['Sales'] = df['Sales'].astype(int)

# Write the cleaned data back to the CSV file
df.to_csv(file_path, index=False)


