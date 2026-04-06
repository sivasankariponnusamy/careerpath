## Quick Debug - Check Which API is Being Called

Open your browser's **Developer Tools** (Press `F12`) and do this:

### Step 1: Open Console Tab
1. Press `F12` to open Developer Tools
2. Click the **Console** tab
3. Type this command and press Enter:

```javascript
console.log('API URL:', import.meta.env.VITE_API_URL || 'https://backend-careerpath-ai.vercel.app/api');
```

### Expected Output:
- ✅ **CORRECT:** `API URL: http://localhost:5000/api`
- ❌ **WRONG:** `API URL: https://backend-careerpath-ai.vercel.app/api`

---

### Step 2: Check Network Tab
1. Click the **Network** tab in Developer Tools
2. Click **"Upload Different File"** button
3. Upload a resume
4. Look for the **extract-skills** request
5. Check the **Request URL**

### Expected URL:
- ✅ **CORRECT:** `http://localhost:5000/api/extract-skills`
- ❌ **WRONG:** `https://backend-careerpath-ai.vercel.app/api/extract-skills`

---

## If It Shows VERCEL URL:

The frontend environment variable is NOT loaded. Do this:

### Fix 1: Hard Refresh Browser
Press `Ctrl + Shift + Delete` and:
1. Check "Cached images and files"
2. Click "Clear data"
3. Close browser completely
4. Reopen: http://localhost:5173
5. Press `Ctrl + F5` (hard refresh)

### Fix 2: Check .env.local
Open a terminal and run:
```powershell
Get-Content frontend\.env.local
```

Should show:
```
VITE_API_URL=http://localhost:5000/api
```

### Fix 3: Restart Frontend (Critical!)
In your frontend terminal, press `Ctrl + C` to stop it, then:
```bash
cd frontend
npm run dev
```

---

## Quick Test Command

After the fixes, run this in a NEW terminal to check:
```powershell
cd backend
python test_database.py
```

The count should increase from **9** to **10** after uploading!
