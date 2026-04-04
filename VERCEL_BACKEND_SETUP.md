# Deploy Flask Backend to Vercel (FREE - No Credit Card)

## Quick Setup Steps

### 1. Install Vercel CLI
```bash
npm install -g vercel
```

### 2. Login to Vercel
```bash
vercel login
```
- Choose "Continue with GitHub" (easiest)
- Authorize Vercel in the browser

### 3. Deploy Backend
```bash
cd backend
vercel
```

When prompted:
- **Set up and deploy?** → Yes (Y)
- **Which scope?** → Your username
- **Link to existing project?** → No (N)
- **Project name?** → `careerpath-backend` (or any name)
- **Directory?** → `.` (current directory)
- **Override settings?** → No (N)

### 4. Get Your Backend URL
After deployment completes, Vercel will show:
```
✅ Production: https://careerpath-backend-xyz.vercel.app
```

**Copy this URL!** You'll need it to connect the frontend.

### 5. Update Frontend to Use Vercel Backend

Once you have the Vercel URL, I'll update your frontend to use it instead of localhost:5000

---

## Alternative: Deploy via Vercel Dashboard (No CLI)

### 1. Go to Vercel
Visit: https://vercel.com/signup

### 2. Sign Up with GitHub
- Click "Continue with GitHub"
- Authorize Vercel

### 3. Import Your Repository
- Click "Add New..." → "Project"
- Select your `careerpath` repository
- Click "Import"

### 4. Configure Project
- **Framework Preset:** Other
- **Root Directory:** `backend`
- Click "Deploy"

### 5. Wait for Deployment
- Takes 1-2 minutes
- Once complete, you'll see your backend URL

### 6. Test Backend
Visit: `https://your-backend-url.vercel.app/api/health`

Should return: `{"status": "healthy"}`

---

## Update Frontend (After Backend Deploys)

Tell me your Vercel backend URL and I'll update the frontend automatically!

Example: `https://careerpath-backend-abc123.vercel.app`

---

## Free Tier Limits
- ✅ Unlimited deployments
- ✅ 100 GB bandwidth/month
- ✅ Serverless functions (perfect for Flask)
- ✅ Automatic HTTPS
- ✅ Global CDN
- ✅ **No credit card required**

---

## Troubleshooting

**Error: "Serverless Function has crashed"**
- Check Vercel deployment logs
- Make sure all dependencies are in requirements.txt

**Error: "Database not found"**
- Vercel serverless functions are stateless
- SQLite won't persist between requests
- For production, use PostgreSQL (free tier: supabase.com or neon.tech)

**CORS errors**
- Already configured in main.py with `CORS(app)`
- Should work automatically
