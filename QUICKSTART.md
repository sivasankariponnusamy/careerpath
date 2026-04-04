# Quick Start Guide

## Step 1: Start Backend Server

```bash
# Open terminal 1
cd backend

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run server
python app.py
```

✅ Backend running on: http://localhost:5000

## Step 2: Start Frontend Server

```bash
# Open terminal 2
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

✅ Frontend running on: http://localhost:5173

## Step 3: Open Application

Open your browser and go to: **http://localhost:5173**

## Demo Flow

1. **Select Your Skills**: Choose your current skills from the list
2. **Choose Career Role**: Select your target job role
3. **Click Analyze**: Get your skill gap analysis
4. **View Results**: 
   - See your match percentage
   - View missing skills
   - Get learning roadmap
5. **Career Guidance**: Receive AI-powered recommendations

## Troubleshooting

### Backend Issues
- **Port 5000 in use**: Change port in `backend/app.py` (line: `app.run(port=5000)`)
- **Module not found**: Ensure virtual environment is activated and dependencies installed
- **CSV file not found**: Verify `dataset/` folder is in the correct location

### Frontend Issues
- **Port 5173 in use**: Vite will automatically use next available port
- **API connection failed**: Ensure backend is running on port 5000
- **Module not found**: Run `npm install` again

## Testing the API

You can test the backend API using curl or Postman:

```bash
# Health check
curl http://localhost:5000/api/health

# Get all skills
curl http://localhost:5000/api/skills

# Get all roles
curl http://localhost:5000/api/roles

# Analyze skills (POST request)
curl -X POST http://localhost:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"skills": ["Python", "Machine Learning"], "target_role": "Data Scientist"}'
```

## Environment Variables

### Frontend (.env)
```
VITE_API_URL=http://localhost:5000/api
```

### Backend
No environment variables required for basic setup.

For LLaMA integration, add to `backend/.env`:
```
LLAMA_API_KEY=your_api_key_here
LLAMA_API_URL=your_llama_endpoint
```

---

**Happy Learning! 🚀**
