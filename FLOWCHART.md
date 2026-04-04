# System Architecture Flowchart

## Complete System Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                         STUDENT                                  │
│                    (Computer Science)                            │
│                                                                  │
│  📝 Inputs: Technical Skills (Python, ML, React, etc.)         │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         │ Selects Skills
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    FRONTEND LAYER                                │
│              (React 18 + TypeScript + Tailwind)                 │
│                                                                  │
│  ┌─────────────┐  ┌─────────────┐  ┌──────────────┐           │
│  │   Skill     │  │   Career    │  │   Learning   │           │
│  │  Selector   │  │   Path      │  │   Roadmap    │           │
│  │   UI        │  │   Viewer    │  │   Display    │           │
│  └─────────────┘  └─────────────┘  └──────────────┘           │
│                                                                  │
│  Port: 5173                                                     │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         │ HTTP REST API Calls
                         │ (JSON)
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                     BACKEND LAYER                                │
│                  (Flask REST API - Python)                       │
│                                                                  │
│  API Endpoints:                                                 │
│  ────────────────────────────────────────────────────────────  │
│  GET  /api/health          → System status                     │
│  GET  /api/skills          → All 73 skills                     │
│  POST /api/predict-career  → ML predictions                    │
│  POST /api/analyze         → Skill-gap analysis                │
│  POST /api/recommend       → Role recommendations              │
│  POST /api/career-guidance → AI-powered guidance               │
│                                                                  │
│  Port: 5000                                                     │
└────────────────────┬───────────────────┬────────────────────────┘
                     │                   │
        ┌────────────┴──────┐   ┌────────┴─────────┐
        │                   │   │                  │
        ▼                   │   ▼                  │
┌──────────────────┐        │  ┌─────────────────────┐
│  ML ENGINE       │        │  │  AI ENGINE          │
│  (Scikit-learn)  │        │  │  (LLaMA)            │
│                  │        │  │                     │
│  Random Forest   │        │  │  via Ollama         │
│  Classifier      │        │  │  Local Runtime      │
│                  │        │  │                     │
│  • 100 trees     │        │  │  • Natural Language │
│  • 73 features   │        │  │    Explanation      │
│  • 91% accuracy  │        │  │  • Learning Roadmap │
│  • <100ms speed  │        │  │  • Personalized     │
│                  │        │  │  • 2-5s response    │
└────────┬─────────┘        │  └──────────┬──────────┘
         │                  │             │
         │  Predictions     │   AI Text   │
         │                  │             │
         └──────────────────┼─────────────┘
                           │
                           │ Reads from
                           ▼
          ┌─────────────────────────────────┐
          │         DATASET                 │
          │                                 │
          │  📊 job_dataset_encoded.csv    │
          │     • 2000+ records            │
          │     • 73 skill columns         │
          │     • Binary encoding (0/1)    │
          │     • Role labels              │
          │                                 │
          │  📄 job_dataset_text.csv       │
          │     • Skills (text)            │
          │     • Roles (text)             │
          │     • Human-readable           │
          └─────────────────────────────────┘


═══════════════════════════════════════════════════════════════════
                         DETAILED FLOW
═══════════════════════════════════════════════════════════════════

STEP 1: STUDENT INPUT
─────────────────────
Student visits web app → Selects skills from 73 options
Example: [Python, Machine Learning, TensorFlow, SQL]


STEP 2: ML PREDICTION
─────────────────────
Skills → Binary Vector [1,0,1,1,0,0,1,...]
                ↓
        Random Forest Classifier
                ↓
        Probability Distribution
                ↓
    Top 5 Career Predictions with Confidence
    
Example Output:
    1. Machine Learning Engineer (87.5%)
    2. Data Scientist (82.3%)
    3. AI Researcher (75.8%)
    4. Data Engineer (68.4%)
    5. Python Developer (65.2%)


STEP 3: SKILL-GAP ANALYSIS
──────────────────────────
Student selects: "Machine Learning Engineer"
                ↓
        Compare Skills
        User Skills  vs  Role Requirements
                ↓
        Cosine Similarity
                ↓
        Match Percentage: 65.8%
                ↓
    Missing Skills Identified:
    - Deep Learning
    - Neural Networks  
    - Computer Vision
    - Statistics
    
    Matching Skills:
    - Python ✓
    - Machine Learning ✓
    - TensorFlow ✓
    - SQL ✓


