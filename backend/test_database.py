"""
Test script to verify database storage is working
Run this after uploading a file to check if it's saved
"""

import os
import sys

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from models import db, Resume
    from main import app
    
    with app.app_context():
        # Test database connection
        print("\n🔍 Testing Database Connection...")
        print(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
        
        # Count total resumes
        total_resumes = Resume.query.count()
        print(f"\n✅ Database connected successfully!")
        print(f"📊 Total resumes in database: {total_resumes}")
        
        if total_resumes == 0:
            print("\n⚠️  No resumes found yet.")
            print("   Upload a resume through the frontend to test storage.")
        else:
            print(f"\n📋 Last {min(5, total_resumes)} uploaded resume(s):\n")
            recent_resumes = Resume.query.order_by(Resume.upload_date.desc()).limit(5).all()
            
            for i, resume in enumerate(recent_resumes, 1):
                import json
                skills = json.loads(resume.extracted_skills) if resume.extracted_skills else []
                print(f"{i}. {resume.filename}")
                print(f"   ├─ Uploaded: {resume.upload_date}")
                print(f"   ├─ Skills: {len(skills)} found")
                print(f"   └─ Top Match: {resume.top_match_role} ({resume.top_match_percentage:.1f}%)")
                print()
                
        print("✅ Test completed successfully!\n")
        
except ImportError as e:
    print(f"\n❌ Import Error: {e}")
    print("Make sure you're in the backend directory and dependencies are installed.")
except Exception as e:
    print(f"\n❌ Database Error: {e}")
    print("The database might not be initialized yet.")
    print("\nTo fix this:")
    print("1. cd backend")
    print("2. python main.py")
    print("   (This will create the database)")
    print("3. Upload a resume through the frontend")
    print("4. Run this script again")
