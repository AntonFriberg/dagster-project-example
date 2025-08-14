import sqlite3

DB_NAME = "etl_data.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS catalogs (
            catalog_id INTEGER PRIMARY KEY,
            name TEXT,
            created_at TEXT,
            updated_at TEXT
        )
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            name TEXT,
            price REAL,
            catalog_id INTEGER,
            created_at TEXT,
            updated_at TEXT,
            FOREIGN KEY (catalog_id) REFERENCES catalogs (catalog_id)
        )
        """)
        conn.commit()