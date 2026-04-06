# 🎯 CareerPath AI - Complete Setup Guide

## ✅ Database Storage Now Works in Both Environments!

Your resume upload feature now **properly stores data** in the database for both:
- 🏠 **Local Development** (SQLite)
- 🌐 **Production Deployment** (PostgreSQL on Vercel)

---

## 🚀 Quick Start - Local Development

### Windows (Easiest)

```powershell
.\start-local.ps1
```

This automatically:
- ✅ Starts backend on http://localhost:5000
- ✅ Starts frontend on http://localhost:5173  
- ✅ Creates database file
- ✅ Configures environment variables

**Open:** http://localhost:5173

### Manual Start

**Terminal 1 - Backend:**
```bash
cd backend
python main.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

**Open:** http://localhost:5173

---

## 🧪 Test Database Storage

After uploading a resume:

```bash
cd backend
python test_database.py
```

**Expected Output:**
```
✅ Database connected successfully!
📊 Total resumes in database: 1

1. your_resume.pdf
   ├─ Uploaded: 2026-04-07 10:30:00
   ├─ Skills: 25 found
   └─ Top Match: Full Stack Developer (85.5%)
```

---

## 🌐 Deploy to Production

### 1. Deploy Backend

```bash
cd backend
vercel --prod
```

### 2. Add PostgreSQL Database

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Select your backend project
3. Click **Storage** → **Create Database** → **PostgreSQL**
4. Wait for automatic `DATABASE_URL` setup
5. Redeploy: `vercel --prod`

### 3. Deploy Frontend

```bash
cd frontend
vercel --prod
```

During setup, set environment variable:
- `VITE_API_URL` = `https://your-backend.vercel.app/api`

### 4. Verify Production Storage

```bash
curl https://your-backend.vercel.app/api/resumes
```

Should return stored resumes ✅

---

## 📊 What Gets Stored

Every uploaded resume saves:

| Field | Description | Example |
|-------|-------------|---------|
| **filename** | Original file name | `john_resume.pdf` |
| **file_type** | File extension | `pdf` |
| **file_size** | Size in bytes | `524288` |
| **extracted_skills** | All found skills | `["Python", "React", "AWS"]` |
| **categorized_skills** | Skills by category | `{"Programming": ["Python"]}` |
| **suggested_roles** | Career matches | `[{"role": "...", "match": 85}]` |
| **top_match_role** | Best career fit | `Full Stack Developer` |
| **top_match_percentage** | Match score | `85.5` |
| **upload_date** | Timestamp | `2026-04-07T10:30:00` |

---

## 🔧 Configuration

### Local Development

**Backend:** Uses SQLite database at `backend/career_path.db`

**Frontend:** Uses `frontend/.env.local`:
```env
VITE_API_URL=http://localhost:5000/api
```

### Production (Vercel)

**Backend:** Uses PostgreSQL via `DATABASE_URL` environment variable (auto-configured)

**Frontend:** Set environment variable in Vercel Dashboard:
```
VITE_API_URL=https://your-backend.vercel.app/api
```

---

## 🆕 New API Endpoints

### 1. Get All Resumes
```http
GET /api/resumes
```

Returns list of all stored resumes (last 50).

### 2. Get Specific Resume
```http
GET /api/resumes/{id}
```

Returns detailed info for one resume.

### 3. Upload Resume (Enhanced)
```http
POST /api/extract-skills
```

Now returns:
- `resume_id` - Database ID ✅
- `saved_to_database` - Storage confirmation ✅
- All extracted data

---

## 📖 Detailed Documentation

| Guide | Description |
|-------|-------------|
| [QUICK_START.md](QUICK_START.md) | Fast setup for both environments |
| [RUN_LOCAL.md](RUN_LOCAL.md) | Complete local development guide |
| [DEPLOY_WITH_DATABASE.md](DEPLOY_WITH_DATABASE.md) | Full deployment instructions |
| [RESUME_DATABASE_FIX.md](RESUME_DATABASE_FIX.md) | Technical details of the fix |
| [SUMMARY.md](SUMMARY.md) | Visual overview of changes |

---

## 🛠️ Useful Commands

