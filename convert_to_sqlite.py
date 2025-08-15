import csv
import sqlite3
import sys
import os

def csv_to_sqlite(csv_file, db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        columns = ', '.join([f'"{header}" TEXT' for header in headers])
        cursor.execute(f'CREATE TABLE IF NOT EXISTS data ({columns})')

        for row in reader:
            placeholders = ', '.join(['?'] * len(row))
            cursor.execute(f'INSERT INTO data VALUES ({placeholders})', row)

    conn.commit()
    conn.close()
    print(f'✅ Database "{db_name}" created.')

def preview_data(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM data LIMIT 5')
    rows = cursor.fetchall()
    print("\n📊 Preview (first 5 rows):")
    for row in rows:
        print(row)
    conn.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python convert_to_sqlite.py sample.csv output.db [--preview]")
    else:
        csv_to_sqlite(sys.argv[1], sys.argv[2])
        if len(sys.argv) == 4 and sys.argv[3] == "--preview":
            preview_data(sys.argv[2])
