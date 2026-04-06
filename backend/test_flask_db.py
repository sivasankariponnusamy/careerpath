"""Test Flask app with new database"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from main import app, db, Resume
from datetime import datetime

try:
    print("Initializing Flask app with new database...")
    with app.app_context():
        print("✓ App context created")
        
        print("Adding resume to database...")
        new_resume = Resume(
            filename="test_flask_resume.pdf",
            file_type="application/pdf",
            file_size=12345,
            extracted_skills='["Python", "Flask", "SQL"]',
            categorized_skills='{"Programming": ["Python", "Flask"], "Database": ["SQL"]}',
            suggested_roles='["Backend Developer", "Full Stack Developer"]',
            top_match_role="Backend Developer",
            top_match_percentage=95.5,
            upload_date=datetime.utcnow()
        )
        
        db.session.add(new_resume)
        print("Committing to database...")
        db.session.commit()
        
        print(f"✓ Resume saved with ID: {new_resume.id}")
        
        # Verify
        print("Verifying save...")
        all_resumes = Resume.query.all()
        print(f"✓ Total resumes in database: {len(all_resumes)}")
        for resume in all_resumes:
            print(f"  - ID {resume.id}: {resume.filename} ({resume.top_match_role})")
        
        print("\n✓✓✓ Flask database test SUCCESSFUL!")
        
except Exception as e:
    print(f"❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
