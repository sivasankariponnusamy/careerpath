"""
Direct database test - bypasses HTTP to test database save directly
"""

import sys
import os
import json
from datetime import datetime

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models import db, Resume
from main import app

print("\n🔬 Direct Database Save Test...\n")

with app.app_context():
    # Create a test resume directly
    test_resume = Resume(
        filename="DIRECT_TEST.txt",
        file_path="/test/path.txt",
        file_type="txt",
        file_size=100,
        text_content="Test content",
        extracted_skills=json.dumps(["Python", "JavaScript", "React"]),
        categorized_skills=json.dumps({"Programming Languages": ["Python", "JavaScript"]}),
        suggested_roles=json.dumps([{"role": "Full Stack Developer", "match_percentage": 85}]),
        top_match_role="Full Stack Developer",
        top_match_percentage=85.0,
        processed=True,
        upload_date=datetime.utcnow()
    )
    
    try:
        print("Adding resume to database...")
        db.session.add(test_resume)
        db.session.commit()
        
        print(f"✅ SUCCESS! Resume saved with ID: {test_resume.id}")
        print("\nVerifying...")
        
        # Verify it was saved
        saved_resume = Resume.query.get(test_resume.id)
        if saved_resume:
            print(f"✅ VERIFIED! Resume ID {saved_resume.id} found in database")
            print(f"   Filename: {saved_resume.filename}")
            print(f"   Top Match: {saved_resume.top_match_role}")
            
            # Count total
            total = Resume.query.count()
            print(f"\n📊 Total resumes in database: {total}")
            
            print("\n🎉 DATABASE SAVE IS WORKING!")
        else:
            print("❌ Could not find saved resume")
            
    except Exception as e:
        print(f"❌ ERROR saving to database: {e}")
        db.session.rollback()
        
print()
