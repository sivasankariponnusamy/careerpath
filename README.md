# AI-Powered Career Guidance & Skill Gap Analyzer

An intelligent career guidance system that uses Machine Learning for skill gap analysis and AI (LLaMA) for personalized career roadmap recommendations.

## 🎯 Project Overview

This project helps users:
- Analyze their skill gaps for desired career roles
- Get personalized career recommendations based on their current skills
- Receive AI-powered career guidance and learning roadmaps
- Access curated learning resources for skill development

## 🏗️ Architecture

```
User (Frontend)
    ↓
React Application (UI/UX)
    ↓
Flask Backend API
    ↓
ML Model (Scikit-learn) → Skill Gap Analysis
    ↓
LLaMA AI → Career Guidance & Roadmap
    ↓
Dataset (CSV) → 2000+ skill-role combinations
```

## 📁 Project Structure

```
-llamacoder/
├── frontend/               # React frontend application
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── data/          # Static data files
│   │   ├── hooks/         # Custom React hooks
│   │   ├── services/      # API service layer
│   │   ├── types/         # TypeScript types
│   │   └── utils/         # Utility functions
│   ├── package.json
│   └── README.md
│
├── backend/               # Flask backend API
│   ├── app.py            # Main Flask application
│   ├── requirements.txt   # Python dependencies
│   └── README.md
│
└── dataset/              # Training datasets
    ├── job_dataset_text.csv      # Skills and roles (text format)
    ├── job_dataset_encoded.csv   # Encoded features for ML
    └── script/
        └── generate_dataset.py   # Dataset generation script
```

## 🛠️ Technology Stack

### Frontend
- **React 18** - UI Framework
- **TypeScript** - Type safety
- **Vite** - Build tool
- **Tailwind CSS** - Styling
- **Shadcn/UI** - Component library

### Backend
- **Python 3.x** - Programming language
- **Flask** - Web framework
- **Flask-CORS** - Cross-origin resource sharing

### Machine Learning
- **Scikit-learn** - ML algorithms
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Cosine Similarity** - Skill matching algorithm

### AI Integration
- **LLaMA** - AI-powered career guidance (integration ready)

### Dataset
- **2000+ Records** - Skill-role combinations
- **73 Skills** - Comprehensive skill coverage
- **Multiple Roles** - Various tech career paths

## 🚀 Getting Started

### Prerequisites
- **Node.js** (v16 or higher)
- **Python** (v3.8 or higher)
- **npm** or **yarn**

### Installation

#### 1. Clone the repository
```bash
cd -llamacoder
```

#### 2. Setup Backend
```bash
cd backend
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run backend server
python app.py
```
Backend will run on `http://localhost:5000`

#### 3. Setup Frontend
```bash
cd frontend
npm install
npm run dev
```
Frontend will run on `http://localhost:5173`

### 4. Access the Application
Open your browser and navigate to `http://localhost:5173`

## 📊 Dataset Information

The project uses two datasets:

1. **job_dataset_text.csv**: Contains skill names and job roles in text format
   - 2000+ records
   - Skills, number of skills, and corresponding roles

2. **job_dataset_encoded.csv**: Binary encoded features for ML model
   - 73 skill columns (binary: 0 or 1)
   - Role column for classification

## 🧠 Machine Learning Model

### Algorithm: Cosine Similarity
- Measures similarity between user skills and role requirements
- Calculates skill gap percentage
- Identifies missing and matching skills

### Features:
- **Skill Gap Analysis**: Quantifies how well skills match a role
- **Role Recommendation**: Suggests best-matching career paths
- **Skill Prioritization**: Ranks skills by importance

## 🤖 AI Integration (LLaMA)

The system includes integration points for LLaMA AI to provide:
- Personalized learning roadmaps
- Career transition guidance
- Skill development strategies
- Industry-specific recommendations

**Note**: LLaMA integration is currently using template-based responses. To enable full AI features, configure LLaMA API in `backend/app.py`.

## 📡 API Endpoints

### Backend API Routes

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/health` | Health check |
| GET | `/api/skills` | Get all available skills |
| GET | `/api/roles` | Get all job roles |
| POST | `/api/analyze` | Analyze skill gap for a role |
| POST | `/api/recommend` | Get role recommendations |
| POST | `/api/career-guidance` | Get AI career guidance |

## 🎨 Features

### Current Features
- ✅ Skill selection interface
- ✅ Career path recommendations
- ✅ Skill gap analysis with ML
- ✅ Match percentage calculation
- ✅ Missing skills identification
- ✅ Learning roadmap generation
- ✅ Interactive UI with modern design

### Coming Soon
- 📄 Resume parsing and skill extraction
- 🤖 Full LLaMA AI integration
- 💬 Chatbot for career queries
- 📱 Mobile application
- 🔗 Job portal integration
- 📊 Advanced analytics dashboard

## ✨ Advantages

- **Personalized Guidance**: Tailored recommendations based on individual skills
- **Industry-Oriented**: Real-world skill requirements from actual job roles
- **AI-Powered**: Intelligent career roadmap generation
- **Easy to Use**: Intuitive interface requiring no technical knowledge
- **Data-Driven**: ML-based analysis ensures accuracy
- **Comprehensive**: Covers 73+ skills across multiple tech domains

## ⚠️ Limitations

- Limited to predefined skill set (73 skills)
- No real-time job market data
- Text-based guidance (voice support coming soon)
- Requires internet connection for API calls

## 🔮 Future Enhancements

1. **Job Portal Integration**: Real-time job matching
2. **Resume Parser**: Automatic skill extraction from resumes
3. **Interactive Chatbot**: Real-time Q&A with AI
4. **Mobile App**: iOS and Android applications
5. **Advanced Analytics**: Skill trend analysis and predictions
6. **Video Tutorials**: Integrated learning content
7. **Community Forum**: Connect with peers and mentors

## 🔐 Ethical AI Statement

This project respects user privacy and data security:
- No personal data is stored permanently
- AI provides supportive, not prescriptive, guidance
- Transparent about AI limitations
- Promotes inclusive career opportunities
- Respects user autonomy in career decisions

## 📝 Module Wise Explanation

### Module 1: User Interface (Frontend)
- Skill selection component
- Career path visualizer
- Skill gap display
- Interactive charts and progress bars

### Module 2: Skill Gap Analyzer (ML Model)
- Cosine similarity calculation
- Feature vector comparison
- Gap percentage computation

### Module 3: Career Recommendation Engine
- Role matching algorithm
- Top-N recommendations
- Confidence scoring

### Module 4: AI Career Guidance (LLaMA)
- Roadmap generation
- Learning phase planning
- Resource recommendations

### Module 5: API Layer (Flask Backend)
- RESTful API endpoints
- Request validation
- Error handling
- CORS support

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed for educational purposes.

## 🎓 Academic Project

This is a student project demonstrating:
- Full-stack development
- Machine Learning integration
- AI-powered applications
- Modern web technologies
- Software engineering best practices

## 📧 Support

For questions or support, please open an issue in the repository.

---

**Built with ❤️ for helping people find their ideal career path**
