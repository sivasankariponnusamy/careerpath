import { useState } from "react";
import { jobRoles } from "../data/jobRoles";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Briefcase, DollarSign, TrendingUp, Users, ExternalLink, MapPin, Clock, Star } from "lucide-react";

interface JobSelectorProps {
  selectedJob: string | null;
  onJobSelect: (jobId: string | null) => void;
}

export function JobSelector({ selectedJob, onJobSelect }: JobSelectorProps) {
  const [hoveredJob, setHoveredJob] = useState<string | null>(null);

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

  const getPlatformIcon = (platform: string) => {
    switch (platform.toLowerCase()) {
      case "linkedin":
        return "💼";
      case "indeed":
        return "🔍";
      case "glassdoor":
        return "🏢";
      case "angellist":
        return "🚀";
      case "hired":
        return "💎";
      case "kaggle":
        return "📊";
      case "stackoverflow jobs":
        return "💻";
      case "remoteok":
        return "🌍";
      case "devopsjobs":
        return "⚙️";
      case "built in":
        return "🏗️";
      case "cloud careers":
        return "☁️";
      default:
        return "🔗";
    }
  };

  return (
    <Card>
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          <Briefcase className="w-5 h-5 text-blue-600" />
          Choose Your Target Role
        </CardTitle>
        <CardDescription>
          Select the career path you want to pursue. We'll analyze your skills against the requirements.
        </CardDescription>
      </CardHeader>
      <CardContent>
        <div className="grid md:grid-cols-2 gap-4">
          {jobRoles.map((role) => (
            <div
              key={role.id}
              className={`relative border rounded-lg p-4 cursor-pointer transition-all ${
                selectedJob === role.id
                  ? "border-blue-500 bg-blue-50 ring-2 ring-blue-200"
                  : "border-gray-200 hover:border-gray-300 hover:shadow-md"
              }`}
              onClick={() => onJobSelect(selectedJob === role.id ? null : role.id)}
              onMouseEnter={() => setHoveredJob(role.id)}
              onMouseLeave={() => setHoveredJob(null)}
            >
              <div className="flex items-start justify-between mb-3">
                <div>
                  <h3 className="font-semibold text-gray-900">{role.title}</h3>
                  <p className="text-sm text-gray-600 mt-1">{role.description}</p>
                </div>
                {selectedJob === role.id && (
                  <div className="bg-blue-500 text-white rounded-full p-1">
                    <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                    </svg>
                  </div>
                )}
              </div>

              <div className="flex items-center gap-2 flex-wrap mb-3">
                <Badge variant="outline" className="text-xs">
                  {role.requiredSkills.length} skills required
                </Badge>
                {role.difficulty && (
                  <Badge className={`text-xs ${getDifficultyColor(role.difficulty)}`}>
                    {role.difficulty}
                  </Badge>
                )}
              </div>

              {/* Job Stats */}
              <div className="grid grid-cols-2 gap-2 mb-3">
                {role.averageSalary && (
                  <div className="flex items-center gap-1 text-xs text-gray-600">
                    <DollarSign className="w-3 h-3" />
                    <span>{role.averageSalary}</span>
                  </div>
                )}
                {role.growthRate && (
                  <div className="flex items-center gap-1 text-xs text-gray-600">
                    <TrendingUp className="w-3 h-3" />
                    <span>{role.growthRate} growth</span>
                  </div>
                )}
              </div>

              {/* Required Skills Preview */}
              <div className="mb-3">
                <div className="text-xs font-medium text-gray-700 mb-1">Key Skills:</div>
                <div className="flex flex-wrap gap-1">
                  {role.requiredSkills.slice(0, 3).map((skill) => (
                    <Badge key={skill} variant="secondary" className="text-xs">
                      {skill}
                    </Badge>
                  ))}
                  {role.requiredSkills.length > 3 && (
                    <Badge variant="secondary" className="text-xs">
                      +{role.requiredSkills.length - 3} more
                    </Badge>
                  )}
                </div>
              </div>

              {/* Job Search Links - Show on hover or when selected */}
              {(hoveredJob === role.id || selectedJob === role.id) && role.jobSearchLinks && (
                <div className="mt-3 pt-3 border-t border-gray-200">
                  <div className="text-xs font-medium text-gray-700 mb-2 flex items-center gap-1">
                    <MapPin className="w-3 h-3" />
                    Find Jobs:
                  </div>
                  <div className="grid grid-cols-2 gap-1">
                    {role.jobSearchLinks.slice(0, 4).map((link, index) => (
                      <Button
                        key={index}
                        variant="outline"
                        size="sm"
                        className="text-xs h-6 px-2 justify-start gap-1"
                        onClick={(e) => {
                          e.stopPropagation();
                          window.open(link.url, '_blank', 'noopener,noreferrer');
                        }}
                      >
                        <span>{getPlatformIcon(link.platform)}</span>
                        <span className="truncate">{link.platform}</span>
                        <ExternalLink className="w-2 h-2 flex-shrink-0" />
                      </Button>
                    ))}
                  </div>
                </div>
              )}

              {/* Career Resources - Show when selected */}
              {selectedJob === role.id && role.careerResources && (
                <div className="mt-3 pt-3 border-t border-gray-200">
                  <div className="text-xs font-medium text-gray-700 mb-2 flex items-center gap-1">
                    <Star className="w-3 h-3" />
                    Career Resources:
                  </div>
                  <div className="space-y-1">
                    {role.careerResources.slice(0, 2).map((resource, index) => (
                      <Button
                        key={index}
                        variant="ghost"
                        size="sm"
                        className="text-xs h-6 px-2 justify-start gap-1 w-full"
                        onClick={(e) => {
                          e.stopPropagation();
                          window.open(resource.url, '_blank', 'noopener,noreferrer');
                        }}
                      >
                        <span>📚</span>
                        <span className="truncate">{resource.title}</span>
                        <ExternalLink className="w-2 h-2 flex-shrink-0" />
                      </Button>
                    ))}
                  </div>
                </div>
              )}
            </div>
          ))}
        </div>

        {/* Job Search Tips */}
        <div className="mt-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
          <h4 className="font-medium text-blue-900 mb-2 flex items-center gap-2">
            <Users className="w-4 h-4" />
            Job Search Tips
          </h4>
          <div className="grid md:grid-cols-2 gap-4 text-sm text-blue-800">
            <div>
              <h5 className="font-medium mb-1">📝 Application Strategy</h5>
              <ul className="space-y-1 text-xs">
                <li>• Tailor your resume for each role</li>
                <li>• Highlight relevant projects and skills</li>
                <li>• Use keywords from job descriptions</li>
                <li>• Prepare a portfolio of your work</li>
              </ul>
            </div>
            <div>
              <h5 className="font-medium mb-1">🎯 Platform Recommendations</h5>
              <ul className="space-y-1 text-xs">
                <li>• LinkedIn: Professional networking</li>
                <li>• Indeed: Large job database</li>
                <li>• AngelList: Startup opportunities</li>
                <li>• Specialized boards: Niche roles</li>
              </ul>
            </div>
          </div>
        </div>
      </CardContent>
    </Card>
  );
}