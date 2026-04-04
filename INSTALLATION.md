# 🎓 AI-Driven Career Recommendation System - Setup Guide

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+** (Download from [python.org](https://www.python.org/downloads/))
- **Node.js 16+** (Download from [nodejs.org](https://nodejs.org/))
- **Git** (Optional, for cloning)

---

## 🚀 Quick Start Guide

### Step 1: Backend Setup

#### 1.1 Navigate to Backend Directory
```bash
cd backend
```

#### 1.2 Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

#### 1.3 Install Python Dependencies
```bash
pip install -r requirements.txt
```

**Required Packages:**
- Flask 3.0.0
- flask-cors 4.0.0
- pandas 2.0.0+
- numpy 1.24.0+
- scikit-learn 1.3.0+
- requests 2.31.0+

**Optional (for resume parsing):**
- PyPDF2 3.0.0+
- python-docx 0.8.11+
- python-pptx 0.6.21+

#### 1.4 Start Backend Server
```bash
python main.py
```

**Expected Output:**
```
Training Random Forest Classifier...
✓ Model trained successfully!
  Training Accuracy: 95.23%
  Testing Accuracy: 91.45%
 * Running on http://0.0.0.0:5000
```

The backend server will start on `http://localhost:5000`

---

### Step 2: Frontend Setup

#### 2.1 Open New Terminal
Keep the backend running and open a new terminal window.

#### 2.2 Navigate to Frontend Directory
```bash
cd frontend
```

#### 2.3 Install Node Dependencies
```bash
npm install
```

**Key Dependencies:**
- React 18
- TypeScript
- Vite
- Tailwind CSS
- Shadcn/UI components

#### 2.4 Start Frontend Development Server
```bash
npm run dev
```

**Expected Output:**
```
VITE v5.x.x  ready in xxx ms

➜  Local:   http://localhost:5173/
➜  Network: use --host to expose
```

The frontend will open at `http://localhost:5173`

---

### Step 3: LLaMA AI Setup (Optional but Recommended)

For AI-powered skill-gap explanation and learning roadmap generation:

#### 3.1 Install Ollama

**Windows:**
1. Download from [ollama.ai](https://ollama.ai/download)
2. Run the installer
3. Ollama will start automatically

**Linux/Mac:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

#### 3.2 Download LLaMA Model
```bash
ollama pull llama2
```

**Alternative Models:**
- `ollama pull llama3` (More advanced, larger size)
- `ollama pull mistral` (Faster, smaller size)

#### 3.3 Verify Installation
```bash
ollama list
```

Should show installed models.

#### 3.4 Update Backend Configuration (Optional)
If using a different model, edit `backend/main.py`:
```python
LLAMA_MODEL = "llama3"  # Change to your model
```

**Note:** The system works without LLaMA but uses template-based responses instead of AI-generated ones.

---

## 🧪 Testing the System

### 1. Health Check
Open browser and visit: `http://localhost:5000/api/health`

**Expected Response:**
```json
{
  "status": "healthy",
  "message": "Flask backend is running",
  "ml_model": "Random Forest Classifier",
  "ml_model_trained": true,
  "llama_available": true,
  "llama_model": "llama2"
}
```

### 2. Test Frontend
1. Open `http://localhost:5173` in your browser
2. You should see the career recommendation interface
3. Select some skills (e.g., Python, Machine Learning)
4. Click "Get Recommendations"
5. View predicted career paths

### 3. Test Career Prediction
Select skills like:
- Python
- Machine Learning
- TensorFlow
- Data Analysis

Expected prediction: **Machine Learning Engineer** or **Data Scientist**

### 4. Test Skill-Gap Analysis
1. Select your current skills
2. Choose a target career role
3. View missing skills and match percentage
4. Read AI-generated learning roadmap

---

## 📂 Project Structure

```
-llamacoder/
├── backend/
│   ├── main.py              # Flask application with ML model
│   ├── requirements.txt      # Python dependencies
│   └── README.md
│
├── frontend/
│   ├── src/
│   │   ├── components/       # React components
│   │   ├── services/         # API integration
│   │   └── App.tsx          # Main app component
│   ├── package.json
│   └── README.md
│
├── dataset/
│   ├── job_dataset_text.csv      # Training data (text)
│   ├── job_dataset_encoded.csv   # Training data (binary)
│   └── script/
│       └── generate_dataset.py
│
├── SYSTEM_ARCHITECTURE.md    # Detailed architecture
├── INSTALLATION.md           # This file
└── README.md                 # Project overview
```

---

## 🔧 Configuration

### Environment Variables (Optional)

#### Frontend (.env)
```env
VITE_API_URL=http://localhost:5000/api
```

#### Backend (.env)
```env
FLASK_ENV=development
FLASK_DEBUG=True
PORT=5000
OLLAMA_URL=http://localhost:11434
```

---

## 🐛 Troubleshooting

### Backend Issues

#### Problem: `ModuleNotFoundError: No module named 'flask'`
**Solution:**
```bash
pip install -r requirements.txt
```

#### Problem: `Dataset files not found`
**Solution:**
- Ensure you're running from the correct directory
- Check that `dataset/` folder exists with CSV files

#### Problem: `Port 5000 already in use`
**Solution:**
Edit `main.py` and change port:
```python
app.run(debug=True, port=5001, host='0.0.0.0')
```

### Frontend Issues

#### Problem: `npm install` fails
**Solution:**
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and package-lock.json
rm -rf node_modules package-lock.json

# Reinstall
npm install
```

#### Problem: `Cannot connect to backend`
**Solution:**
- Ensure backend is running on port 5000
- Check `src/services/api.ts` has correct API URL
- Verify CORS is enabled in Flask

### LLaMA Issues

#### Problem: `LLaMA not available`
**Solution:**
- Check if Ollama is running: `ollama list`
- Start Ollama service
- Pull model: `ollama pull llama2`
- Restart backend server

#### Problem: `LLaMA responses are slow`
**Solution:**
- Use smaller model: `ollama pull mistral`
- Reduce `max_tokens` in `main.py`
- Consider GPU acceleration

---

## 📊 Dataset Information

The system uses two dataset files:

### 1. job_dataset_text.csv
- **Format**: skills, num_skills, role
- **Example**:
  ```csv
  skills,num_skills,role
  "Python,Machine Learning,TensorFlow",3,Machine Learning Engineer
  ```

### 2. job_dataset_encoded.csv
- **Format**: 73 skill columns (binary) + 1 role column
- **Example**:
  ```csv
  Python,Java,JavaScript,...,role
  1,0,1,...,Machine Learning Engineer
  ```

**Dataset Statistics:**
- Records: 2000+
- Skills: 73
- Career Roles: 10+
- Encoding: Binary (1=has skill, 0=doesn't have)

---

## 🎯 Using the System

### For Students:

1. **Select Your Skills**
   - Choose from 73+ technical skills
   - Or upload resume for automatic detection

2. **Get Career Predictions**
   - View top 5 recommended career paths
   - See confidence scores for each prediction

3. **Analyze Skill Gaps**
   - Select target career role
   - View missing skills
   - See match percentage

4. **Get Learning Guidance**
   - Read AI-generated skill-gap explanation
   - Follow 6-month learning roadmap
   - Access recommended resources

### For Developers:

#### API Usage Example:
```python
import requests

# Predict career
response = requests.post('http://localhost:5000/api/predict-career', 
    json={'skills': ['Python', 'Machine Learning']})
print(response.json())

# Analyze skill gap
response = requests.post('http://localhost:5000/api/analyze',
    json={
        'skills': ['Python', 'SQL'],
        'target_role': 'Data Scientist'
    })
print(response.json())
```

#### Frontend Integration:
```typescript
import { api } from './services/api';

// Get predictions
const predictions = await api.predictCareer(['Python', 'React']);

// Get AI guidance
const guidance = await api.getCareerGuidance(
    skills, 
    'Software Engineer', 
    missingSkills
);
```

---

## 🔐 Security Notes

- System runs locally by default (localhost)
- No authentication required for development
- For production deployment:
  - Add authentication (JWT recommended)
  - Enable HTTPS
  - Implement rate limiting
  - Add input validation

---

## 📱 Browser Compatibility

- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+

---

## 🚀 Production Deployment

### Backend (Flask)
```bash
# Install production server
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 main:app
```

### Frontend (React)
```bash
# Build for production
npm run build

# Serve with nginx or serve
npm install -g serve
serve -s dist -p 3000
```

---

## 📞 Support & Resources

- **Documentation**: See `SYSTEM_ARCHITECTURE.md`
- **Dataset Scripts**: See `dataset/script/`
- **Issues**: Check troubleshooting section above

---

## ✅ Verification Checklist

- [ ] Python 3.8+ installed
- [ ] Node.js 16+ installed
- [ ] Backend dependencies installed
- [ ] Frontend dependencies installed
- [ ] Backend server running (port 5000)
- [ ] Frontend server running (port 5173)
- [ ] Health check API working
- [ ] Frontend can communicate with backend
- [ ] ML model trained successfully
- [ ] (Optional) Ollama installed and running
- [ ] (Optional) LLaMA model downloaded

---

## 🎉 Success!

If all steps completed successfully, you should have:
- ✅ Backend API running on `http://localhost:5000`
- ✅ Frontend UI running on `http://localhost:5173`
- ✅ Random Forest model trained with 90%+ accuracy
- ✅ (Optional) LLaMA AI providing intelligent guidance

**Your AI-Driven Career Recommendation System is ready to use!**

---

*Last Updated: January 26, 2026*
