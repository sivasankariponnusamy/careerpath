# Deploying CareerPath AI with Database Storage

Complete guide for deploying to Vercel with working database storage.

## Overview

The application now supports database storage in **both environments**:

| Environment | Backend Code | Database | API URL |
|-------------|--------------|----------|---------|
| **Local** | `backend/main.py` | SQLite (`career_path.db`) | `http://localhost:5000/api` |
| **Vercel** | `backend/api/index.py` | PostgreSQL (Vercel) | `https://your-app.vercel.app/api` |

Both use the **same database schema** and store the same data.

## Deployment Steps

### Step 1: Install Vercel CLI (if not installed)

```bash
npm install -g vercel
```

### Step 2: Deploy Backend to Vercel

```bash
cd backend
vercel --prod
```

During deployment:
- Choose your project name (or use existing)
- Confirm settings
- Wait for deployment to complete

You'll get a URL like: `https://backend-careerpath-ai.vercel.app`

### Step 3: Add PostgreSQL Database on Vercel

1. **Go to Vercel Dashboard:**
   - Visit https://vercel.com/dashboard
   - Select your backend project

2. **Create Database:**
   - Click on "Storage" tab
   - Click "Create Database"
   - Select "PostgreSQL"
   - Choose a name: `careerpath-db`
   - Select region (choose closest to your users)
   - Click "Create"

3. **Connect Database to Project:**
   - Vercel automatically creates `DATABASE_URL` environment variable
   - The database tables will be created automatically on first request

4. **Verify Connection:**
   - Go to "Settings" → "Environment Variables"
   - Confirm `DATABASE_URL` exists
   - Should look like: `postgres://username:password@host/database`

### Step 4: Redeploy Backend (with Database)

After adding the database, redeploy:

```bash
cd backend
vercel --prod
```

This ensures the backend recognizes the database.

### Step 5: Deploy Frontend to Vercel

```bash
cd frontend
vercel --prod
```

During deployment, when asked for environment variables, add:
- `VITE_API_URL` = `https://backend-careerpath-ai.vercel.app/api` (your backend URL)

### Step 6: Test the Deployment

1. **Visit your frontend URL:** `https://your-frontend.vercel.app`

2. **Upload a test resume**

3. **Verify database storage:**
   ```bash
   curl https://backend-careerpath-ai.vercel.app/api/resumes
   ```

   You should see:
   ```json
   {
     "resumes": [
       {
         "id": 1,
         "filename": "test_resume.pdf",
         "extracted_skills": ["Python", "React", ...],
         "top_match_role": "Full Stack Developer",
         "upload_date": "2026-04-07T10:30:00"
       }
     ],
     "count": 1
   }
   ```

4. **Check Vercel Logs:**
   - Dashboard → Backend Project → Functions
   - Look for: `✓ Resume saved to database with ID: 1`

## Database Configuration Details

### Backend Environment Variables

The backend code automatically handles both environments:

```python
# In backend/api/index.py
db_path = os.environ.get('DATABASE_URL', 'sqlite:///career_path.db')
if db_path.startswith('postgres://'):
    db_path = db_path.replace('postgres://', 'postgresql://', 1)
```

- **Local:** Uses SQLite file (`career_path.db`)
- **Vercel:** Uses PostgreSQL from `DATABASE_URL` environment variable

### Frontend Environment Variables

For Vercel Frontend deployment, set:

| Variable | Value | Purpose |
|----------|-------|---------|
| `VITE_API_URL` | `https://backend-careerpath-ai.vercel.app/api` | Backend API endpoint |

**How to add:**
1. Vercel Dashboard → Frontend Project → Settings → Environment Variables
2. Add `VITE_API_URL` with your backend URL
3. Redeploy frontend

## Database Schema

Tables created automatically:

### `resumes` Table
```sql
CREATE TABLE resumes (
    id INTEGER PRIMARY KEY,
    filename VARCHAR(255) NOT NULL,
    file_type VARCHAR(50) NOT NULL,
    file_size INTEGER NOT NULL,
    text_content TEXT,
    extracted_skills TEXT,
    categorized_skills TEXT,
    suggested_roles TEXT,
    top_match_role VARCHAR(200),
    top_match_percentage FLOAT,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    processed BOOLEAN DEFAULT FALSE
);
```

