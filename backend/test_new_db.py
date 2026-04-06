"""Test with completely new database file"""
import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'careerpath_new.db')

# Remove old database if exists
if os.path.exists(db_path):
    try:
        os.remove(db_path)
        print(f"✓ Removed old database")
    except Exception as e:
        print(f"❌ Could not remove old database: {e}")
        exit(1)

try:
    print("Creating new database connection...")
    conn = sqlite3.connect(db_path, timeout=30)
    cursor = conn.cursor()
    
    print("Setting SQLite pragmas...")
    cursor.execute("PRAGMA journal_mode=WAL")
    cursor.execute("PRAGMA busy_timeout=30000")
    print(f"✓ Journal mode: {cursor.fetchone()[0]}")
    
    print("Creating table...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    print("Inserting test record...")
    cursor.execute("INSERT INTO resumes (filename) VALUES (?)", ("test_resume.pdf",))
    
    print("Committing transaction...")
    conn.commit()
    
    print("Reading back data...")
    cursor.execute("SELECT * FROM resumes")
    rows = cursor.fetchall()
    print(f"✓ SUCCESS! Found {len(rows)} rows: {rows}")
    
    conn.close()
    print("✓ Database connection closed successfully")
    print(f"\n✓✓✓ Database working! File: {db_path}")
    
except Exception as e:
    print(f"❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
