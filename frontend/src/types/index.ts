export interface JobRole {
  id: string;
  title: string;
  description: string;
  requiredSkills: string[];
  averageSalary?: string;
  growthRate?: string;
  difficulty?: 'Beginner' | 'Intermediate' | 'Advanced';
  jobSearchLinks?: JobSearchLink[];
  careerResources?: CareerResource[];
}

export interface JobSearchLink {
  platform: string;
  url: string;
  description: string;
}

export interface CareerResource {
  title: string;
  url: string;
  description: string;
}

export interface Skill {
  name: string;
  category: string;
  difficulty: 'Beginner' | 'Intermediate' | 'Advanced';
  description?: string;
  prerequisites?: string[];
}

export interface Resource {
  title: string;
  url: string;
  description: string;
  level: string;
  duration: string;
  rating: string;
  type: ResourceType;
  tags?: string[];
  prerequisites?: string[];
}

export interface SkillResources {
  skill: string;
  resources: Resource[];
}

export interface UserSkill {
  name: string;
  proficiency: 1 | 2 | 3 | 4 | 5; // 1-5 rating
  experience: string; // e.g., "6 months", "2 years"
  lastUsed?: string;
}

export interface LearningProgress {
  skill: string;
  resource: string;
  progress: number; // 0-100
  startedAt?: Date;
  completedAt?: Date;
  notes?: string;
}

export interface CareerPath {
  role: string;
  currentSkills: string[];
  missingSkills: string[];
  totalSkills: number;
  matchPercentage: number;
  estimatedTime: string;
  difficulty: 'Easy' | 'Medium' | 'Hard';
  recommendedOrder: string[];
}

export interface AssessmentQuestion {
  id: string;
  skill: string;
  question: string;
  options: string[];
  correctAnswer: number;
  difficulty: 'Beginner' | 'Intermediate' | 'Advanced';
  explanation: string;
}

export interface SkillAssessment {
  skill: string;
  score: number;
  level: 'Beginner' | 'Intermediate' | 'Advanced';
  recommendations: string[];
  nextSteps: string[];
}

export type ResourceType = 'article';