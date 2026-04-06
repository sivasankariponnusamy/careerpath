"""List all resumes in database to find Surya-Resume-1.pdf"""
import sqlite3
import json

conn = sqlite3.connect('careerpath_new.db')
cursor = conn.cursor()

cursor.execute("""
    SELECT id, filename, top_match_role, top_match_percentage, upload_date
    FROM resumes 
    ORDER BY upload_date DESC
""")

resumes = cursor.fetchall()
print(f"\n{'='*80}")
print(f"ALL RESUMES IN DATABASE ({len(resumes)} total)")
print(f"{'='*80}\n")

for resume in resumes:
    print(f"ID: {resume[0]}")
    print(f"Filename: {resume[1]}")
    print(f"Prediction: {resume[2]} ({resume[3]}%)")
    print(f"Upload Date: {resume[4]}")
    print(f"-" * 80)

# Now search specifically for Surya resume
print(f"\n{'='*80}")
print(f"SEARCHING FOR SURYA RESUME")
print(f"{'='*80}\n")

cursor.execute("""
    SELECT id, filename, top_match_role, top_match_percentage, 
           extracted_skills, suggested_roles
    FROM resumes 
    WHERE filename LIKE '%Surya%' OR filename LIKE '%surya%'
""")

surya_resume = cursor.fetchone()
if surya_resume:
    print(f"✓ Found Surya resume!")
    print(f"Resume ID: {surya_resume[0]}")
    print(f"Filename: {surya_resume[1]}")
    print(f"Top Match: {surya_resume[2]} ({surya_resume[3]}%)")
    print(f"\nAll Suggested Roles:")
    suggested = json.loads(surya_resume[5])
    for role in suggested:
        print(f"  - {role['role']}: {role['match_percentage']}% ({role['confidence']})")
    print(f"\nExtracted Skills:")
    skills = json.loads(surya_resume[4])
    print(f"  {', '.join(skills[:20])}")
    if len(skills) > 20:
        print(f"  ... and {len(skills) - 20} more")
else:
    print("❌ No Surya resume found in database")

conn.close()
