import sqlite3
import pandas as pd

# Load CSV file into a DataFrame
dataframe = pd.read_csv('C:/Users/Compu Srore/projectllm/database.csv')
print(dataframe.columns)

# Connect to SQLite
connection = sqlite3.connect("earthquake.db")

# Create a cursor object to create the table and insert records
cursor = connection.cursor()

# Create the table
table_info = """
CREATE TABLE IF NOT EXISTS EARTHQUAKES (
    LAT VARCHAR(25), 
    LONG VARCHAR(25),
    TYPE VARCHAR(50), 
    MAG VARCHAR(25)
);
"""
cursor.execute(table_info)

# Insert records from DataFrame into the database
for index, row in dataframe.iterrows():
    cursor.execute("""
    INSERT INTO EARTHQUAKES (LAT, LONG, TYPE, MAG) 
    VALUES (?, ?, ?, ?)""",
    (row['Latitude'], row['Longitude'], row['Type'], row['Magnitude']))

# Display all the records
print("The inserted records are:")
data = cursor.execute('SELECT * FROM EARTHQUAKES')
for row in data:
    print(row)

# Commit your changes in the database and close the connection
connection.commit()
connection.close()
