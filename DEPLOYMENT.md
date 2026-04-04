# 🚀 Deployment Guide

This guide will help you deploy CareerPath AI as a live website.

## 📋 Deployment Options

### Option 1: Vercel (Recommended - Easiest)

**Frontend Deployment:**

1. Go to [Vercel](https://vercel.com)
2. Sign in with your GitHub account
3. Click "Add New Project"
4. Import your repository: `sivasankari28121/careerpath-ai`
5. Vercel will auto-detect: Framework Preset: **Vite**
6. Override settings:
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
7. Click **Deploy**

Your frontend will be live at: `https://careerpath-ai.vercel.app`

---

### Option 2: Netlify

**Frontend Deployment:**

1. Go to [Netlify](https://netlify.com)
2. Sign in with your GitHub account
3. Click "Add new site" → "Import an existing project"
4. Choose GitHub and select your repository
5. Build settings (auto-detected from `netlify.toml`):
   - **Base directory**: `frontend`
   - **Build command**: `npm run build`
   - **Publish directory**: `frontend/dist`
6. Click **Deploy**

Your frontend will be live at: `https://your-site-name.netlify.app`

---

### Option 3: GitHub Pages

**Frontend Deployment:**

1. Your repository already has GitHub Actions workflow configured
2. Go to your GitHub repository settings
3. Navigate to **Pages** → **Source**
4. Select **GitHub Actions**
5. Push your code to the `main` branch
6. The workflow will automatically build and deploy

Your site will be live at: `https://sivasankari28121.github.io/careerpath-ai/`

---

## 🔧 Backend Deployment (Optional)

Since the frontend currently has mock data, you can deploy just the frontend. For full functionality with the Flask backend:

### Deploy Backend to Render:

1. Go to [Render](https://render.com)
2. Sign in with GitHub
3. Click **New** → **Web Service**
4. Connect your repository
5. Configure:
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python main.py`
   - **Environment**: Python 3.11+
6. Add environment variable:
   - `PYTHON_VERSION`: `3.11`
7. Click **Create Web Service**

Then update your frontend API URL to point to your Render backend URL.

---

## 🌐 Quick Deploy Commands

If you want to push your code now:

```bash
# Add deployment files to git
git add .
git commit -m "Add deployment configuration"

# Push to GitHub
git push origin main
```

---

## ✅ What's Already Configured

- ✅ `vercel.json` - Vercel configuration
- ✅ `netlify.toml` - Netlify configuration  
- ✅ `.github/workflows/deploy.yml` - GitHub Actions workflow
- ✅ `.gitignore` - Git ignore rules

---

## 🎯 Next Steps

1. **Push your code to GitHub** (if not already done)
2. **Choose a deployment platform** (Vercel recommended)
3. **Deploy your frontend**
4. **Share your live URL!** 🎉

---

## 💡 Tips

- Vercel and Netlify offer **free tier** with automatic deployments
- Every push to `main` branch triggers automatic redeployment
- You can add a custom domain later
- GitHub Pages is free but may have slower build times

---

## 🆘 Need Help?

If you encounter any issues:
1. Check build logs on your deployment platform
2. Ensure all environment variables are set
3. Verify Node.js version is 18+
4. Make sure all dependencies are in package.json
