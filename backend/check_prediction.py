"""Check what prediction the backend actually returns for latest resume"""
import sqlite3
import json
import os

# Connect to database
db_path = 'careerpath_new.db'  # Fixed: no underscore!
print(f"Checking database: {os.path.abspath(db_path)}")
print(f"Database exists: {os.path.exists(db_path)}")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# First check what tables exist
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print(f"\nTables in database: {[t[0] for t in tables]}")

# Get the most recent resume
cursor.execute("""
    SELECT id, filename, top_match_role, top_match_percentage, 
           extracted_skills, suggested_roles
    FROM resumes 
    ORDER BY upload_date DESC 
    LIMIT 1
""")

resume = cursor.fetchone()
if resume:
    print(f"\n{'='*60}")
    print(f"MOST RECENT UPLOAD IN DATABASE")
    print(f"{'='*60}")
    print(f"Resume ID: {resume[0]}")
    print(f"Filename: {resume[1]}")
    print(f"Top Match: {resume[2]} ({resume[3]}%)")
    print(f"\nAll Suggested Roles:")
    suggested = json.loads(resume[5])
    for role in suggested:
        print(f"  - {role['role']}: {role['match_percentage']}% ({role['confidence']})")
    
    print(f"\nExtracted Skills ({len(json.loads(resume[4]))} total):")
    skills = json.loads(resume[4])[:15]  # Show first 15
    print(f"  {', '.join(skills)}")
    if len(json.loads(resume[4])) > 15:
        print(f"  ... and {len(json.loads(resume[4])) - 15} more")
else:
    print("No resumes found in database")

conn.close()
