import sqlite3
import pandas as pd
import time

DB_FILE = "monitoring.db"
CSV_FILE = "predictions.csv"

while True:
    try:
        conn = sqlite3.connect(DB_FILE)

        df = pd.read_sql_query("SELECT * FROM predictions", conn)

        df.to_csv(CSV_FILE, index=False)

        conn.close()

        print("CSV updated. Rows:", len(df))

    except Exception as e:
        print("Error:", e)

    time.sleep(5)