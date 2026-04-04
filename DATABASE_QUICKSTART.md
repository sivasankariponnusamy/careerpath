# Quick Start: Database Integration for Resume Storage

## What Changed?

Your CareerPath AI now saves uploaded resumes to a database! Previously, resumes were only processed in memory and lost after page refresh. Now they're permanently stored.

## Installation (3 Steps)

### Step 1: Install New Dependencies

```powershell
cd backend
pip install Flask-SQLAlchemy Flask-Migrate
```

### Step 2: Start the Backend

```powershell
python main.py
```

You should see:
```
✓ Database initialized successfully!
✓ Model trained successfully!
```

### Step 3: Test It!

1. Open the frontend in your browser
2. Upload a resume
3. Check that these were created:
   - `backend/career_path.db` (SQLite database)
   - `backend/uploads/` (folder with resume files)

## What's New?

### Backend Changes

1. **New Database Models** (`backend/models.py`)
   - `Resume` - Stores resume metadata and extracted data
   - `SkillGapAnalysis` - Stores career analysis results

2. **Updated Main App** (`backend/main.py`)
   - Database configuration added
   - Resumes now saved to database after processing
   - File uploads stored in `backend/uploads/`

3. **New API Endpoints**
   - `GET /api/resumes` - List all uploaded resumes
   - `GET /api/resumes/<id>` - Get specific resume
   - `GET /api/resumes/<id>/download` - Download original file
   - `DELETE /api/resumes/<id>` - Delete resume
   - `GET /api/resumes/stats` - Get statistics
   - `GET /api/skill-gap-analyses` - List analyses
   - `POST /api/skill-gap-analyses` - Save analysis

### Frontend Changes

1. **Updated API Client** (`frontend/src/services/api.ts`)
   - Added `delete()` method
   - Added new API methods for resume management

## Verify It's Working

### Check Database

```powershell
# View database contents (Windows)
sqlite3 backend\career_path.db
.tables
SELECT * FROM resumes;
.quit
```

Or download [DB Browser for SQLite](https://sqlitebrowser.org/) for a GUI.

### Check Uploaded Files

```powershell
dir backend\uploads
```

You should see your uploaded resume files with timestamps.

## Next Steps (Optional)

### 1. Build Resume History UI

Create a component to display all uploaded resumes:

```typescript
// Example component
import { useState, useEffect } from 'react';
import { api } from '@/services/api';

export function ResumeHistory() {
  const [resumes, setResumes] = useState([]);

  useEffect(() => {
    api.getAllResumes().then(data => {
      setResumes(data.resumes);
    });
  }, []);

  return (
    <div>
      <h2>Resume History</h2>
      {resumes.map(resume => (
        <div key={resume.id}>
          <p>{resume.filename}</p>
          <p>Uploaded: {new Date(resume.upload_date).toLocaleDateString()}</p>
          <p>Top Match: {resume.top_match_role} ({resume.top_match_percentage}%)</p>
          <button onClick={() => api.downloadResume(resume.id)}>Download</button>
          <button onClick={() => api.deleteResume(resume.id)}>Delete</button>
        </div>
      ))}
    </div>
  );
}
```

### 2. Display Statistics Dashboard

```typescript
const stats = await api.getResumeStats();
console.log(`Total resumes: ${stats.total_resumes}`);
console.log(`Top skill: ${stats.top_skills[0].skill}`);
```

### 3. Save Skill Gap Analyses

When user completes a skill gap analysis, save it:

```typescript
const analysis = {
  resume_id: 1,  // If from uploaded resume
  user_skills: selectedSkills,
  target_role: targetRole,
  match_percentage: gapAnalysis.match_percentage,
  missing_skills: gapAnalysis.missing_skills,
  matching_skills: gapAnalysis.matching_skills,
  recommended_skills: gapAnalysis.recommended_skills,
  ai_explanation: aiGuidance.explanation,
  learning_roadmap: aiGuidance.roadmap
};

await api.saveAnalysis(analysis);
```

## Troubleshooting

### Database not created?

1. Make sure you're in the backend directory
2. Check you have write permissions
3. Look for error messages in console

### Can't install Flask-SQLAlchemy?

```powershell
# Try upgrading pip first
python -m pip install --upgrade pip
pip install Flask-SQLAlchemy Flask-Migrate
```

### Resume files not saving?

Check that `backend/uploads/` folder was created:
```powershell
mkdir backend\uploads  # Create manually if needed
```

## File Structure

```
backend/
├── main.py              (Updated - Database integration)
├── models.py            (New - Database models)
├── requirements.txt     (Updated - New dependencies)
├── career_path.db       (New - SQLite database)
└── uploads/             (New - Resume files folder)
    └── 20260321_143052_resume.pdf

frontend/
└── src/
    └── services/
        └── api.ts       (Updated - New API methods)
```

## Testing Checklist

- [ ] Backend starts without errors
- [ ] `career_path.db` file is created
- [ ] `uploads/` folder is created
- [ ] Upload a resume through the UI
- [ ] Resume appears in database
- [ ] File is saved in `uploads/` folder
- [ ] API returns `resume_id` in response
- [ ] Can query `/api/resumes` endpoint

## Database Schema Visualization

```
┌─────────────────────────────┐
│       resumes               │
├─────────────────────────────┤
│ id (PK)                     │
│ filename                    │
│ file_path                   │
│ file_type                   │
│ file_size                   │
│ text_content                │
│ extracted_skills (JSON)     │
│ categorized_skills (JSON)   │
│ suggested_roles (JSON)      │
│ top_match_role              │
│ top_match_percentage        │
│ upload_date                 │
│ processed                   │
│ user_email                  │
│ user_name                   │
└─────────────────────────────┘
         ↑
         │ (FK: resume_id)
         │
┌─────────────────────────────┐
│  skill_gap_analyses         │
├─────────────────────────────┤
│ id (PK)                     │
│ resume_id (FK)              │
│ user_skills (JSON)          │
│ target_role                 │
│ match_percentage            │
│ missing_skills (JSON)       │
│ matching_skills (JSON)      │
│ recommended_skills (JSON)   │
│ ai_explanation              │
│ learning_roadmap (JSON)     │
│ analysis_date               │
└─────────────────────────────┘
```

## Success! 🎉

Your resumes are now being saved to the database automatically. Every upload is tracked with full metadata and analysis results.

For detailed information, see: [RESUME_DATABASE_SETUP.md](./RESUME_DATABASE_SETUP.md)
