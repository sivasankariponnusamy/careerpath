# CareerPath AI - Quick Start Guide

## 🚀 Running Locally (Recommended for Development)

### Option 1: Automatic Startup (Windows)

Just double-click or run:
```powershell
.\start-local.ps1
```

This will:
- ✅ Start backend on http://localhost:5000
- ✅ Start frontend on http://localhost:5173
- ✅ Configure environment variables automatically
- ✅ Create database file
- ✅ Database storage **works perfectly**

### Option 2: Manual Startup

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

**Open browser:** http://localhost:5173

### Verify Database Storage Works

After uploading a resume:
```bash
cd backend
python test_database.py
```

You should see:
```
✅ Database connected successfully!
📊 Total resumes in database: 1

1. your_resume.pdf
   ├─ Skills: 25 found
   └─ Top Match: Full Stack Developer (85.5%)
```

---

## 🌐 Deploying to Vercel (Production)

### Quick Deploy

```bash
# Deploy Backend
cd backend
vercel --prod

# Deploy Frontend  
cd frontend
vercel --prod
```

### Setup Database on Vercel

1. **Go to** [Vercel Dashboard](https://vercel.com/dashboard)
2. **Select** your backend project
3. **Click** Storage → Create Database → PostgreSQL
4. **Wait** for automatic connection
5. **Redeploy** backend

✅ Database storage now works on Vercel too!

### Full Deployment Guide

See [DEPLOY_WITH_DATABASE.md](DEPLOY_WITH_DATABASE.md) for complete instructions.

---

## 🗄️ Database Storage - Works in Both Environments!

| Environment | Backend | Database | Status |
|-------------|---------|----------|--------|
| **Local** | `backend/main.py` | SQLite file | ✅ Working |
| **Vercel** | `backend/api/index.py` | PostgreSQL | ✅ Working |

### What Gets Stored

Every uploaded resume saves:
- ✅ Filename, file type, file size
- ✅ Extracted skills (full list)
- ✅ Categorized skills (by category)
- ✅ Suggested career roles
- ✅ Top match role & percentage
- ✅ Upload timestamp

### View Stored Data

**Local:**
```bash
cd backend
python view_resumes.py
```

**Vercel:**
```bash
curl https://your-backend.vercel.app/api/resumes
```

---

## 📝 Configuration Files

### Local Development
- `frontend/.env.local` - Uses local backend (http://localhost:5000/api)
- `backend/career_path.db` - SQLite database file

### Production (Vercel)
- Environment variable: `VITE_API_URL` → your backend URL
- Environment variable: `DATABASE_URL` → PostgreSQL connection (auto-set)

---

## 🔧 Troubleshooting

### Frontend can't connect to backend

**Check if backend is running:**
```bash
curl http://localhost:5000/api/health
```

**Should return:**
```json
{"status": "healthy", "message": "Flask backend is running"}
```

**Fix:** Make sure backend is started first, then frontend.

### Database not saving

**Run test:**
```bash
cd backend
python test_database.py
```

**Common issues:**
- Backend not running
- Database file permission error
- Import errors (run `pip install -r requirements.txt`)

### Port already in use

**Kill processes on ports:**
```powershell
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

netstat -ano | findstr :5173
taskkill /PID <PID> /F
```

---

## 📚 Documentation

- [RUN_LOCAL.md](RUN_LOCAL.md) - Detailed local setup guide
- [DEPLOY_WITH_DATABASE.md](DEPLOY_WITH_DATABASE.md) - Complete deployment guide
- [RESUME_DATABASE_FIX.md](RESUME_DATABASE_FIX.md) - Technical details on the database fix

---

## ✅ Quick Checklist

**For Local Development:**
- [ ] Run `.\start-local.ps1` or start manually
- [ ] Open http://localhost:5173
- [ ] Upload a test resume
- [ ] Run `python test_database.py` to verify storage
- [ ] Check `backend/career_path.db` file exists

**For Vercel Deployment:**
- [ ] Deploy backend: `cd backend && vercel --prod`
- [ ] Create PostgreSQL on Vercel Dashboard
- [ ] Deploy frontend: `cd frontend && vercel --prod`
- [ ] Set `VITE_API_URL` environment variable in frontend
- [ ] Test upload and check `/api/resumes` endpoint

---

**Both environments fully support database storage! 🎉**
