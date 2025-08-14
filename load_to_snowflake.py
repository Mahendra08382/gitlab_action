import os
import snowflake.connector
import pandas as pd

# Read credentials from environment variables
conn = snowflake.connector.connect(
	user="MAHENDRA",
    password="Sr-Uh4YPYiY-2bd",
    account="yv62438.central-india.azure",
    warehouse="COMPUTE_WH",
    database="MY_WORK_DB",
    schema="PUBLIC"
)

# Example: Load CSV into a Snowflake table
file_path = "data.csv"
df = pd.read_csv(file_path)

# Create a cursor
cur = conn.cursor()

# Create table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS MY_TABLE (
    ID INT,
    NAME STRING
)
""")

# Insert data
for _, row in df.iterrows():
    cur.execute("INSERT INTO MY_TABLE (ID, NAME) VALUES (%s, %s)", (int(row.ID), row.NAME))

cur.close()
conn.close()

print("✅ Data loaded to Snowflake successfully")
