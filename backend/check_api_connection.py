"""
Check which API URL the application is currently using
Run this to debug connection issues
"""

import requests

print("\n🔍 Checking API Connections...\n")

# Check local backend
print("1. Testing LOCAL backend (http://localhost:5000)...")
try:
    response = requests.get("http://localhost:5000/api/health", timeout=3)
    if response.status_code == 200:
        data = response.json()
        print(f"   ✅ LOCAL backend is RUNNING")
        print(f"      Status: {data.get('status')}")
        print(f"      Message: {data.get('message')}")
    else:
        print(f"   ❌ LOCAL backend returned status {response.status_code}")
except requests.exceptions.ConnectionError:
    print("   ❌ LOCAL backend is NOT RUNNING")
    print("      Run: cd backend && python main.py")
except Exception as e:
    print(f"   ❌ Error: {e}")

print()

# Check Vercel backend
print("2. Testing VERCEL backend (https://backend-careerpath-ai.vercel.app)...")
try:
    response = requests.get("https://backend-careerpath-ai.vercel.app/api/health", timeout=5)
    if response.status_code == 200:
        data = response.json()
        print(f"   ✅ VERCEL backend is accessible")
        print(f"      Status: {data.get('status')}")
    else:
        print(f"   ⚠️  VERCEL backend returned status {response.status_code}")
except Exception as e:
    print(f"   ⚠️  VERCEL backend: {e}")

print()
print("=" * 60)
print()

# Determine which backend should be used
import os

# Check if frontend .env.local exists
env_file = os.path.join(os.path.dirname(__file__), '..', 'frontend', '.env.local')
if os.path.exists(env_file):
    print("✅ frontend/.env.local EXISTS")
    with open(env_file, 'r') as f:
        content = f.read()
        print(f"\nContent:\n{content}")
        
    if "localhost:5000" in content:
        print("\n✅ CORRECTLY configured to use LOCAL backend")
        print("\n⚠️  If uploads still don't save locally:")
        print("   1. RESTART the frontend dev server")
        print("   2. Run: .\\restart-frontend.ps1")
        print("   3. Or manually: Ctrl+C in frontend terminal, then npm run dev")
        print("   4. Refresh browser (Ctrl+F5)")
    elif "vercel" in content.lower():
        print("\n❌ Currently configured to use VERCEL backend")
        print("\n   To use local backend, update frontend/.env.local:")
        print("   VITE_API_URL=http://localhost:5000/api")
else:
    print("❌ frontend/.env.local DOES NOT EXIST")
    print("\n   Creating it now...")
    os.makedirs(os.path.dirname(env_file), exist_ok=True)
    with open(env_file, 'w') as f:
        f.write("# Local Development Configuration\n")
        f.write("VITE_API_URL=http://localhost:5000/api\n")
    print("   ✅ Created!")
    print("\n   ⚠️  You MUST restart the frontend dev server:")
    print("   1. Stop frontend (Ctrl+C)")
    print("   2. Run: cd frontend && npm run dev")
    print("   3. Or run: .\\restart-frontend.ps1")

print()
print("=" * 60)
print()
print("💡 Quick Fix:")
print("   Run: .\\restart-frontend.ps1")
print("   Then upload a resume and check: python backend/test_database.py")
print()
