"""View all resumes in the new database"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from main import app, Resume

with app.app_context():
    resumes = Resume.query.order_by(Resume.upload_date.desc()).all()
    
    print(f"\n📊 Total resumes in database: {len(resumes)}\n")
    
    for resume in resumes:
        print(f"{'='*60}")
        print(f"Resume ID: {resume.id}")
        print(f"Filename: {resume.filename}")
        print(f"File Type: {resume.file_type}")
        print(f"File Size: {resume.file_size} bytes")
        print(f"Upload Date: {resume.upload_date}")
        print(f"Top Role: {resume.top_match_role}")
        print(f"Match: {resume.top_match_percentage}%")
        print(f"Skills: {resume.extracted_skills[:100]}...")  # First 100 chars
        print()
