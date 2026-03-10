import sqlite3

conn = sqlite3.connect("monitoring.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    message TEXT,
    prediction TEXT,
    confidence REAL,
    latency REAL
)
""")

conn.commit()
conn.close()

print("Database initialized successfully")