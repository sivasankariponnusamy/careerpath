"""
Test script to verify local backend saves to database
This bypasses the frontend to test the backend directly
"""

import requests
import os

print("\n🧪 Testing Local Backend Database Storage...\n")

# Test file path
test_file = os.path.join(os.path.dirname(__file__), '..', 'dataset', 'sample_resume.txt')

# Create a simple test resume if it doesn't exist
if not os.path.exists(test_file):
    test_content = """
    John Doe
    Software Developer
    
    Skills: Python, JavaScript, React, Node.js, Docker, PostgreSQL, Git, AWS
    
    Experience:
    - Full Stack Developer at Tech Corp
    - Built web applications using React and Node.js
    - Deployed applications on AWS
    
    Education:
    - BS Computer Science
    """
    os.makedirs(os.path.dirname(test_file), exist_ok=True)
    with open(test_file, 'w') as f:
        f.write(test_content)
    print(f"✓ Created test resume: {test_file}")

# Test the backend
print("Testing http://localhost:5000/api/extract-skills...")

try:
    # First check if backend is running
    health = requests.get("http://localhost:5000/api/health", timeout=3)
    if health.status_code == 200:
        print("✅ Backend is running")
    else:
        print("❌ Backend returned status:", health.status_code)
        exit(1)
        
except requests.exceptions.ConnectionError:
    print("❌ Backend is NOT running!")
    print("\nStart it with: cd backend && python main.py")
    exit(1)

# Upload test resume
print("\nUploading test resume...")
with open(test_file, 'rb') as f:
    files = {'resume': ('test_resume.txt', f, 'text/plain')}
    response = requests.post(
        "http://localhost:5000/api/extract-skills",
        files=files,
        timeout=10
    )

if response.status_code == 200:
    data = response.json()
    print("\n✅ SUCCESS! Backend responded:")
    print(f"   - Skills found: {data.get('count', 0)}")
    print(f"   - Resume ID: {data.get('resume_id', 'None')}")
    print(f"   - Saved to database: {data.get('saved_to_database', False)}")
    
    if data.get('saved_to_database'):
        print("\n🎉 DATABASE STORAGE WORKING!")
        print(f"   Resume saved with ID: {data.get('resume_id')}")
    else:
        print("\n❌ Database storage FAILED")
        print("   Check backend terminal for errors")
else:
    print(f"\n❌ Upload failed with status {response.status_code}")
    print(response.text)

print("\n" + "="*60)
print("Now check database:")
print("  cd backend && python test_database.py")
print("="*60 + "\n")
