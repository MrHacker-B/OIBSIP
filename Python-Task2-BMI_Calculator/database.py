import sqlite3


def create_database():
    conn = sqlite3.connect("bmi_records.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bmi_records(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        weight REAL,
        height REAL,
        bmi REAL,
        category TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_record(name, weight, height, bmi, category):
    conn = sqlite3.connect("bmi_records.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO bmi_records(name, weight, height, bmi, category)
    VALUES (?, ?, ?, ?, ?)
    """, (name, weight, height, bmi, category))

    conn.commit()
    conn.close()


def fetch_records(name):
    conn = sqlite3.connect("bmi_records.db")
    cursor = conn.cursor()

    cursor.execute(""" SELECT bmi,category FROM bmi_records WHERE name=? ORDER BY id """, (name,))

    records = cursor.fetchall()

    conn.close()

    return records