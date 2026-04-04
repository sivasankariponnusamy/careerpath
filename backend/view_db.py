import sqlite3
import json

# Connect to database
conn = sqlite3.connect('career_path.db')
cursor = conn.cursor()

print("=" * 60)
print("DATABASE TABLES")
print("=" * 60)
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
for table in tables:
    print(f"  • {table[0]}")

print("\n" + "=" * 60)
print("RESUMES TABLE")
print("=" * 60)
cursor.execute("SELECT id, filename, file_type, top_match_role, top_match_percentage, upload_date FROM resumes")
resumes = cursor.fetchall()

if resumes:
    for resume in resumes:
        print(f"""
ID: {resume[0]}
Filename: {resume[1]}
File Type: {resume[2]}
Top Match Role: {resume[3]}
Match Percentage: {resume[4]}%
Upload Date: {resume[5]}
{'-' * 60}""")
else:
    print("No resumes found in database.")

print("\n" + "=" * 60)
print("RESUME DETAILS (ID 1)")
print("=" * 60)
cursor.execute("SELECT * FROM resumes WHERE id=1")
columns = [description[0] for description in cursor.description]
row = cursor.fetchone()

if row:
    for i, col in enumerate(columns):
        value = row[i]
        # Format JSON fields nicely
        if col in ['extracted_skills', 'categorized_skills', 'suggested_roles']:
            try:
                value = json.loads(value) if value else None
                if col == 'extracted_skills':
                    print(f"\n{col}:")
                    print(f"  {', '.join(value) if value else 'None'}")
                elif col == 'categorized_skills':
                    print(f"\n{col}:")
                    if value:
                        for category, skills in value.items():
                            print(f"  {category}: {', '.join(skills)}")
                elif col == 'suggested_roles':
                    print(f"\n{col}:")
                    if value:
                        for role in value:
                            print(f"  • {role['role']}: {role['match_percentage']}% ({role['confidence']})")
            except:
                print(f"{col}: {value}")
        elif col == 'text_content':
            # Truncate long text
            print(f"{col}: {value[:100] if value else 'None'}...")
        else:
            print(f"{col}: {value}")
else:
    print("No resume found with ID 1")

print("\n" + "=" * 60)
print("DATABASE STATISTICS")
print("=" * 60)
cursor.execute("SELECT COUNT(*) FROM resumes")
total_resumes = cursor.fetchone()[0]
print(f"Total Resumes: {total_resumes}")

cursor.execute("SELECT COUNT(*) FROM skill_gap_analyses")
total_analyses = cursor.fetchone()[0]
print(f"Total Skill Gap Analyses: {total_analyses}")

conn.close()
print("\n✓ Database query complete!")