## Monitoring & Maintenance

### View Stored Resumes

**Production (Vercel):**
```bash
curl https://backend-careerpath-ai.vercel.app/api/resumes
```

**Local:**
```bash
cd backend
python view_resumes.py
```

### Check Database Size

1. Vercel Dashboard → Storage → PostgreSQL
2. View usage statistics
3. Manage storage limits

### Backup Database

**Local SQLite:**
```bash
cp backend/career_path.db backend/career_path.db.backup
```

**Vercel PostgreSQL:**
1. Dashboard → Storage → Your Database → Settings
2. Use built-in backup tools
3. Or connect with PostgreSQL client and export

## Troubleshooting

### Database Not Saving on Vercel

**Check Environment Variable:**
```bash
# Vercel CLI
vercel env ls

# Should show DATABASE_URL (production)
```

**Check Logs:**
1. Vercel Dashboard → Backend Project → Functions
2. Look for errors in `/api/extract-skills` function
3. Check for: "⚠ Error saving resume to database"

**Common Fix:**
```bash
# Redeploy after ensuring DATABASE_URL exists
cd backend
vercel --prod
```

### "saved_to_database: false" in API Response

The API response includes `saved_to_database` field:

```json
{
  "resume_id": null,
  "saved_to_database": false,
  ...
}
```

If `false`:
1. Database connection failed
2. `DATABASE_URL` not set
3. Database tables not created

**Fix:** Check Vercel logs and ensure PostgreSQL is connected.

### CORS Errors

Backend has CORS enabled for all origins:
```python
CORS(app, origins="*")
```

If you get CORS errors:
1. Check backend is deployed
2. Verify API URL in frontend env variable
3. Redeploy backend

### Database Migration Issues

If you update the database schema:

1. **Local:** Delete `career_path.db` and restart backend
2. **Vercel:** Database tables auto-update on deployment

## Production Checklist

- [ ] Backend deployed to Vercel
- [ ] PostgreSQL database created and connected
- [ ] `DATABASE_URL` environment variable set
- [ ] Backend redeployed after adding database
- [ ] Frontend deployed to Vercel
- [ ] `VITE_API_URL` set in frontend environment variables
- [ ] Test resume upload works
- [ ] Verify `/api/resumes` returns stored data
- [ ] Check Vercel function logs for errors
- [ ] Confirm `saved_to_database: true` in API response

## Cost Considerations

### Vercel Free Tier Includes:
- ✅ Serverless Functions (100k invocations/month)
- ✅ PostgreSQL Database (60 hours compute/month)
- ✅ Bandwidth (100GB/month)

### If You Exceed Free Tier:
- Upgrade to Vercel Pro ($20/month)
- Or use external PostgreSQL (Railway, ElephantSQL, etc.)

## Alternative: External PostgreSQL

If you prefer external PostgreSQL:

1. **Sign up for PostgreSQL hosting:**
   - [Neon](https://neon.tech) (Free tier)
   - [Railway](https://railway.app) (Free trial)
   - [ElephantSQL](https://www.elephantsql.com) (Free tier)

2. **Get connection string:**
   ```
   postgresql://username:password@host:5432/database
   ```

3. **Add to Vercel:**
   - Dashboard → Backend Project → Settings → Environment Variables
   - Add `DATABASE_URL` with your connection string

4. **Redeploy:**
   ```bash
   cd backend
   vercel --prod
   ```

## Support & Resources

- 📖 [Vercel Documentation](https://vercel.com/docs)
- 🗄️ [PostgreSQL on Vercel](https://vercel.com/storage/postgres)
- 🔧 [Flask-SQLAlchemy Docs](https://flask-sqlalchemy.palletsprojects.com/)

---

**Quick Deploy Commands:**

```bash
# Deploy Backend
cd backend && vercel --prod

# Deploy Frontend
cd frontend && vercel --prod

# Test Deployment
curl https://backend-careerpath-ai.vercel.app/api/resumes
```
