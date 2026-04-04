# Backend - Flask API with ML Model

## Setup Instructions

### 1. Create Virtual Environment
```bash
cd backend
python -m venv venv
```

### 2. Activate Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Server
```bash
python app.py
```

The backend will run on `http://localhost:5000`

## API Endpoints

### 1. Health Check
- **GET** `/api/health`
- Check if the server is running

### 2. Get All Skills
- **GET** `/api/skills`
- Returns list of all available skills

### 3. Get All Roles
- **GET** `/api/roles`
- Returns list of all job roles

### 4. Analyze Skill Gap
- **POST** `/api/analyze`
- Body: `{"skills": ["Python", "SQL"], "target_role": "Data Scientist"}`
- Returns skill gap analysis

### 5. Recommend Roles
- **POST** `/api/recommend`
- Body: `{"skills": ["Python", "SQL"], "top_n": 5}`
- Returns top matching roles

### 6. Career Guidance
- **POST** `/api/career-guidance`
- Body: `{"skills": [...], "target_role": "...", "missing_skills": [...]}`
- Returns AI-generated career guidance (LLaMA integration point)

## ML Model

The backend uses **scikit-learn** for:
- Cosine similarity calculation
- Skill matching algorithms
- Role recommendation system

## LLaMA Integration

To integrate LLaMA for career guidance:
1. Update the `generate_career_roadmap()` function
2. Add LLaMA API endpoint configuration
3. Install required LLaMA dependencies