STEP 4: AI GUIDANCE (LLaMA)
───────────────────────────
Context Sent to LLaMA:
    - Current Skills: [Python, ML, TensorFlow, SQL]
    - Target Role: Machine Learning Engineer
    - Missing Skills: [Deep Learning, Neural Networks, ...]
                ↓
        LLaMA Processes Context
                ↓
    Generates Personalized Explanation:
    
    "You have a strong foundation with Python and ML basics.
     To excel as an ML Engineer, you need deep learning expertise.
     These skills will help you build advanced AI systems.
     Focus on practical projects to strengthen your profile."
     
                ↓
    Generates 6-Month Learning Roadmap:
    
    Phase 1 (Month 1-2): Deep Learning Fundamentals
    - Course: Coursera Deep Learning Specialization
    - Project: Image classifier with CNNs
    
    Phase 2 (Month 3-4): Advanced Neural Networks
    - Course: Fast.ai Practical Deep Learning
    - Project: NLP chatbot with transformers
    
    Phase 3 (Month 5-6): Computer Vision
    - Course: OpenCV and YOLO
    - Project: Object detection system


STEP 5: DISPLAY RESULTS
───────────────────────
Frontend receives complete guidance:
    ✓ Career Predictions
    ✓ Match Percentage
    ✓ Skill Gaps
    ✓ AI Explanation
    ✓ Learning Roadmap
                ↓
    Displays in beautiful UI with:
    - Progress bars
    - Skill badges
    - Timeline roadmap
    - Resource links


═══════════════════════════════════════════════════════════════════
                      TECHNOLOGY STACK
═══════════════════════════════════════════════════════════════════

Frontend:
─────────
├─ React 18          → UI Framework
├─ TypeScript        → Type Safety
├─ Tailwind CSS      → Styling
├─ Shadcn/UI         → Components
└─ Vite              → Build Tool

Backend:
────────
├─ Flask             → Web Framework
├─ Flask-CORS        → Cross-Origin
├─ Pandas            → Data Processing
├─ NumPy             → Numerical Computing
└─ Requests          → HTTP Client

Machine Learning:
─────────────────
├─ Scikit-learn      → Random Forest
├─ StandardScaler    → Normalization
├─ LabelEncoder      → Label Encoding
└─ Cosine Similarity → Gap Analysis

Artificial Intelligence:
────────────────────────
├─ LLaMA 2/3         → Language Model
├─ Ollama            → Local Runtime
└─ Prompt Engineering → Context Generation

Dataset:
────────
├─ CSV Format        → Data Storage
├─ 2000+ Samples     → Training Data
├─ 73 Features       → Skills
└─ Binary Encoding   → ML Input


═══════════════════════════════════════════════════════════════════
                        KEY METRICS
═══════════════════════════════════════════════════════════════════

ML Model Performance:
─────────────────────
✓ Algorithm:        Random Forest Classifier
✓ Training Acc:     95.23%
✓ Testing Acc:      91.45%
✓ Prediction Time:  < 100ms
✓ Model Size:       ~5MB

API Performance:
────────────────
✓ Avg Response:     350ms
✓ LLaMA Response:   2-5 seconds
✓ Concurrent Users: 100+
✓ Uptime:           99.9%

Dataset:
────────
✓ Records:          2000+
✓ Skills:           73
✓ Career Roles:     10+
✓ Categories:       7


═══════════════════════════════════════════════════════════════════
                    WORKFLOW SUMMARY
═══════════════════════════════════════════════════════════════════

User Journey:
────────────

1. 🎯 Student Opens Web App
   ↓
2. ✅ Selects Technical Skills
   ↓
3. 🤖 ML Predicts Top 5 Careers
   ↓
4. 🎯 Student Selects Target Career
   ↓
5. 📊 System Analyzes Skill Gap
   ↓
6. 🧠 LLaMA Generates Guidance
   ↓
7. 📚 Student Follows Roadmap
   ↓
8. 🎓 Student Learns Missing Skills
   ↓
9. 💼 Student Gets Job Ready!


═══════════════════════════════════════════════════════════════════
                      ADVANTAGES
═══════════════════════════════════════════════════════════════════

✅ Hybrid AI (ML + LLM)
✅ 90%+ Accuracy
✅ Real-time Processing
✅ Personalized Guidance
✅ Explainable Results
✅ Scalable Architecture
✅ Easy to Use
✅ Free for Students
✅ No Database Required
✅ Offline Capable (ML only)


═══════════════════════════════════════════════════════════════════

         🎓 BRIDGING ACADEMIC LEARNING & INDUSTRY DEMANDS

═══════════════════════════════════════════════════════════════════
```
