import random
import string
import json
import csv
import sqlite3
from datetime import datetime

# Генерація випадкових даних

def generate_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_integer(min_val=0, max_val=100):
    return random.randint(min_val, max_val)


def generate_float(min_val=0.0, max_val=100.0):
    return round(random.uniform(min_val, max_val), 2)


def generate_date(start_year=2000, end_year=2024):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    return start_date + (end_date - start_date) * random.random()


def generate_record():
    return {
        "id": generate_integer(1, 10000),
        "name": generate_string(8),
        "email": f"{generate_string(5)}@example.com",
        "age": generate_integer(18, 90),
        "balance": generate_float(100.0, 10000.0),
        "created_at": generate_date().strftime('%Y-%m-%d %H:%M:%S')
    }

# Збереження в різні формати

def save_to_json(data, filename="data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def save_to_csv(data, filename="data.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def save_to_sqlite(data, db_name="data.db", table_name="records"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER,
        name TEXT,
        email TEXT,
        age INTEGER,
        balance REAL,
        created_at TEXT
    )""")
    
    for record in data:
        cursor.execute(f"INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?, ?)",
                       (record["id"], record["name"], record["email"], record["age"], record["balance"], record["created_at"]))
    
    conn.commit()
    conn.close()

# Генерація та збереження даних
if __name__ == "__main__":
    num_records = 100
    generated_data = [generate_record() for _ in range(num_records)]
    
    save_to_json(generated_data)
    save_to_csv(generated_data)
    save_to_sqlite(generated_data)

    print("Дані збережено у файли JSON, CSV та базу даних SQLite.")
