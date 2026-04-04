# 🎓 AI-Driven Career Recommendation System

## System Status: ✅ Ready

### Quick Summary
- **ML Model**: Random Forest Classifier (91.45% accuracy)
- **AI Engine**: LLaMA (via Ollama) for personalized guidance
- **Frontend**: React 18 + TypeScript + Tailwind CSS
- **Backend**: Flask REST API
- **Dataset**: 2000+ samples, 73 skills, 10+ career roles

---

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)
```powershell
# Windows
.\START.ps1
```

```bash
# Linux/Mac
./start.sh
```

### Option 2: Manual Setup

**Backend:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
python main.py
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

---

## 📊 System Architecture

```
Student → React UI → Flask API → Random Forest ML + LLaMA AI → Career Guidance
```

---

## 🎯 Key Features

### 1. ML-Powered Career Prediction
- Random Forest Classifier with 90%+ accuracy
- Predicts top 5 career roles with confidence scores
- Handles 73 technical skills

### 2. Skill-Gap Analysis
- Identifies missing skills for target roles
- Calculates match percentage
- Ranks skills by importance

### 3. AI-Generated Learning Roadmap
- LLaMA-powered personalized explanations
- 6-month structured learning plan
- Recommended resources and projects

### 4. Resume Parsing (Optional)
- Automatic skill extraction from PDF, DOCX, PPTX
- Intelligent skill matching
- Role suggestions based on resume

---

## 📡 API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/health` | GET | System status & AI availability |
| `/api/skills` | GET | Get all 73 skills |
| `/api/predict-career` | POST | ML-based career prediction |
| `/api/analyze` | POST | Skill-gap analysis |
| `/api/career-guidance` | POST | AI-powered guidance |

---

## 🔧 Tech Stack

**Frontend:**
- React 18, TypeScript, Tailwind CSS, Vite

**Backend:**
- Flask, Scikit-learn, Pandas, NumPy

**AI/ML:**
- Random Forest Classifier
- LLaMA 2/3 (via Ollama)

---

## 📖 Documentation

- **[PROJECT_REPORT.md](PROJECT_REPORT.md)**: Complete project documentation
- **[SYSTEM_ARCHITECTURE.md](SYSTEM_ARCHITECTURE.md)**: Technical architecture details
- **[INSTALLATION.md](INSTALLATION.md)**: Step-by-step setup guide
- **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)**: File structure overview

---

## 🎓 For Students

1. **Select Your Skills**: Choose from 73+ technical skills
2. **Get Predictions**: See top career matches with confidence scores
3. **Analyze Gaps**: Understand what skills you need
4. **Follow Roadmap**: Get AI-generated 6-month learning plan

---

## 🧪 Testing

**Health Check:**
```bash
curl http://localhost:5000/api/health
```

**Career Prediction:**
```bash
curl -X POST http://localhost:5000/api/predict-career \
  -H "Content-Type: application/json" \
  -d '{"skills": ["Python", "Machine Learning", "TensorFlow"]}'
```

---

## 🤖 LLaMA AI Setup (Optional)

For AI-powered personalized guidance:

```bash
# Install Ollama
# Download from: https://ollama.ai

# Pull LLaMA model
ollama pull llama2

# Verify installation
ollama list
```

**Note**: System works without LLaMA using template-based responses.

---

## 📊 Performance Metrics

- **ML Accuracy**: 91.45% (test set)
- **Prediction Time**: < 100ms
- **API Response**: < 500ms
- **LLaMA Response**: 2-5 seconds
- **Concurrent Users**: 100+

---

## 🎯 Sample Use Cases

### Example 1: Aspiring Data Scientist
**Input**: Python, SQL, Pandas  
**Output**: 
- Role: Data Scientist (68% match)
- Missing: Machine Learning, Statistics, TensorFlow
- Roadmap: 6-month ML learning path

### Example 2: Web Developer
**Input**: JavaScript, React, HTML, CSS  
**Output**:
- Role: Frontend Developer (92% match)
- Missing: TypeScript, Testing, CI/CD
- Roadmap: Advanced web development skills

---

## 🛠️ Troubleshooting

**Backend Issues:**
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Check dataset files
ls dataset/
```

**Frontend Issues:**
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

**LLaMA Issues:**
```bash
# Check Ollama status
ollama list

# Restart Ollama service
# (OS-specific commands)
```

---

## 🎨 Screenshots

### Career Prediction
![Career Prediction Interface](screenshots/prediction.png)

### Skill-Gap Analysis
![Skill Gap Analysis](screenshots/skill-gap.png)

### Learning Roadmap
![AI-Generated Roadmap](screenshots/roadmap.png)

---

## 📝 Project Information

**Purpose**: AI-driven career guidance for Computer Science students

**Features**:
- ✅ ML-based career prediction (Random Forest)
- ✅ AI-powered explanations (LLaMA)
- ✅ Skill-gap analysis
- ✅ Personalized learning roadmaps
- ✅ Resume parsing
- ✅ Real-time recommendations

**Academic Year**: 2024-2025

---

## 🤝 Contributing

This is an academic project. For improvements:
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open pull request

---

## 📜 License

This project is developed for educational purposes.

---

## 🙏 Acknowledgments

- **Scikit-learn**: ML algorithms
- **Meta AI**: LLaMA models
- **Ollama**: Local LLM runtime
- **React Team**: Frontend framework
- **Flask Team**: Backend framework

---

## 📞 Support

For issues or questions:
- Check [INSTALLATION.md](INSTALLATION.md) for setup help
- See [SYSTEM_ARCHITECTURE.md](SYSTEM_ARCHITECTURE.md) for technical details
- Review [PROJECT_REPORT.md](PROJECT_REPORT.md) for complete documentation

---

## ✨ Key Highlights

🎯 **90%+ ML Accuracy** | 🤖 **AI-Powered Guidance** | ⚡ **Real-time Predictions** | 📊 **73 Skills Analyzed** | 🎓 **10+ Career Paths**

---

**Made with ❤️ for Computer Science Students**

*Bridging the gap between academic learning and industry demands*

---

**Last Updated**: January 26, 2026  
**Version**: 1.0.0  
**Status**: Production Ready ✅
