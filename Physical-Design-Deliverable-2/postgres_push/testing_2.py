import pandas as pd

# Read the JSON file into a pandas DataFrame
# Define the path to the JSON file
file_path = 'C:/Users/yfmad/Fundamentals-of-Data-Science/Physical-Design-Deliverable-2/assets/game/vgsales.csv'
df = pd.read_csv(file_path)

# Identify duplicate rows
duplicate_rows = df[df.duplicated(subset=['Name', 'Platform', 'Year'], keep=False)]

# Print the duplicate rows
print(duplicate_rows)