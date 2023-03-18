import pandas as pd
import numpy as np

# Define the path to the CSV file
file_path = 'C:/Users/yfmad/Fundamentals-of-Data-Science/Physical-Design-Deliverable-2/assets/game/imdb-videogames.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Replace any missing or blank values in the "certificate" column with "M"
df['certificate'] = df['certificate'].fillna('M')

# Cleaning rating column

# Calculate the average value of the "rating" column
avg_rating = df['rating'].mean()

# Replace any rating value that is inferior to 0 and superior to 10 with the average value of the column and assign
# the mean value of the ratings to the cell if the cell is currently empty
df['rating'] = df['rating'].replace('', np.nan)
df['rating'] = df['rating'].fillna(avg_rating)
df.loc[df['rating'] < 0, 'rating'] = avg_rating
df.loc[df['rating'] > 10, 'rating'] = avg_rating

# Cleaning votes column

# Convert "votes" column to numeric data type
df['votes'] = pd.to_numeric(df['votes'], errors='coerce')

# Calculate the average value of the "votes" column
avg_votes = df['votes'].mean()

# Replace any rating value that is inferior to 0 and superior to 10 with the average value of the column and assign
# the mean value of the ratings to the cell if the cell is currently empty
df['votes'] = df['votes'].replace('', np.nan)
df['votes'] = df['votes'].fillna(avg_votes)
df.loc[df['votes'] < 0, 'votes'] = avg_votes

# Cleaning data for Adventure, Comedy, Crime, Family, Fantasy, Mystery, Sci-Fi, Thriller
df['Adventure'] = df['Adventure'].fillna(False)
df['Comedy'] = df['Comedy'].fillna(False)
df['Crime'] = df['Crime'].fillna(False)
df['Family'] = df['Family'].fillna(False)
df['Fantasy'] = df['Fantasy'].fillna(False)
df['Mystery'] = df['Mystery'].fillna(False)
df['Sci-Fi'] = df['Sci-Fi'].fillna(False)
df['Thriller'] = df['Thriller'].fillna(False)

# Replace any non-True/False values in Adventure, Comedy, Crime, Family, Fantasy, Mystery, Sci-Fi, Thriller column
# with False
df['Adventure'] = df['Adventure'].replace(['TRUE', 'FALSE'], [True, False])
df['Adventure'] = df['Adventure'].replace(to_replace='.*', value=False, regex=True)
df['Comedy'] = df['Comedy'].replace(['TRUE', 'FALSE'], [True, False])
df['Comedy'] = df['Comedy'].replace(to_replace='.*', value=False, regex=True)
df['Crime'] = df['Crime'].replace(['TRUE', 'FALSE'], [True, False])
df['Crime'] = df['Crime'].replace(to_replace='.*', value=False, regex=True)
df['Family'] = df['Family'].replace(['TRUE', 'FALSE'], [True, False])
df['Family'] = df['Family'].replace(to_replace='.*', value=False, regex=True)
df['Fantasy'] = df['Fantasy'].replace(['TRUE', 'FALSE'], [True, False])
df['Fantasy'] = df['Fantasy'].replace(to_replace='.*', value=False, regex=True)
df['Mystery'] = df['Mystery'].replace(['TRUE', 'FALSE'], [True, False])
df['Mystery'] = df['Mystery'].replace(to_replace='.*', value=False, regex=True)
df['Sci-Fi'] = df['Sci-Fi'].replace(['TRUE', 'FALSE'], [True, False])
df['Sci-Fi'] = df['Sci-Fi'].replace(to_replace='.*', value=False, regex=True)
df['Thriller'] = df['Thriller'].replace(['TRUE', 'FALSE'], [True, False])
df['Thriller'] = df['Thriller'].replace(to_replace='.*', value=False, regex=True)

# Write the cleaned data back to the CSV file
df.to_csv(file_path, index=False)