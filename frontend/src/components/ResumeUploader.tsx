import { useState, useRef } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Upload, FileText, CheckCircle, AlertCircle, X, Loader2, Sparkles } from "lucide-react";

interface ResumeUploaderProps {
  onSkillsExtracted: (skills: string[], roleId?: string) => void;
  selectedSkills: string[];
  onResumeRemoved?: () => void;
}

export function ResumeUploader({ onSkillsExtracted, selectedSkills, onResumeRemoved }: ResumeUploaderProps) {
  const [uploadedFile, setUploadedFile] = useState<File | null>(null);
  const [extractedSkills, setExtractedSkills] = useState<string[]>([]);
  const [categorizedSkills, setCategorizedSkills] = useState<Record<string, string[]>>({});
  const [suggestedRoles, setSuggestedRoles] = useState<Array<{role: string, match_percentage: number, confidence: string}>>([]);
  const [topMatch, setTopMatch] = useState<{role: string, match_percentage: number, message: string} | null>(null);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [skillsFromResume, setSkillsFromResume] = useState<string[]>([]);
  const fileInputRef = useRef<HTMLInputElement>(null);

  // Convert role name to role ID for roadmap mapping
  const getRoleIdFromName = (roleName: string): string | undefined => {
    const roleMapping: { [key: string]: string } = {
      'Frontend Developer': 'frontend-developer',
      'Backend Developer': 'backend-developer',
      'Full Stack Developer': 'fullstack-developer',
      'Data Scientist': 'data-scientist',
      'DevOps Engineer': 'devops-engineer',
      'Mobile Developer': 'mobile-developer',
      'UI/UX Designer': 'ui-ux-designer',
      'Cloud Engineer': 'cloud-engineer',
      'Machine Learning Engineer': 'ml-engineer',
      'Data Engineer': 'data-engineer'
    };
    return roleMapping[roleName];
  };

  const handleFileSelect = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      const validTypes = [
        'application/pdf',
        'application/msword',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'application/vnd.openxmlformats-officedocument.presentationml.presentation',
        'text/plain'
      ];
      
      const validExtensions = ['.pdf', '.doc', '.docx', '.pptx', '.txt'];
      const fileExtension = file.name.toLowerCase().substring(file.name.lastIndexOf('.'));
      
      if (validTypes.includes(file.type) || validExtensions.includes(fileExtension)) {
        setUploadedFile(file);
        analyzeResume(file);
      } else {
        alert('Please upload a PDF, Word (DOC/DOCX), PowerPoint (PPTX), or Text file');
      }
    }
  };

  const analyzeResume = async (file: File) => {
    setIsAnalyzing(true);
    
    try {
      const formData = new FormData();
      formData.append('resume', file);
      
      // TEMPORARY FIX: Hardcode local backend for testing
      const API_URL = 'https://backend-careerpath-ai.vercel.app/api';
      
      // Debug: Log which API is being used
      console.log('🔍 API URL:', API_URL);
      console.log('🔍 Calling LOCAL backend');
      
      const response = await fetch(`${API_URL}/extract-skills`, {
        method: 'POST',
        body: formData,
      });
      
      if (!response.ok) {
        throw new Error('Failed to analyze resume');
      }
      
      const data = await response.json();
      setExtractedSkills(data.skills || []);
      setCategorizedSkills(data.categorized_skills || {});
      setSuggestedRoles(data.suggested_roles || []);
      setTopMatch(data.top_match || null);
      setIsAnalyzing(false);
    } catch (error) {
      console.error('Error analyzing resume:', error);
      setIsAnalyzing(false);
      alert('Failed to analyze resume. Please try again.');
    }
  };

  const handleAddExtractedSkills = () => {
    const newSkills = [...new Set([...selectedSkills, ...extractedSkills])];
    const roleId = topMatch ? getRoleIdFromName(topMatch.role) : undefined;
    setSkillsFromResume(extractedSkills);
    onSkillsExtracted(newSkills, roleId);
    // Keep the resume and extracted skills visible
  };

  const handleRemoveFile = () => {
    // Remove only skills that came from the resume
    const remainingSkills = selectedSkills.filter(skill => !skillsFromResume.includes(skill));
    onSkillsExtracted(remainingSkills, undefined);
    
    setUploadedFile(null);
    setExtractedSkills([]);
    setCategorizedSkills({});
    setSuggestedRoles([]);
    setTopMatch(null);
    setSkillsFromResume([]);
    
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
    
    // Notify parent that resume was removed (to reset detected role)
    if (onResumeRemoved) {
      onResumeRemoved();
    }
  };

  const getFileIcon = (fileName: string) => {
    const ext = fileName.toLowerCase();
    if (ext.endsWith('.pdf')) return <FileText className="w-4 h-4 text-red-500" />;
    if (ext.endsWith('.doc') || ext.endsWith('.docx')) return <FileText className="w-4 h-4 text-blue-500" />;
    if (ext.endsWith('.pptx')) return <FileText className="w-4 h-4 text-orange-500" />;
    return <FileText className="w-4 h-4 text-gray-500" />;
  };

  return (
    <Card>
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          <Upload className="w-5 h-5 text-indigo-600" />
          AI Resume Scanner
        </CardTitle>
        <CardDescription>
          Upload your resume and let CareerPath AI automatically extract your current skills
        </CardDescription>
      </CardHeader>
      <CardContent>
        {!uploadedFile ? (
          <div className="space-y-4">
            <div
              onClick={() => fileInputRef.current?.click()}
              className="border-2 border-dashed border-gray-300 rounded-lg p-8 text-center cursor-pointer hover:border-indigo-400 hover:bg-indigo-50 transition-colors"
            >
              <Upload className="w-12 h-12 text-gray-400 mx-auto mb-4" />
              <p className="text-lg font-medium text-gray-700 mb-2">
                Drop your resume here or click to browse
              </p>
              <p className="text-sm text-gray-500">
                Supports PDF, Word (DOC/DOCX), PowerPoint (PPTX), and Text files (Max 5MB)
              </p>
              <input
                ref={fileInputRef}
                type="file"
                accept=".pdf,.doc,.docx,.pptx,.txt"
                onChange={handleFileSelect}
                className="hidden"
              />
            </div>
            
            <div className="bg-indigo-50 border border-indigo-200 rounded-lg p-4">
              <div className="flex items-start gap-2">
                <Sparkles className="w-5 h-5 text-indigo-600 mt-0.5" />
                <div className="text-sm text-indigo-800">
                  <p className="font-medium mb-1">CareerPath AI Technology</p>
                  <p>Our advanced AI analyzes your resume to identify technical skills, soft skills, and experience levels, providing you with the most accurate skill assessment.</p>
                </div>
              </div>
            </div>
          </div>
        ) : (
          <div className="space-y-4">
            {/* File Info */}
            <div className="flex items-center justify-between p-4 bg-gray-50 rounded-lg border">
              <div className="flex items-center gap-3">
                {getFileIcon(uploadedFile.name)}
                <div>
                  <p className="font-medium text-gray-900">{uploadedFile.name}</p>
                  <p className="text-sm text-gray-500">
                    {(uploadedFile.size / 1024 / 1024).toFixed(2)} MB
                  </p>
                </div>
              </div>
              <Button
                variant="ghost"
                size="sm"
                onClick={handleRemoveFile}
                className="text-gray-500 hover:text-red-600"
              >
                <X className="w-4 h-4" />
              </Button>
            </div>

            {/* Analysis Status */}
            {isAnalyzing && (
              <div className="flex items-center gap-3 p-4 bg-indigo-50 rounded-lg border border-indigo-200">
                <Loader2 className="w-5 h-5 text-indigo-600 animate-spin" />
                <div>
                  <p className="font-medium text-indigo-900">CareerPath AI is analyzing...</p>
                  <p className="text-sm text-indigo-700">Extracting skills and experience from your resume</p>
                </div>
              </div>
            )}

            {/* Extracted Skills */}
            {!isAnalyzing && extractedSkills.length > 0 && (
              <div className="space-y-4">
                {/* Role Suggestions */}
                {topMatch && (
                  <div className="bg-gradient-to-r from-green-50 to-emerald-50 border-2 border-green-300 rounded-lg p-4">
                    <div className="flex items-start gap-3">
                      <Sparkles className="w-6 h-6 text-green-600 mt-0.5" />
                      <div className="flex-1">
                        <p className="font-semibold text-green-900 text-lg mb-2">
                          🎯 You're eligible for {topMatch.role}!
                        </p>
                        <div className="flex items-center gap-2 mb-2">
                          <div className="flex-1 bg-white rounded-full h-3 overflow-hidden">
                            <div 
                              className="bg-gradient-to-r from-green-500 to-emerald-500 h-full transition-all duration-500"
                              style={{ width: `${topMatch.match_percentage}%` }}
                            />
                          </div>
                          <span className="font-bold text-green-700">{topMatch.match_percentage}%</span>
                        </div>
                        <p className="text-sm text-green-700">
                          {topMatch.message}
                        </p>
                      </div>
                    </div>
                    
                    {suggestedRoles.length > 1 && (
                      <div className="mt-3 pt-3 border-t border-green-200">
                        <p className="text-sm font-medium text-green-800 mb-2">Other suitable roles:</p>
                        <div className="flex flex-wrap gap-2">
                          {suggestedRoles.slice(1).map((role, index) => (
                            <Badge key={index} className="bg-green-100 text-green-800 border-green-300">
                              {role.role} ({role.match_percentage}%)
                            </Badge>
                          ))}
                        </div>
                      </div>
                    )}
                  </div>
                )}
                
                {/* Categorized Skills */}
                <div className="space-y-3">
                  <div className="flex items-center gap-2">
                    <CheckCircle className="w-5 h-5 text-green-600" />
                    <p className="font-medium text-gray-900">
                      CareerPath AI found {extractedSkills.length} skills in your resume
                    </p>
                  </div>
                  
                  {Object.keys(categorizedSkills).length > 0 ? (
                    <div className="space-y-3">
                      {Object.entries(categorizedSkills).map(([category, skills]) => (
                        <div key={category} className="bg-gray-50 rounded-lg p-3 border">
                          <p className="text-sm font-semibold text-gray-700 mb-2">{category}:</p>
                          <div className="flex flex-wrap gap-2">
                            {skills.map((skill) => (
                              <Badge
                                key={skill}
                                variant="secondary"
                                className="bg-green-100 text-green-800 border-green-200"
                              >
                                {skill}
                              </Badge>
                            ))}
                          </div>
                        </div>
                      ))}
                    </div>
                  ) : (
                    <div className="flex flex-wrap gap-2">
                      {extractedSkills.map((skill) => (
                        <Badge
                          key={skill}
                          variant="secondary"
                          className="bg-green-100 text-green-800 border-green-200"
                        >
                          {skill}
                        </Badge>
                      ))}
                    </div>
                  )}
                </div>

                <div className="flex gap-2">
                  <Button
                    onClick={handleAddExtractedSkills}
                    className="bg-green-600 hover:bg-green-700"
                  >
                    <CheckCircle className="w-4 h-4 mr-2" />
                    {extractedSkills.filter(s => !selectedSkills.includes(s)).length > 0 
                      ? `Add ${extractedSkills.filter(s => !selectedSkills.includes(s)).length} New Skills`
                      : 'Use These Skills'
                    }
                  </Button>
                  <Button
                    variant="outline"
                    onClick={handleRemoveFile}
                  >
                    Upload Different File
                  </Button>
                </div>
              </div>
            )}

            {/* No Skills Found */}
            {!isAnalyzing && extractedSkills.length === 0 && (
              <div className="flex items-center gap-3 p-4 bg-yellow-50 rounded-lg border border-yellow-200">
                <AlertCircle className="w-5 h-5 text-yellow-600" />
                <div className="flex-1">
                  <p className="font-medium text-yellow-900">No skills detected</p>
                  <p className="text-sm text-yellow-700">
                    CareerPath AI couldn't extract skills from this file. Try uploading a different format or add skills manually.
                  </p>
                </div>
                <Button
                  variant="outline"
                  size="sm"
                  onClick={handleRemoveFile}
                >
                  Try Again
                </Button>
              </div>
            )}
          </div>
        )}
      </CardContent>
    </Card>
  );
}