import pandas as pd
import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="password125")
cur = conn.cursor()

# Define the path to the CSV file
file_path = 'C:/Users/yfmad/Fundamentals-of-Data-Science/Physical-Design-Deliverable-2/assets/game/game_dimension.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Iterate over each row in the dataframe and insert into the database
for index, row in df.iterrows():
    cur.execute("INSERT INTO games (Name, Release_date, Genres, Review_scor, SinglePlayer_All_PlayStyles_Polled, "
                "SinglePlayer_All_PlayStyles_Median, SinglePlayer_All_PlayStyles_Rushed, "
                "SinglePlayer_All_PlayStyles_Leisure) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",
                (row["Name"], row["Release_date"], row["Genres"], row["Review_score"],
                 row["SinglePlayer_All_PlayStyles_Polled"], row["SinglePlayer_All_PlayStyles_Median"],
                 row["SinglePlayer_All_PlayStyles_Rushed"], row["SinglePlayer_All_PlayStyles_Leisure"]))


# Commit the changes to the database
conn.commit()

# Close the database connection
cur.close()
conn.close()