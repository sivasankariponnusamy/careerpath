// API Configuration
const API_BASE_URL = import.meta.env.VITE_API_URL || 'https://backend-careerpath-ai.vercel.app/api';

export const apiClient = {
  async get(endpoint: string) {
    const response = await fetch(`${API_BASE_URL}${endpoint}`);
    if (!response.ok) {
      throw new Error(`API Error: ${response.statusText}`);
    }
    return response.json();
  },

  async post(endpoint: string, data: any) {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
    if (!response.ok) {
      throw new Error(`API Error: ${response.statusText}`);
    }
    return response.json();
  },

  async delete(endpoint: string) {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      method: 'DELETE',
    });
    if (!response.ok) {
      throw new Error(`API Error: ${response.statusText}`);
    }
    return response.json();
  },
};

// API Methods
export const api = {
  // Health check
  healthCheck: () => apiClient.get('/health'),

  // Get all available skills
  getAllSkills: () => apiClient.get('/skills'),

  // Get all job roles
  getAllRoles: () => apiClient.get('/roles'),

  // Predict career using ML model
  predictCareer: (skills: string[]) =>
    apiClient.post('/predict-career', { skills }),

  // Analyze skill gap
  analyzeSkillGap: (skills: string[], targetRole: string) =>
    apiClient.post('/analyze', { skills, target_role: targetRole }),

  // Get role recommendations (uses ML model)
  getRecommendations: (skills: string[], topN: number = 5) =>
    apiClient.post('/recommend', { skills, top_n: topN }),

  // Get AI-powered career guidance (uses LLaMA)
  getCareerGuidance: (skills: string[], targetRole: string, missingSkills: string[]) =>
    apiClient.post('/career-guidance', { skills, target_role: targetRole, missing_skills: missingSkills }),

  // Resume Management APIs
  getAllResumes: (limit: number = 50) =>
    apiClient.get(`/resumes?limit=${limit}`),

  getResume: (resumeId: number) =>
    apiClient.get(`/resumes/${resumeId}`),

  downloadResume: (resumeId: number) => {
    window.open(`${API_BASE_URL}/resumes/${resumeId}/download`, '_blank');
  },

  deleteResume: (resumeId: number) =>
    apiClient.delete(`/resumes/${resumeId}`),

  getResumeStats: () =>
    apiClient.get('/resumes/stats'),

  // Skill Gap Analysis APIs
  getAllAnalyses: (limit: number = 50) =>
    apiClient.get(`/skill-gap-analyses?limit=${limit}`),

  saveAnalysis: (analysisData: any) =>
    apiClient.post('/skill-gap-analyses', analysisData),
};

export default api;
