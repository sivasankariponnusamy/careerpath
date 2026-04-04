# Resume Database Setup Guide

## Overview
Your CareerPath AI application now stores uploaded resumes in a database! This allows you to:
- ✅ Save resume files permanently
- ✅ Track extracted skills and career matches
- ✅ View upload history
- ✅ Retrieve and analyze past resumes
- ✅ Get statistics on skills and roles

## Database Architecture

### Database Type
- **SQLite** - A lightweight, file-based database (no server required!)
- Database file: `backend/career_path.db` (created automatically)

### Database Tables

#### 1. **Resumes Table**
Stores uploaded resume information:
- `id` - Unique identifier
- `filename` - Original filename
- `file_path` - Path to stored file
- `file_type` - File extension (pdf, docx, pptx, txt)
- `file_size` - File size in bytes
- `text_content` - Extracted text (first 10,000 characters)
- `extracted_skills` - JSON array of detected skills
- `categorized_skills` - JSON object of skills grouped by category
- `suggested_roles` - JSON array of recommended career roles
- `top_match_role` - Best matching career role
- `top_match_percentage` - Match confidence percentage
- `upload_date` - When the resume was uploaded
- `processed` - Whether skill extraction completed
- `user_email` - Optional user email
- `user_name` - Optional user name

#### 2. **SkillGapAnalysis Table**
Stores skill gap analysis results:
- `id` - Unique identifier
- `resume_id` - Foreign key to resumes table
- `user_skills` - JSON array of user's skills
- `target_role` - Desired career role
- `match_percentage` - How well skills match the role
- `missing_skills` - Skills needed for the role
- `matching_skills` - Skills already possessed
- `recommended_skills` - Top skills to learn
- `ai_explanation` - AI-generated guidance
- `learning_roadmap` - Structured learning plan
- `analysis_date` - When analysis was performed

## Installation Steps

### 1. Install Required Packages

```powershell
cd backend
pip install -r requirements.txt
```

This will install:
- `Flask-SQLAlchemy` - Database ORM
- `Flask-Migrate` - Database migrations (optional)

### 2. Database Initialization

The database is **automatically created** when you start the backend server:

```powershell
python main.py
```

You should see:
```
✓ Database initialized successfully!
Training Random Forest Classifier...
✓ Model trained successfully!
```

### 3. File Storage

Resume files are stored in:
```
backend/uploads/
```

Files are saved with timestamps to prevent conflicts:
```
20260321_143052_john_doe_resume.pdf
20260321_143125_jane_smith_cv.docx
```

## API Endpoints

### Resume Management

#### 1. Upload Resume (Existing - Now with DB Storage)
```http
POST /api/extract-skills
Content-Type: multipart/form-data

Body: {resume: <file>}
```

**Response:**
```json
{
  "resume_id": 1,
  "skills": ["Python", "JavaScript", "React"],
  "count": 3,
  "file_type": "pdf",
  "categorized_skills": {...},
  "suggested_roles": [...],
  "top_match": {...},
  "saved_to_database": true
}
```

#### 2. Get All Resumes
```http
GET /api/resumes?limit=50
```

**Response:**
```json
{
  "resumes": [
    {
      "id": 1,
      "filename": "john_doe_resume.pdf",
      "file_type": "pdf",
      "file_size": 125840,
      "extracted_skills": ["Python", "React", "Docker"],
      "top_match_role": "Full Stack Developer",
      "top_match_percentage": 85.5,
      "upload_date": "2026-03-21T14:30:52Z",
      "processed": true
    }
  ],
  "count": 1,
  "total_in_db": 1
}
```

#### 3. Get Single Resume
```http
GET /api/resumes/1
```

#### 4. Download Resume File
```http
GET /api/resumes/1/download
```

Downloads the original uploaded file.

#### 5. Delete Resume
```http
DELETE /api/resumes/1
```

Deletes both database record and file from disk.

#### 6. Get Resume Statistics
```http
GET /api/resumes/stats
```

**Response:**
```json
{
  "total_resumes": 25,
  "total_size_bytes": 5242880,
  "total_size_mb": 5.0,
  "top_skills": [
    {"skill": "Python", "count": 18},
    {"skill": "JavaScript", "count": 15}
  ],
  "role_distribution": {
    "Full Stack Developer": 8,
    "Data Scientist": 6
  },
  "avg_skills_per_resume": 12.5
}
```

### Skill Gap Analysis

#### 7. Get All Analyses
```http
GET /api/skill-gap-analyses?limit=50
```

#### 8. Save Analysis
```http
POST /api/skill-gap-analyses
Content-Type: application/json

Body: {
  "resume_id": 1,
  "user_skills": ["Python", "Flask"],
  "target_role": "Full Stack Developer",
  "match_percentage": 65.5,
  "missing_skills": ["React", "Docker"],
  "matching_skills": ["Python", "Flask"],
  "recommended_skills": [...],
  "ai_explanation": "...",
  "learning_roadmap": {...}
}
```

## Frontend Integration

### Update API Service (Optional)

Add new methods to `frontend/src/services/api.ts`:

