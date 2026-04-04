# Frontend - React Application

## Setup Instructions

### 1. Navigate to frontend directory
```bash
cd frontend
```

### 2. Install Dependencies
```bash
npm install
```

### 3. Environment Setup
Create a `.env` file in the frontend directory:
```
VITE_API_URL=http://localhost:5000/api
```

### 4. Run Development Server
```bash
npm run dev
```

The frontend will run on `http://localhost:5173`

### 5. Build for Production
```bash
npm run build
```

## Features

- **Skill Selection**: Choose your current skills from the comprehensive list
- **Resume Upload**: Upload resume for automatic skill extraction (coming soon)
- **Career Path Analysis**: See recommended career paths based on your skills
- **Skill Gap Analysis**: Identify missing skills for target roles
- **AI Career Guidance**: Get personalized learning roadmap from LLaMA AI
- **Learning Resources**: Access curated learning resources for each skill

## Technology Stack

- **React 18**: UI framework
- **TypeScript**: Type-safe development
- **Vite**: Fast build tool
- **Tailwind CSS**: Styling
- **Shadcn/UI**: Component library

## API Integration

The frontend connects to the Flask backend at `http://localhost:5000/api` for:
- Skill analysis
- Role recommendations
- Career guidance
- ML-powered skill gap calculation
