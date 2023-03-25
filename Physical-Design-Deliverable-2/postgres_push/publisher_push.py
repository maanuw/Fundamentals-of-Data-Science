import pandas as pd
import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="password125")
cur = conn.cursor()

# Define the path to the CSV file
file_path = 'C:/Users/yfmad/Fundamentals-of-Data-Science/Physical-Design-Deliverable-2/assets/publisher/Publisher-T.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Get the number of rows in the dataframe
num_rows = df.shape[0]
print(f"Total number of rows in the dataframe: {num_rows}")

# Iterate over each row in the dataframe and insert into the database
for index, row in df.iterrows():
    cur.execute("INSERT INTO publisher (Name, Classification, Released_games, Unreleased_games, Total_revenue, "
                "Avg_revenue_per_game, Med_revenue_per_game, Percent_developed_in_house, Percent_indie_releases, "
                "Action, Casual, Adventure, Simulation, Strategy, RPG, MMO, Racing, Sports) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                (row["Name"], row["Classification"], row["Released_games"], row["Unreleased_games"], row["Total_revenue"],
                 row["Avg_revenue_per_game"], row["Med_revenue_per_game"], row["%_developed_in_house"],
                 row["%_indie_releases"], row["Action"], row["Casual"], row["Adventure"], row["Simaulation"],
                 row["Strategy"], row["RPG"], row["MMO"], row["Racing"], row["Sports"]))
    #print(f"Inserted row {index+1}/{num_rows} into the database")


# Commit the changes to the database
conn.commit()
print("Changes committed to the database")

# Close the database connection
cur.close()
conn.close()
print("Database connection closed")