import { useState, useEffect } from "react";
import { JobSelector } from "./components/JobSelector";
import { SkillSelector } from "./components/SkillSelector";
import { ResumeUploader } from "./components/ResumeUploader";
import { CareerPath } from "./components/CareerPath";
import { LearningPath } from "./components/LearningPath";
import api from "./services/api";
import { jobRoles } from "./data/jobRoles";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { 
  BarChart3, 
  Users, 
  CheckCircle,
  ArrowRight,
  Sparkles,
  Brain,
  Rocket,
  FileText,
  TrendingUp as TrendingUpIcon,
  Briefcase
} from "lucide-react";

function App() {
  const [selectedJob, setSelectedJob] = useState<string | null>(null);
  const [selectedSkills, setSelectedSkills] = useState<string[]>([]);
  const [detectedRole, setDetectedRole] = useState<string | null>(null);
  const [analysisComplete, setAnalysisComplete] = useState(false);
  const [skillGapResult, setSkillGapResult] = useState<any>(null);

  const handleReset = () => {
    setSelectedJob(null);
    setSelectedSkills([]);
    setAnalysisComplete(false);
    setSkillGapResult(null);
  };

  const handleSkillsFromResume = (skills: string[], roleId?: string) => {
    setSelectedSkills(skills);
    if (roleId) {
      setDetectedRole(roleId);
    } else if (roleId === undefined) {
      // If roleId is explicitly undefined, reset the detected role
      setDetectedRole(null);
    }
  };

  const handleResumeRemoved = () => {
    setDetectedRole(null);
  };

  // Auto-detect role based on selected skills
  const detectRoleFromSkills = (skills: string[]): string | null => {
    if (skills.length === 0) return null;

    let bestMatch = { roleId: null as string | null, matchCount: 0, matchPercentage: 0 };

    jobRoles.forEach(role => {
      const matchingSkills = skills.filter(skill => 
        role.requiredSkills.some(reqSkill => 
          reqSkill.toLowerCase() === skill.toLowerCase()
        )
      );
      const matchPercentage = (matchingSkills.length / role.requiredSkills.length) * 100;
      
      if (matchingSkills.length > bestMatch.matchCount) {
        bestMatch = {
          roleId: role.id,
          matchCount: matchingSkills.length,
          matchPercentage
        };
      }
    });

    return bestMatch.matchCount >= 2 ? bestMatch.roleId : null;
  };

  // Mapping of job roles to roadmap.sh URLs
  const getRoadmapUrl = (jobId: string | null): string => {
    const roadmapUrls: { [key: string]: string } = {
      'frontend-developer': 'https://roadmap.sh/frontend',
      'backend-developer': 'https://roadmap.sh/backend',
      'fullstack-developer': 'https://roadmap.sh/full-stack',
      'data-scientist': 'https://roadmap.sh/data-analyst',
      'devops-engineer': 'https://roadmap.sh/devops',
      'mobile-developer': 'https://roadmap.sh/android',
      'ml-engineer': 'https://roadmap.sh/ai-data-scientist',
      'cloud-engineer': 'https://roadmap.sh/devops',
      'ui-ux-designer': 'https://roadmap.sh/ux-design',
      'cybersecurity-specialist': 'https://roadmap.sh/cyber-security',
      'data-engineer': 'https://roadmap.sh/data-analyst'
    };
    return roadmapUrls[jobId || ''] || 'https://roadmap.sh';
  };

  const handleRoadmapClick = () => {
    // Priority: 1. Detected role from resume, 2. Manually selected job, 3. Auto-detected from skills
    const roleToUse = detectedRole || selectedJob || detectRoleFromSkills(selectedSkills);
    const url = getRoadmapUrl(roleToUse);
    window.open(url, '_blank', 'noopener,noreferrer');
  };

  const handleIndeedClick = () => {
    // Priority: 1. Detected role from resume, 2. Manually selected job, 3. Auto-detected from skills
    const roleToUse = detectedRole || selectedJob || detectRoleFromSkills(selectedSkills);
    
    // Find the job role details
    const jobRole = jobRoles.find(role => role.id === roleToUse);
    const jobTitle = jobRole ? jobRole.title : 'Software Developer';
    
    // Build Indeed search URL with the job title
    const searchQuery = encodeURIComponent(jobTitle);
    const indeedUrl = `https://www.indeed.com/jobs?q=${searchQuery}`;
    
    window.open(indeedUrl, '_blank', 'noopener,noreferrer');
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-50 via-white to-purple-50">
      {/* Header */}
      <div className="bg-white border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="bg-gradient-to-r from-indigo-600 to-purple-600 p-2 rounded-lg">
                <TrendingUpIcon className="w-6 h-6 text-white" />
              </div>
              <div>
                <h1 className="text-2xl font-bold text-gray-900">
                  CareerPath AI
                </h1>
                <p className="text-sm text-gray-600">
                  AI-powered skill gap analysis and personalized career roadmaps
                </p>
              </div>
            </div>
            <div className="flex items-center gap-2">
              <Badge variant="outline" className="bg-green-50 text-green-700 border-green-200">
                <CheckCircle className="w-3 h-3 mr-1" />
                Free Tool
              </Badge>
              <Badge variant="outline" className="bg-indigo-50 text-indigo-700 border-indigo-200">
                <Users className="w-3 h-3 mr-1" />
                50+ Skills
              </Badge>
              <Badge variant="outline" className="bg-purple-50 text-purple-700 border-purple-200">
                <FileText className="w-3 h-3 mr-1" />
                Resume Upload
              </Badge>
            </div>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {!analysisComplete ? (
          <div className="space-y-8">
            {/* Progress Indicator */}
            <div className="flex items-center justify-center mb-8">
              <div className="flex items-center gap-4">
                <div className={`flex items-center gap-2 ${selectedJob ? 'text-indigo-600' : 'text-gray-400'}`}>
                  <div className={`w-8 h-8 rounded-full flex items-center justify-center ${selectedJob ? 'bg-indigo-600 text-white' : 'bg-gray-200'}`}>
                    1
                  </div>
                  <span className="font-medium">Choose Role</span>
                </div>
                <ArrowRight className="w-4 h-4 text-gray-400" />
                <div className={`flex items-center gap-2 ${selectedSkills.length > 0 ? 'text-indigo-600' : 'text-gray-400'}`}>
                  <div className={`w-8 h-8 rounded-full flex items-center justify-center ${selectedSkills.length > 0 ? 'bg-indigo-600 text-white' : 'bg-gray-200'}`}>
                    2
                  </div>
                  <span className="font-medium">Add Skills</span>
                </div>
                <ArrowRight className="w-4 h-4 text-gray-400" />
                <div className={`flex items-center gap-2 ${selectedJob && selectedSkills.length > 0 ? 'text-indigo-600' : 'text-gray-400'}`}>
                  <div className={`w-8 h-8 rounded-full flex items-center justify-center ${selectedJob && selectedSkills.length > 0 ? 'bg-indigo-600 text-white' : 'bg-gray-200'}`}>
                    3
                  </div>
                  <span className="font-medium">Get Results</span>
                </div>
              </div>
            </div>

            {/* Hero Section */}
            <div className="text-center mb-8">
              <h2 className="text-4xl font-bold text-gray-900 mb-4">
                Your AI Career Coach is Here
              </h2>
              <p className="text-xl text-gray-600 max-w-3xl mx-auto">
                Get personalized career guidance powered by AI. Upload your resume, select your target role, and receive a customized learning path to bridge your skill gaps.
              </p>
            </div>

            {/* Job Selection */}
            <JobSelector 
              selectedJob={selectedJob} 
              onJobSelect={setSelectedJob} 
            />

            {/* Resume Upload */}
            <ResumeUploader 
              onSkillsExtracted={handleSkillsFromResume}
              selectedSkills={selectedSkills}
              onResumeRemoved={handleResumeRemoved}
            />

            {/* Skill Selection */}
            <SkillSelector 
              selectedSkills={selectedSkills} 
              onSkillsChange={setSelectedSkills} 
            />

            {/* Analyze Button */}
            <div className="flex justify-center">
              <Button
                onClick={handleRoadmapClick}
                disabled={!selectedJob && !detectedRole && selectedSkills.length === 0}
                size="lg"
                className="bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 text-white px-8 py-3 text-lg font-medium shadow-lg disabled:opacity-50"
              >
                <BarChart3 className="w-5 h-5 mr-2" />
                Generate Career Roadmap
              </Button>
            </div>

            {/* Features Section */}
            <div className="grid md:grid-cols-3 gap-6">
              <Card className="border-indigo-200 bg-indigo-50 hover:shadow-lg transition-shadow">
                <CardHeader className="pb-3">
                  <CardTitle className="text-lg flex items-center gap-2 text-indigo-900">
                    <Brain className="w-5 h-5" />
                    AI-Powered Analysis
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-sm text-indigo-800">
                    Our advanced AI analyzes your skills against industry requirements to identify precise gaps and opportunities for growth.
                  </p>
                </CardContent>
              </Card>

              <Card className="border-purple-200 bg-purple-50 hover:shadow-lg transition-shadow">
                <CardHeader className="pb-3">
                  <CardTitle className="text-lg flex items-center gap-2 text-purple-900">
                    <Sparkles className="w-5 h-5" />
                    Smart Resume Parsing
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-sm text-purple-800">
                    Upload your resume and let our AI extract your skills automatically. Save time and ensure accuracy in your skill assessment.
                  </p>
                </CardContent>
              </Card>

              <Card className="border-green-200 bg-green-50 hover:shadow-lg transition-shadow">
                <CardHeader className="pb-3">
                  <CardTitle className="text-lg flex items-center gap-2 text-green-900">
                    <Rocket className="w-5 h-5" />
                    Actionable Roadmaps
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-sm text-green-800">
                    Receive personalized learning paths with curated resources, timelines, and step-by-step guidance to reach your career goals.
                  </p>
                </CardContent>
              </Card>
            </div>

            {/* Indeed Button */}
            <div className="flex justify-center mt-8">
              <Button
                onClick={handleIndeedClick}
                disabled={selectedSkills.length === 0}
                size="lg"
                className="bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 text-white px-8 py-3 text-lg font-medium shadow-lg disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <Briefcase className="w-5 h-5 mr-2" />
                Indeed
              </Button>
            </div>
          </div>
        ) : (
          <div className="space-y-8">
            {/* Results Header */}
            <div className="text-center mb-8">
              <div className="inline-flex items-center gap-2 bg-green-100 text-green-800 px-4 py-2 rounded-full mb-4">
                <CheckCircle className="w-4 h-4" />
                Career Roadmap Generated
              </div>
              <h2 className="text-3xl font-bold text-gray-900 mb-2">
                Your Personalized Career Path is Ready!
              </h2>
              <p className="text-gray-600">
                CareerPath AI has analyzed your profile and created a customized roadmap to help you achieve your career goals.
              </p>
            </div>

            {/* Career Path Overview */}
            <CareerPath
              role={selectedJob!}
              currentSkills={skillGapResult.currentSkills}
              missingSkills={skillGapResult.missingSkills}
              matchPercentage={skillGapResult.matchPercentage}
              estimatedTime={skillGapResult.estimatedTime}
            />

            {/* Learning Path */}
            {skillGapResult.missingSkills.length > 0 && (
              <LearningPath missingSkills={skillGapResult.missingSkills} />
            )}

            {/* Action Buttons */}
            <div className="flex justify-center gap-4">
              <Button
                onClick={handleReset}
                variant="outline"
                size="lg"
                className="px-8"
              >
                Analyze Another Career Path
              </Button>
            </div>
          </div>
        )}
      </div>

      {/* Footer */}
      <div className="bg-white border-t border-gray-200 mt-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div className="text-center text-gray-600">
            <div className="flex items-center justify-center gap-2 mb-2">
              <TrendingUpIcon className="w-5 h-5 text-indigo-600" />
              <span className="font-semibold text-gray-900">CareerPath AI</span>
            </div>
            <p className="text-sm">
              🚀 Transform your career with AI-powered guidance
            </p>
            <p className="text-xs mt-2">
              Built with React, TypeScript, and Tailwind CSS
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;