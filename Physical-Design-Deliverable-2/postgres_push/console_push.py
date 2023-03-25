import pandas as pd
import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="password125")
cur = conn.cursor()

# Define the path to the CSV file
file_path = 'C:/Users/yfmad/Fundamentals-of-Data-Science/Physical-Design-Deliverable-2/assets/console/console.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Iterate over each row in the dataframe and insert into the database
for index, row in df.iterrows():
    cur.execute("INSERT INTO Consoles (ConsoleID, Console_Name, Manufacturer, Release_Year, Sales, Type) "
                "VALUES (%s, %s, %s, %s, %s, %s);",
                (row["ConsoleID"], row["Console_Name"], row["Manufacturer"], row["Release_Year"], row["Sales"],
                 row["Type"]))

# Commit the changes to the database
conn.commit()

# Close the database connection
cur.close()
conn.close()