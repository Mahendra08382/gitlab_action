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

cur = conn.cursor()

try: 
    # Create table if not exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS MY_TABLE (
            ID INT,
            NAME STRING
        )
    """)

    # Dummy hardcoded values
    data = [
        (1, "Alice"),
        (2, "Bob"),
        (3, "Charlie"),
        (4, "David")
    ]

    # Insert each row into the table
    for row in data:
        cur.execute("INSERT INTO MY_TABLE (ID, NAME) VALUES (%s, %s)", row)

    print("✅ Dummy data loaded successfully into MY_TABLE")

finally:
    cur.close()
    conn.close()