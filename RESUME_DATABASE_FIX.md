# Resume Upload Database Storage - Fix Documentation

## Problem Identified

The uploaded resume files were **NOT being stored in the database** because:

1. **Two Backend Implementations Exist:**
   - `backend/main.py` - Full Flask app with SQLAlchemy database (✅ has storage)
   - `backend/api/index.py` - Serverless function for Vercel (❌ didn't have storage)

2. **Vercel Deployment Uses Different Code:**
   - Your frontend calls: `https://backend-careerpath-ai.vercel.app/api/extract-skills`
   - This endpoint uses `backend/api/index.py` which had NO database code
   - The database code only existed in `backend/main.py` (not deployed to Vercel)

## Solution Applied

### 1. Added Flask-SQLAlchemy to Vercel API
**File:** `backend/api/requirements.txt`
```
flask-sqlalchemy==3.1.1  # Added
```

### 2. Added Database Models and Storage Logic
**File:** `backend/api/index.py`

- Added SQLAlchemy database configuration
- Created `Resume` database model 
- Modified `/api/extract-skills` endpoint to save uploads to database
- Added new endpoints:
  - `GET /api/resumes` - List all stored resumes
  - `GET /api/resumes/<id>` - Get specific resume by ID

### 3. Database Configuration
The system now supports:
- **Local Development:** SQLite database (`career_path.db`)
- **Production (Vercel):** PostgreSQL via `DATABASE_URL` environment variable

## What Gets Stored Now

Each uploaded resume stores:
- ✅ Filename, file type, file size
- ✅ Extracted text content (first 10,000 characters)
- ✅ All extracted skills (as JSON array)
- ✅ Categorized skills (Programming Languages, Web Tech, etc.)
- ✅ Suggested career roles with match percentages
- ✅ Top matching role and percentage
- ✅ Upload timestamp
- ✅ Processing status

## How to Verify the Fix

### Option 1: Check Locally (Before Deploying)

1. **Run the backend locally:**
   ```bash
   cd backend
   python main.py
   ```

2. **Upload a resume through your frontend** (change API URL to `http://localhost:5000`)

3. **View stored resumes:**
   ```bash
   python view_resumes.py
   ```

   Or query the database directly:
   ```bash
   python view_db.py
   ```

### Option 2: Check After Vercel Deployment

1. **Deploy the updated code to Vercel:**
   ```bash
   cd backend
   vercel --prod
   ```

2. **Set up PostgreSQL database on Vercel:**
   - Go to Vercel Dashboard → Your Project → Storage
   - Create a PostgreSQL database
   - Add `DATABASE_URL` environment variable (auto-configured)
   - Redeploy

3. **Upload a resume via your frontend**

4. **Check database using the API:**
   ```bash
   curl https://backend-careerpath-ai.vercel.app/api/resumes
   ```

### Option 3: Test API Response

When you upload a resume, the response now includes:
```json
{
  "resume_id": 1,
  "saved_to_database": true,
  "skills": [...],
  "categorized_skills": {...},
  ...
}
```

✅ If `saved_to_database: true`, it worked!
❌ If `saved_to_database: false`, check database connection

## Setting Up Database for Vercel

### Step 1: Add PostgreSQL Database
1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Select your project
3. Go to "Storage" tab
4. Click "Create Database" → Choose "PostgreSQL"
5. Follow the setup wizard

### Step 2: Configure Environment Variable
Vercel automatically sets `DATABASE_URL` for you. If not:

1. Go to Settings → Environment Variables
2. Add `DATABASE_URL` with your PostgreSQL connection string:
   ```
   postgresql://username:password@host:port/database
   ```

### Step 3: Redeploy
```bash
vercel --prod
```

The database tables will be created automatically on first run.

## New API Endpoints Available

### 1. Get All Resumes
```bash
GET /api/resumes
```

Response:
```json
{
  "resumes": [
    {
      "id": 1,
      "filename": "john_doe_resume.pdf",
      "extracted_skills": ["Python", "React", "AWS"],
      "top_match_role": "Full Stack Developer",
      "top_match_percentage": 85.5,
      "upload_date": "2026-04-07T10:30:00"
    }
  ],
  "count": 1
}
```

### 2. Get Specific Resume
```bash
GET /api/resumes/1
```

Response:
```json
{
  "resume": {
    "id": 1,
    "filename": "john_doe_resume.pdf",
    "file_type": "pdf",
    "file_size": 524288,
    "extracted_skills": ["Python", "JavaScript", "React", ...],
    "categorized_skills": {
      "Programming Languages": ["Python", "JavaScript"],
      "Web Technologies": ["React", "Node.js"]
    },
    "suggested_roles": [
      {"role": "Full Stack Developer", "match_percentage": 85.5}
    ],
    "top_match_role": "Full Stack Developer",
    "top_match_percentage": 85.5,
    "upload_date": "2026-04-07T10:30:00",
    "processed": true
  }
}
```

## Troubleshooting

### Database Not Saving Locally
```bash
# Check if database file exists
ls backend/career_path.db

# If not, run the app to create it
cd backend
python main.py
```

### Database Not Saving on Vercel
1. Check if `DATABASE_URL` environment variable is set
2. Check Vercel function logs: Dashboard → Your Project → Functions → View Logs
3. Ensure PostgreSQL database is created and connected
4. Redeploy after adding database

### View Database Contents
```bash
# Local
cd backend
python view_resumes.py

# Vercel (via API)
curl https://backend-careerpath-ai.vercel.app/api/resumes
```

## Files Changed

1. ✏️ `backend/api/index.py` - Added database models and storage logic
2. ✏️ `backend/api/requirements.txt` - Added flask-sqlalchemy
3. ✅ `backend/view_resumes.py` - New script to view stored resumes
4. ✅ `RESUME_DATABASE_FIX.md` - This documentation

## Next Steps

1. **Test Locally** - Verify database storage works locally
2. **Deploy to Vercel** - Push updated code
3. **Add PostgreSQL** - Set up database on Vercel
4. **Test Production** - Upload resume and check `/api/resumes`
5. **Monitor** - Check Vercel logs for any errors

---

**Status:** ✅ Fix Applied - Ready for Testing & Deployment