```typescript
export const api = {
  // ... existing methods ...

  // Get all resumes
  getAllResumes: (limit: number = 50) =>
    apiClient.get(`/resumes?limit=${limit}`),

  // Get single resume
  getResume: (resumeId: number) =>
    apiClient.get(`/resumes/${resumeId}`),

  // Download resume
  downloadResume: (resumeId: number) =>
    window.open(`${API_BASE_URL}/resumes/${resumeId}/download`, '_blank'),

  // Delete resume
  deleteResume: (resumeId: number) =>
    apiClient.delete(`/resumes/${resumeId}`),

  // Get resume statistics
  getResumeStats: () =>
    apiClient.get('/resumes/stats'),

  // Get all analyses
  getAllAnalyses: (limit: number = 50) =>
    apiClient.get(`/skill-gap-analyses?limit=${limit}`),

  // Save analysis
  saveAnalysis: (analysisData: any) =>
    apiClient.post('/skill-gap-analyses', analysisData),
};
```

### Update Resume Uploader Component (Optional)

The component already works! The backend now automatically saves resumes. You can optionally display the `resume_id` to users:

```typescript
// In ResumeUploader.tsx, after successful upload:
const data = await response.json();
console.log('Resume saved with ID:', data.resume_id);
// You can now store this ID for later retrieval
```

## Database Management

### View Database Contents

#### Option 1: SQLite Browser (Recommended)
1. Download [DB Browser for SQLite](https://sqlitebrowser.org/)
2. Open `backend/career_path.db`
3. Browse tables, run queries, export data

#### Option 2: Python Script
```python
import sqlite3
import json

conn = sqlite3.connect('career_path.db')
cursor = conn.cursor()

# Get all resumes
cursor.execute("SELECT id, filename, top_match_role, upload_date FROM resumes")
for row in cursor.fetchall():
    print(row)

conn.close()
```

#### Option 3: Command Line
```powershell
sqlite3 backend/career_path.db

# View tables
.tables

# Query resumes
SELECT id, filename, top_match_role FROM resumes;

# Exit
.quit
```

### Backup Database

```powershell
# Simple backup
copy backend\career_path.db backend\career_path_backup.db

# Or with timestamp
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
copy backend\career_path.db "backend\backup\career_path_${timestamp}.db"
```

### Reset Database

If you need to start fresh:

```powershell
# Stop the backend server first!
# Then delete the database file
rm backend\career_path.db

# Restart the server - it will create a new empty database
python backend\main.py
```

## Troubleshooting

### Issue: Database file not created

**Solution:**
- Make sure you're running `python main.py` from the backend directory
- Check console for error messages
- Ensure you have write permissions in the backend folder

### Issue: "No such table: resumes"

**Solution:**
- Delete `career_path.db` and restart the server
- The database will be recreated with correct tables

### Issue: Resume files not saving

**Solution:**
- Check that `backend/uploads/` directory exists
- Verify disk space
- Check file permissions

### Issue: "Database is locked"

**Solution:**
- Close any other programs accessing the database (like SQLite Browser)
- Restart the backend server

## Migration to PostgreSQL/MySQL (Optional)

For production, consider migrating to a robust database:

### PostgreSQL Setup:

1. Install PostgreSQL
2. Create database:
```sql
CREATE DATABASE careerpath;
```

3. Update `main.py`:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/careerpath'
```

4. Install PostgreSQL driver:
```bash
pip install psycopg2-binary
```

5. Restart server - tables will be created automatically

## Security Considerations

### Current Setup (Development)
- ✅ Files stored locally
- ✅ No authentication required
- ⚠️ Database is not encrypted
- ⚠️ All users share the same database

### For Production:
1. Add user authentication
2. Store user_id with each resume
3. Implement access controls
4. Encrypt sensitive data
5. Use environment variables for configuration
6. Set up regular backups
7. Use HTTPS for file transfers

## What's Stored vs. What's Not

### ✅ Stored in Database:
- Resume metadata (filename, size, type)
- Extracted skills
- Career role suggestions
- Analysis results
- Upload timestamps

### ✅ Stored on Disk:
- Original resume files (PDF, DOCX, etc.)

### ❌ Not Stored:
- Temporary upload data
- User session information (no auth yet)
- API request logs

## Next Steps

1. ✅ **Test the Integration**
   - Upload a resume
   - Check `backend/career_path.db` was created
   - View uploaded files in `backend/uploads/`

2. **Build a Resume History UI**
   - Create a component to list all uploaded resumes
   - Add download and delete buttons
   - Show statistics dashboard

3. **Add User Authentication**
   - Implement login system
   - Associate resumes with users
   - Add privacy controls

4. **Analytics Dashboard**
   - Show trending skills
   - Display role distributions
   - Track user progress over time

## Support

If you encounter any issues:
1. Check the console output for error messages
2. Verify all packages are installed: `pip list`
3. Ensure database file has write permissions
4. Check that uploads folder exists and is writable

---

**Database is now connected!** 🎉

Your resumes are being saved automatically every time a user uploads a file.
