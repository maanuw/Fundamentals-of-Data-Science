import pandas as pd
import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="***")
cur = conn.cursor()

# Truncate the 'facts' table to delete all rows
cur.execute("TRUNCATE TABLE facts")

# Define the path to the CSV file
file_path = 'C:/Users/yfmad/Fundamentals-of-Data-Science/Physical-Design-Deliverable-2/assets/game/vgsales.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Iterate over each row in the dataframe and insert into the database
for index, row in df.iterrows():
    cur.execute("INSERT INTO facts (Name, Platform, Year, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, "
                "Other_Sales, Global_Sales) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                (row["Name"], row["Platform"], row["Year"], row["Genre"], row["Publisher"], row["NA_Sales"],
                 row["EU_Sales"], row["JP_Sales"], row["Other_Sales"], row["Global_Sales"]))

# Commit the changes to the database
conn.commit()

# Close the database connection
cur.close()
conn.close()
