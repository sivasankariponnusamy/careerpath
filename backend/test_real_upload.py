"""Test actual HTTP upload to verify database saves work"""
import requests
import os

API_URL = "http://localhost:5000/api"

# Create a simple test resume file content
test_resume_content = """
John Doe
Senior Software Engineer

SKILLS:
- Python (5 years)
- JavaScript (4 years)
- React (3 years)
- Node.js (3 years)
- SQL (5 years)
- Docker (2 years)
- AWS (2 years)

EXPERIENCE:
Senior Developer at Tech Corp
- Built web applications using Python and React
- Managed cloud infrastructure on AWS
- Led team of 5 developers
"""

# Create a temporary test file
test_file_path = "test_resume_john_doe.txt"
with open(test_file_path, 'w') as f:
    f.write(test_resume_content)

try:
    print(f"📤 Uploading test resume to {API_URL}/extract-skills...")
    
    with open(test_file_path, 'rb') as f:
        files = {'resume': (test_file_path, f, 'text/plain')}  # Changed from 'file' to 'resume'
        response = requests.post(
            f"{API_URL}/extract-skills",
            files=files,
            timeout=30
        )
    
    print(f"\n✓ Response Status: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"\n📊 Response Data:")
        print(f"  - Resume ID: {data.get('resume_id')}")
        print(f"  - Saved to DB: {data.get('saved_to_database')}")
        print(f"  - Skills Found: {len(data.get('skills', []))}")
        print(f"  - Top Role: {data.get('top_role')}")
        print(f"  - Match %: {data.get('match_percentage')}%")
        
        if data.get('saved_to_database') and data.get('resume_id'):
            print(f"\n✅✅✅ SUCCESS! Resume saved to database with ID: {data.get('resume_id')}")
        else:
            print(f"\n❌ FAILED: Resume not saved to database")
            print(f"Full response: {data}")
    else:
        print(f"\n❌ ERROR: {response.status_code}")
        print(response.text)
        
finally:
    # Cleanup
    if os.path.exists(test_file_path):
        os.remove(test_file_path)
        print(f"\n🧹 Cleaned up test file")
