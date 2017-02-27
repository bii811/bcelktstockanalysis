import sqlite3
import os
import csv

database = os.path.join(os.path.dirname(__file__), "../mining/db/bcelktstockanalysis.db")

with sqlite3.connect(database) as conn:
    c = conn.cursor()
    c.execute("SELECT * FROM stock_daily_log")
    data = c.fetchall()

with open('data/data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