### View Stored Resumes
```bash
# Local
cd backend
python view_resumes.py

# Production
curl https://your-backend.vercel.app/api/resumes
```

### Test Database Connection
```bash
cd backend
python test_database.py
```

### Check API Health
```bash
# Local
curl http://localhost:5000/api/health

# Production
curl https://your-backend.vercel.app/api/health
```

### View Database File
```bash
# Local SQLite
cd backend
python view_db.py
```

---

## ✔️ Verification Checklist

### Local Development
- [ ] Backend starts without errors
- [ ] Frontend loads at http://localhost:5173
- [ ] Can upload resume
- [ ] Skills are extracted
- [ ] `test_database.py` shows stored resume
- [ ] File `backend/career_path.db` exists

### Vercel Production
- [ ] Backend deployed successfully
- [ ] PostgreSQL database created
- [ ] `DATABASE_URL` environment variable set
- [ ] Frontend deployed successfully
- [ ] `VITE_API_URL` configured in frontend
- [ ] Can upload resume
- [ ] `/api/resumes` returns stored data
- [ ] Response shows `saved_to_database: true`

---

## 🎉 What Was Fixed

### Before
- ❌ Uploaded resumes NOT saved to database
- ❌ Only Vercel backend existed (no storage)
- ❌ Skills extracted but lost after refresh
- ❌ No way to retrieve previous uploads

### After  
- ✅ All uploads SAVED to database
- ✅ Works in LOCAL and PRODUCTION
- ✅ Permanent storage of skills & analysis
- ✅ Can retrieve all upload history
- ✅ New API endpoints for data access
- ✅ Easy testing with `test_database.py`

---

## 📂 Project Structure

```
careerpath/
├── backend/
│   ├── main.py                  # Local development server ✅ Database
│   ├── api/
│   │   └── index.py            # Vercel serverless function ✅ Database
│   ├── models.py               # Database models
│   ├── requirements.txt        # Python dependencies
│   ├── test_database.py        # Test storage ✅ NEW
│   ├── view_resumes.py         # View stored data ✅ NEW
│   └── career_path.db          # SQLite database (local) ✅ Created
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   └── ResumeUploader.tsx  # Fixed API URL ✅
│   │   └── services/
│   │       └── api.ts          # API client
│   ├── .env.local              # Local config ✅ NEW
│   └── package.json
│
├── start-local.ps1             # Windows startup script ✅ NEW
├── start-local.sh              # Linux/Mac startup script ✅ NEW
├── QUICK_START.md              # Quick guide ✅ NEW
├── RUN_LOCAL.md                # Local setup guide ✅ NEW
├── DEPLOY_WITH_DATABASE.md     # Deployment guide ✅ NEW
├── RESUME_DATABASE_FIX.md      # Technical details ✅ NEW
├── SUMMARY.md                  # Visual summary ✅ NEW
└── README_COMPLETE.md          # This file ✅ NEW
```

---

## 🆘 Troubleshooting

### "Module not found" errors
```bash
cd backend
pip install -r requirements.txt
```

### Port already in use
```powershell
# Windows - Kill process on port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Frontend can't connect
1. Verify backend is running: `curl http://localhost:5000/api/health`
2. Check `frontend/.env.local` has `VITE_API_URL=http://localhost:5000/api`
3. Restart frontend: `npm run dev`

### Database not saving
1. Run `python test_database.py` for detailed diagnostics
2. Check backend console for errors
3. Verify `backend/career_path.db` file exists
4. Check file permissions

### Vercel deployment issues
1. Ensure PostgreSQL database is created
2. Verify `DATABASE_URL` environment variable exists
3. Check Vercel function logs for errors
4. Redeploy after database setup

---

## 📞 Support

For issues:
1. Check the troubleshooting section above
2. Review the detailed guides in documentation
3. Check Vercel function logs (for production issues)
4. Verify all environment variables are set

---

## 🎊 Success!

Your CareerPath AI application now has **full database storage** working in both local development and production deployment!

**Next Steps:**
1. ✅ Test locally with `.\start-local.ps1`
2. ✅ Upload a resume and verify storage
3. ✅ Deploy to Vercel when ready
4. ✅ Set up PostgreSQL on Vercel
5. ✅ Test production deployment

**Happy coding! 🚀**
