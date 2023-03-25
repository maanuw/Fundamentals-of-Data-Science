import pandas as pd

# Define a function to extract the year from a date string
def extract_year(date_str):
    return str(date_str).split('-')[0]

# Read the JSON file into a pandas DataFrame
# Define the path to the JSON file
file_path = 'C:/Users/yfmad/Fundamentals-of-Data-Science/Physical-Design-Deliverable-2/assets/game/playtime.json'
df = pd.read_json(file_path)

# Extract year from the "Release-date" column
df['Year'] = df['Release_date'].apply(extract_year)

# Identify duplicate rows
duplicate_rows = df[df.duplicated(subset=['Name', 'Release_date'], keep=False)]

# Print the duplicate rows
print(duplicate_rows)



