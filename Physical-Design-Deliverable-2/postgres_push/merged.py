import pandas as pd
import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="password125")
cur = conn.cursor()

# Define the path to the CSV file
file_path = 'C:/Users/yfmad/Fundamentals-of-Data-Science/Physical-Design-Deliverable-2/assets/game/Sales_fact.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Iterate over each row in the dataframe and insert into the database
for index, row in df.iterrows():
    # Check if a row with the same primary key already exists
    cur.execute("SELECT COUNT(*) FROM merged WHERE Name = %s AND Platform = %s AND Year = %s AND Publisher = %s",
                (row["Name"], row["Platform"], row["Year"], row["Publisher"]))
    if cur.fetchone()[0] == 0:
        # Insert a new row if a row with the same primary key does not already exist
        cur.execute("INSERT INTO merged (Name, Platform, Year, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, "
                    "Other_Sales, Global_Sales) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                    (row["Name"], row["Platform"], row["Year"], row["Genre"], row["Publisher"], row["NA_Sales"],
                     row["EU_Sales"], row["JP_Sales"], row["Other_Sales"], row["Global_Sales"]))

# Commit the changes to the database
conn.commit()

# Close the database connection
cur.close()
conn.close()
