# Project Structure

```
-llamacoder/
│
├── frontend/                      # React Frontend Application
│   ├── src/
│   │   ├── components/            # React components
│   │   │   ├── ui/               # Shadcn UI components
│   │   │   ├── CareerPath.tsx    # Career path visualization
│   │   │   ├── JobSelector.tsx   # Job role selector
│   │   │   ├── LearningPath.tsx  # Learning roadmap display
│   │   │   ├── ResumeUploader.tsx # Resume upload component
│   │   │   ├── SkillGapAnalysis.tsx # Skill gap analysis display
│   │   │   ├── SkillList.tsx     # Skill list display
│   │   │   └── SkillSelector.tsx # Skill selection interface
│   │   │
│   │   ├── data/                 # Static data files
│   │   │   ├── assessmentQuestions.ts
│   │   │   ├── jobRoles.ts
│   │   │   ├── skillResources.ts
│   │   │   └── skills.ts
│   │   │
│   │   ├── hooks/                # Custom React hooks
│   │   │   └── useSkillAssessment.ts
│   │   │
│   │   ├── services/             # API service layer
│   │   │   └── api.ts            # Flask API integration
│   │   │
│   │   ├── types/                # TypeScript type definitions
│   │   │   └── index.ts
│   │   │
│   │   ├── utils/                # Utility functions
│   │   │   └── skillGapCalculator.ts
│   │   │
│   │   ├── App.tsx               # Main application component
│   │   ├── main.tsx              # Application entry point
│   │   └── index.css             # Global styles
│   │
│   ├── public/                   # Static assets
│   ├── .env                      # Environment variables
│   ├── package.json              # Frontend dependencies
│   ├── tsconfig.json             # TypeScript configuration
│   ├── vite.config.ts            # Vite build configuration
│   ├── tailwind.config.js        # Tailwind CSS configuration
│   └── README.md                 # Frontend documentation
│
├── backend/                       # Flask Backend API
│   ├── app.py                    # Main Flask application
│   │                            # - ML Model (Scikit-learn)
│   │                            # - API endpoints
│   │                            # - LLaMA integration
│   │
│   ├── requirements.txt          # Python dependencies
│   └── README.md                 # Backend documentation
│
├── dataset/                      # Training Data
│   ├── job_dataset_text.csv     # Skills and roles (text format)
│   │                            # - 2000+ records
│   │                            # - Skills, num_skills, role
│   │
│   ├── job_dataset_encoded.csv  # Encoded features for ML
│   │                            # - 73 skill columns (binary)
│   │                            # - Role column
│   │
│   └── script/
│       └── generate_dataset.py  # Dataset generation script
│
├── README.md                     # Main project documentation
├── QUICKSTART.md                 # Quick start guide
├── PROJECT_STRUCTURE.md          # This file
├── start.bat                     # Windows startup script
└── start.sh                      # Linux/Mac startup script
```

## Component Details

### Frontend Components

**UI Components** (frontend/src/components/ui/)
- `button.tsx` - Reusable button component
- `card.tsx` - Card container component
- `badge.tsx` - Badge/tag component
- `progress.tsx` - Progress bar component
- `input.tsx` - Input field component

**Feature Components** (frontend/src/components/)
- `CareerPath.tsx` - Displays career path recommendations
- `JobSelector.tsx` - Job role selection interface
- `LearningPath.tsx` - Shows personalized learning roadmap
- `ResumeUploader.tsx` - Resume upload and parsing
- `SkillGapAnalysis.tsx` - Visualizes skill gaps
- `SkillList.tsx` - Lists skills with tags
- `SkillSelector.tsx` - Multi-select skill picker

### Backend Structure

**app.py** contains:
- `SkillGapAnalyzer` class
  - `_create_role_profiles()` - Creates average skill profiles
  - `analyze_skill_gap()` - Analyzes skill gaps using ML
  - `recommend_roles()` - Recommends matching roles
  
- API Endpoints:
  - GET `/api/health` - Health check
  - GET `/api/skills` - Get all skills
  - GET `/api/roles` - Get all roles
  - POST `/api/analyze` - Analyze skill gap
  - POST `/api/recommend` - Get recommendations
  - POST `/api/career-guidance` - Get AI guidance

### Data Flow

```
User Input (Frontend)
      ↓
API Service Layer (api.ts)
      ↓
Flask Backend (app.py)
      ↓
ML Model (Scikit-learn)
      ↓
Cosine Similarity Calculation
      ↓
Response (JSON)
      ↓
Frontend Components
      ↓
User Display
```

## File Sizes

- **Frontend**: ~50-100 files (with node_modules)
- **Backend**: ~5 files
- **Dataset**: 2 CSV files (~2MB total)
- **Documentation**: 4 markdown files

## Technology Stack by Layer

### Frontend Layer
- React 18 - UI Framework
- TypeScript - Type Safety
- Vite - Build Tool
- Tailwind CSS - Styling
- Shadcn/UI - Components

### Backend Layer
- Flask - Web Framework
- Flask-CORS - CORS Support
- Pandas - Data Processing
- NumPy - Numerical Computing
- Scikit-learn - ML Algorithms

### Data Layer
- CSV Files - Dataset Storage
- Cosine Similarity - Skill Matching
- Binary Encoding - Feature Representation

## Startup Flow

1. **Backend Initialization**
   - Load CSV datasets
   - Create role profiles
   - Initialize ML model
   - Start Flask server (port 5000)

2. **Frontend Initialization**
   - Load React application
   - Check backend health
   - Initialize API client
   - Start dev server (port 5173)

3. **User Workflow**
   - Select job role
   - Choose/upload skills
   - Request analysis
   - View results
   - Get learning roadmap
