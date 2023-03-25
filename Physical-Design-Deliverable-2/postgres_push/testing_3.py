import pandas as pd

# Read the CSV file into a pandas DataFrame
file_path = 'C:/Users/yfmad/Fundamentals-of-Data-Science/Physical-Design-Deliverable-2/assets/game/game_dimension.csv'
df = pd.read_csv(file_path)

# Identify duplicate rows
duplicate_rows = df[df.duplicated(subset=['Name', 'Release_date'], keep=False)]

# Print the Name and Release_date columns for the duplicate rows
print(duplicate_rows.loc[:, ['Name', 'Release_date']])
