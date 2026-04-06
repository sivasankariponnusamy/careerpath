"""
Script to view all stored resumes in the database
Run this to check if uploaded resumes are being saved properly
"""

import sys
import os
from datetime import datetime

# Add the backend directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    # Try importing from main.py (local development)
    from models import db, Resume
    from main import app
    
    with app.app_context():
        resumes = Resume.query.order_by(Resume.upload_date.desc()).all()
        
        if not resumes:
            print("\n❌ No resumes found in database!")
            print("\nPossible reasons:")
            print("1. No files have been uploaded yet")
            print("2. Database file doesn't exist")
            print("3. Upload endpoint is not saving to database")
        else:
            print(f"\n✅ Found {len(resumes)} resume(s) in database:\n")
            print("=" * 100)
            
            for i, resume in enumerate(resumes, 1):
                print(f"\n{i}. Resume ID: {resume.id}")
                print(f"   Filename: {resume.filename}")
                print(f"   File Type: {resume.file_type}")
                print(f"   File Size: {resume.file_size:,} bytes")
                print(f"   Upload Date: {resume.upload_date}")
                print(f"   Processed: {'✓' if resume.processed else '✗'}")
                
                if resume.extracted_skills:
                    import json
                    skills = json.loads(resume.extracted_skills)
                    print(f"   Skills Found: {len(skills)}")
                    print(f"   Skills: {', '.join(skills[:10])}{'...' if len(skills) > 10 else ''}")
                
                if resume.top_match_role:
                    print(f"   Top Match: {resume.top_match_role} ({resume.top_match_percentage:.1f}%)")
                
                print("-" * 100)
                
except Exception as e:
    print(f"\n❌ Error: {str(e)}")
    print("\nMake sure you're running this from the backend directory")
    print("and that the database file exists.")
