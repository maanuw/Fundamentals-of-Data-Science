import pandas as pd

# Read the CSV file into a pandas DataFrame
file_path = 'C:/Users/yfmad/Fundamentals-of-Data-Science/Physical-Design-Deliverable-2/assets/game/Sales_fact.csv'
df = pd.read_csv(file_path)

# Identify duplicate rows
duplicate_rows = df[df.duplicated(subset=['Name', 'Platform', 'Year', 'Publisher'], keep=False)]

# Print the Name and Release_date columns for the duplicate rows
print(duplicate_rows.loc[:, ['Name', 'Platform', 'Year', 'Publisher']])

# Print the number of duplicates
print("Number of duplicates:", len(duplicate_rows))
