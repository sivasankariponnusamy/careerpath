# Running CareerPath AI Locally

This guide shows you how to run the application locally with database storage working.

## Prerequisites

- Python 3.8+ installed
- Node.js 16+ installed
- Both backend and frontend dependencies installed

## Step 1: Start Backend Server

Open a terminal and run:

```bash
cd backend
python main.py
```

You should see:
```
✓ Database initialized successfully!
✓ Dataset loaded with X skills
✓ Model trained successfully!
 * Running on http://127.0.0.1:5000
```

**Keep this terminal open** - the backend must stay running.

## Step 2: Configure Frontend for Local Development

The frontend is already configured to use `VITE_API_URL` environment variable.

A `.env.local` file has been created in the `frontend/` directory with:
```
VITE_API_URL=http://localhost:5000/api
```

This tells the frontend to use your local backend instead of Vercel.

## Step 3: Start Frontend

Open **another terminal** and run:

```bash
cd frontend
npm run dev
```

You should see:
```
VITE v5.x.x  ready in XXX ms

➜  Local:   http://localhost:5173/
➜  Network: use --host to expose
```

## Step 4: Test the Application

1. **Open browser:** Go to http://localhost:5173/
2. **Upload a resume:** Use the "AI Resume Scanner" feature
3. **Wait for processing:** Skills will be extracted and analyzed
4. **Verify database storage:**

Open **another terminal** and run:
```bash
cd backend
python test_database.py
```

You should see:
```
🔍 Testing Database Connection...
✅ Database connected successfully!
📊 Total resumes in database: 1

📋 Last 1 uploaded resume(s):

1. your_resume.pdf
   ├─ Uploaded: 2026-04-07 10:30:00
   ├─ Skills: 25 found
   └─ Top Match: Full Stack Developer (85.5%)

✅ Test completed successfully!
```

## Database Location

When running locally, the SQLite database is stored at:
```
backend/career_path.db
```

You can view the database using:
```bash
cd backend
python view_resumes.py
```

## Troubleshooting

### Backend won't start
```bash
cd backend
pip install -r requirements.txt
python main.py
```

### Frontend shows connection error
1. Make sure backend is running on http://localhost:5000
2. Check that `frontend/.env.local` exists with `VITE_API_URL=http://localhost:5000/api`
3. Restart the frontend dev server

### Database not saving
1. Check if `backend/career_path.db` file exists
2. Run `python test_database.py` to see detailed error
3. Check backend terminal for error messages

### "CORS" errors
The backend has CORS enabled for all origins, so this shouldn't happen.
If it does, restart the backend server.

## Switching Between Local and Deployed

### Use Local Backend
```bash
# frontend/.env.local
VITE_API_URL=http://localhost:5000/api
```

### Use Deployed Backend (Vercel)
```bash
# frontend/.env.local
VITE_API_URL=https://backend-careerpath-ai.vercel.app/api
```

Or delete `frontend/.env.local` to use the default Vercel URL.

## API Endpoints Available

When running locally, you can test these endpoints:

### Health Check
```bash
curl http://localhost:5000/api/health
```

### Get All Skills
```bash
curl http://localhost:5000/api/skills
```

### Get Stored Resumes
```bash
curl http://localhost:5000/api/resumes
```

### Upload Resume
```bash
curl -X POST http://localhost:5000/api/extract-skills \
  -F "resume=@path/to/your/resume.pdf"
```

## Next Steps

- ✅ Local development is set up
- 🚀 For deployment, see [DEPLOYMENT.md](DEPLOYMENT.md)
- 📖 For database fix details, see [RESUME_DATABASE_FIX.md](RESUME_DATABASE_FIX.md)

---

**Quick Start Commands:**

Terminal 1 (Backend):
```bash
cd backend && python main.py
```

Terminal 2 (Frontend):
```bash
cd frontend && npm run dev
```

Terminal 3 (Test Database):
```bash
cd backend && python test_database.py
```
