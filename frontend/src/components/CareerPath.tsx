import { useState } from "react";
import { jobRoles } from "../data/jobRoles";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Progress } from "@/components/ui/progress";
import { 
  Target, 
  Clock, 
  TrendingUp, 
  ExternalLink, 
  Briefcase, 
  DollarSign, 
  MapPin, 
  Star,
  BookOpen,
  CheckCircle,
  XCircle,
  Download,
  Share2
} from "lucide-react";

interface CareerPathProps {
  role: string;
  currentSkills: string[];
  missingSkills: string[];
  matchPercentage: number;
  estimatedTime: string;
}

export function CareerPath({ 
  role, 
  currentSkills, 
  missingSkills, 
  matchPercentage, 
  estimatedTime 
}: CareerPathProps) {
  const [showJobLinks, setShowJobLinks] = useState(false);
  
  const jobRole = jobRoles.find(jr => jr.id === role);
  
  const getDifficultyColor = (difficulty?: string) => {
    switch (difficulty) {
      case "Beginner":
        return "bg-green-100 text-green-800";
      case "Intermediate":
        return "bg-yellow-100 text-yellow-800";
      case "Advanced":
        return "bg-red-100 text-red-800";
      default:
        return "bg-gray-100 text-gray-800";
    }
  };

  const getMatchColor = (percentage: number) => {
    if (percentage >= 80) return "text-green-600";
    if (percentage >= 50) return "text-yellow-600";
    return "text-red-600";
  };

  const getMatchBgColor = (percentage: number) => {
    if (percentage >= 80) return "bg-green-100";
    if (percentage >= 50) return "bg-yellow-100";
    return "bg-red-100";
  };

  const handleJobSearch = (url: string) => {
    window.open(url, '_blank', 'noopener,noreferrer');
  };

  const handleDownloadPlan = () => {
    const planContent = generateCareerPlan();
    const blob = new Blob([planContent], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${role.replace('-', '-')}-career-plan.txt`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  const generateCareerPlan = () => {
    const date = new Date().toLocaleDateString();
    let content = `CAREER DEVELOPMENT PLAN\n`;
    content += `========================\n\n`;
    content += `Target Role: ${jobRole?.title}\n`;
    content += `Generated: ${date}\n\n`;
    
    content += `CURRENT STATUS\n`;
    content += `------------\n`;
    content += `Skills Match: ${matchPercentage}%\n`;
    content += `Current Skills: ${currentSkills.length}\n`;
    content += `Missing Skills: ${missingSkills.length}\n`;
    content += `Estimated Learning Time: ${estimatedTime}\n\n`;
    
    if (jobRole?.averageSalary) {
      content += `SALARY EXPECTATIONS\n`;
      content += `------------------\n`;
      content += `Average Salary: ${jobRole.averageSalary}\n`;
      if (jobRole.growthRate) {
        content += `Growth Rate: ${jobRole.growthRate}\n`;
      }
      content += `\n`;
    }
    
    content += `YOUR CURRENT SKILLS\n`;
    content += `------------------\n`;
    currentSkills.forEach(skill => {
      content += `✓ ${skill}\n`;
    });
    content += `\n`;
    
    content += `SKILLS TO DEVELOP\n`;
    content += `-----------------\n`;
    missingSkills.forEach(skill => {
      content += `○ ${skill}\n`;
    });
    content += `\n`;
    
    if (jobRole?.jobSearchLinks) {
      content += `JOB SEARCH PLATFORMS\n`;
      content += `-------------------\n`;
      jobRole.jobSearchLinks.forEach(link => {
        content += `${link.platform}: ${link.url}\n`;
      });
      content += `\n`;
    }
    
    content += `NEXT STEPS\n`;
    content += `----------\n`;
    content += `1. Focus on learning the missing skills\n`;
    content += `2. Build projects to demonstrate your abilities\n`;
    content += `3. Update your resume and portfolio\n`;
    content += `4. Start applying for jobs on recommended platforms\n`;
    content += `5. Network with professionals in the field\n`;
    
    return content;
  };

  const handleSharePlan = async () => {
    const shareData = {
      title: `My Career Path to ${jobRole?.title}`,
      text: `I'm ${matchPercentage}% ready to become a ${jobRole?.title}! I have ${currentSkills.length} skills and need to learn ${missingSkills.length} more. Estimated time: ${estimatedTime}`,
      url: window.location.href
    };

    try {
      if (navigator.share) {
        await navigator.share(shareData);
      } else {
        // Fallback: copy to clipboard
        const text = `${shareData.title}\n\n${shareData.text}\n\n${shareData.url}`;
        await navigator.clipboard.writeText(text);
        alert('Career plan copied to clipboard!');
      }
    } catch (err) {
      console.log('Error sharing:', err);
    }
  };

  return (
    <Card>
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          <Target className="w-5 h-5 text-purple-600" />
          Your Career Path to {jobRole?.title}
        </CardTitle>
        <CardDescription>
          Your personalized roadmap to becoming a {jobRole?.title}. Track your progress and take action.
        </CardDescription>
      </CardHeader>
      <CardContent>
        <div className="space-y-6">
          {/* Progress Overview */}
          <div className={`p-6 rounded-lg ${getMatchBgColor(matchPercentage)} border-2 border-opacity-20`}>
            <div className="flex items-center justify-between mb-4">
              <div>
                <div className={`text-3xl font-bold ${getMatchColor(matchPercentage)}`}>
                  {matchPercentage}%
                </div>
                <div className="text-lg font-medium text-gray-700">
                  Skills Match
                </div>
              </div>
              <div className="text-right">
                <div className="text-sm text-gray-600">Estimated Time</div>
                <div className="text-lg font-medium text-gray-900 flex items-center gap-1">
                  <Clock className="w-4 h-4" />
                  {estimatedTime}
                </div>
              </div>
            </div>
            
            <Progress 
              value={matchPercentage} 
              className="h-3 mb-2"
            />
            
            <div className="flex justify-between text-sm text-gray-600">
              <span>{currentSkills.length} skills mastered</span>
              <span>{missingSkills.length} skills to learn</span>
            </div>
          </div>

          {/* Job Details */}
          {jobRole && (
            <div className="grid md:grid-cols-3 gap-4">
              <div className="flex items-center gap-2 p-3 bg-gray-50 rounded-lg">
                <DollarSign className="w-5 h-5 text-green-600" />
                <div>
                  <div className="text-sm font-medium text-gray-900">Salary Range</div>
                  <div className="text-sm text-gray-600">{jobRole.averageSalary}</div>
                </div>
              </div>
              
              <div className="flex items-center gap-2 p-3 bg-gray-50 rounded-lg">
                <TrendingUp className="w-5 h-5 text-blue-600" />
                <div>
                  <div className="text-sm font-medium text-gray-900">Growth Rate</div>
                  <div className="text-sm text-gray-600">{jobRole.growthRate}</div>
                </div>
              </div>
              
              <div className="flex items-center gap-2 p-3 bg-gray-50 rounded-lg">
                <Briefcase className="w-5 h-5 text-purple-600" />
                <div>
                  <div className="text-sm font-medium text-gray-900">Difficulty</div>
                  <Badge className={`text-xs ${getDifficultyColor(jobRole.difficulty)}`}>
                    {jobRole.difficulty}
                  </Badge>
                </div>
              </div>
            </div>
          )}

          {/* Skills Breakdown */}
          <div className="grid md:grid-cols-2 gap-6">
            <div>
              <h3 className="font-semibold text-gray-900 mb-3 flex items-center gap-2">
                <CheckCircle className="w-4 h-4 text-green-600" />
                Your Current Skills ({currentSkills.length})
              </h3>
              <div className="space-y-2">
                {currentSkills.map((skill) => (
                  <div key={skill} className="flex items-center gap-2 p-2 bg-green-50 rounded-lg border border-green-200">
                    <CheckCircle className="w-4 h-4 text-green-600" />
                    <span className="text-sm font-medium text-green-800">{skill}</span>
                  </div>
                ))}
              </div>
            </div>
            
            <div>
              <h3 className="font-semibold text-gray-900 mb-3 flex items-center gap-2">
                <XCircle className="w-4 h-4 text-red-600" />
                Skills to Develop ({missingSkills.length})
              </h3>
              <div className="space-y-2">
                {missingSkills.map((skill) => (
                  <div key={skill} className="flex items-center gap-2 p-2 bg-red-50 rounded-lg border border-red-200">
                    <XCircle className="w-4 h-4 text-red-600" />
                    <span className="text-sm font-medium text-red-800">{skill}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Job Search Section */}
          <div className="border-t pt-6">
            <div className="flex items-center justify-between mb-4">
              <h3 className="font-semibold text-gray-900 flex items-center gap-2">
                <MapPin className="w-4 h-4 text-blue-600" />
                Job Search Platforms
              </h3>
              <Button
                variant="outline"
                size="sm"
                onClick={() => setShowJobLinks(!showJobLinks)}
              >
                {showJobLinks ? 'Hide' : 'Show'} Platforms
              </Button>
            </div>
            
            {showJobLinks && jobRole?.jobSearchLinks && (
              <div className="grid md:grid-cols-2 gap-3">
                {jobRole.jobSearchLinks.map((link, index) => (
                  <div
                    key={index}
                    className="flex items-center justify-between p-3 border border-gray-200 rounded-lg hover:bg-gray-50"
                  >
                    <div className="flex-1">
                      <div className="font-medium text-gray-900">{link.platform}</div>
                      <div className="text-xs text-gray-600">{link.description}</div>
                    </div>
                    <Button
                      variant="outline"
                      size="sm"
                      onClick={() => handleJobSearch(link.url)}
                      className="ml-2"
                    >
                      <ExternalLink className="w-4 h-4" />
                    </Button>
                  </div>
                ))}
              </div>
            )}
          </div>

          {/* Career Resources */}
          {jobRole?.careerResources && (
            <div className="border-t pt-6">
              <h3 className="font-semibold text-gray-900 mb-4 flex items-center gap-2">
                <BookOpen className="w-4 h-4 text-purple-600" />
                Career Development Resources
              </h3>
              <div className="grid md:grid-cols-2 gap-3">
                {jobRole.careerResources.map((resource, index) => (
                  <div
                    key={index}
                    className="flex items-center justify-between p-3 border border-gray-200 rounded-lg hover:bg-gray-50"
                  >
                    <div className="flex-1">
                      <div className="font-medium text-gray-900">{resource.title}</div>
                      <div className="text-xs text-gray-600">{resource.description}</div>
                    </div>
                    <Button
                      variant="outline"
                      size="sm"
                      onClick={() => window.open(resource.url, '_blank', 'noopener,noreferrer')}
                      className="ml-2"
                    >
                      <ExternalLink className="w-4 h-4" />
                    </Button>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Action Buttons */}
          <div className="flex flex-wrap gap-3 pt-6 border-t">
            <Button onClick={handleDownloadPlan} className="flex items-center gap-2">
              <Download className="w-4 h-4" />
              Download Career Plan
            </Button>
            <Button variant="outline" onClick={handleSharePlan} className="flex items-center gap-2">
              <Share2 className="w-4 h-4" />
              Share Progress
            </Button>
            <Button 
              variant="outline" 
              onClick={() => setShowJobLinks(!showJobLinks)}
              className="flex items-center gap-2"
            >
              <Briefcase className="w-4 h-4" />
              Browse Jobs
            </Button>
          </div>

          {/* Motivational Message */}
          <div className="p-4 bg-gradient-to-r from-blue-50 to-purple-50 rounded-lg border border-blue-200">
            <div className="flex items-start gap-3">
              <Star className="w-5 h-5 text-yellow-600 mt-0.5" />
              <div>
                <h4 className="font-medium text-gray-900 mb-1">You're on the right track! 🚀</h4>
                <p className="text-sm text-gray-700">
                  {matchPercentage >= 80 
                    ? "Excellent! You're almost ready for this role. Focus on polishing your portfolio and start applying."
                    : matchPercentage >= 50
                    ? "Great progress! You're halfway there. Keep learning the missing skills and you'll be job-ready soon."
                    : "Every expert was once a beginner. Start with the fundamentals and build your skills step by step."
                  }
                </p>
              </div>
            </div>
          </div>
        </div>
      </CardContent>
    </Card>
  );
}