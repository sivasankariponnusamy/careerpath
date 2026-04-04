import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { BookOpen, ExternalLink, Download, Clock, Star, Target, Lightbulb } from "lucide-react";
import { skillResources } from "../data/skillResources";

interface LearningPathProps {
  missingSkills: string[];
}

export function LearningPath({ missingSkills }: LearningPathProps) {
  const downloadPlan = () => {
    const planContent = `
CAREERPATH AI - PERSONALIZED LEARNING PLAN
==========================================

Missing Skills to Master:
${missingSkills.map(skill => `• ${skill}`).join('\n')}

Recommended Learning Resources:
${missingSkills.map(skill => {
  const resources = (skillResources as Record<string, any[]>)[skill] || [];
  return resources.map((resource: any, index: number) => `
${skill} - Resource ${index + 1}:
  Title: ${resource.title}
  Description: ${resource.description}
  Duration: ${resource.duration}
  Level: ${resource.level}
  Rating: ${resource.rating}/5
`).join('');
}).join('')}

Generated on: ${new Date().toLocaleDateString()}
Powered by CareerPath AI
    `.trim();

    const blob = new Blob([planContent], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'CareerPath_AI_Learning_Plan.txt';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  return (
    <Card>
      <CardHeader>
        <div className="flex items-center justify-between">
          <div>
            <CardTitle className="flex items-center gap-2">
              <Target className="w-5 h-5 text-indigo-600" />
              Your Personalized Learning Path
            </CardTitle>
            <CardDescription>
              CareerPath AI has curated the best resources to help you master your missing skills
            </CardDescription>
          </div>
          <Button
            onClick={downloadPlan}
            variant="outline"
            className="flex items-center gap-2"
          >
            <Download className="w-4 h-4" />
            Download Plan
          </Button>
        </div>
      </CardHeader>
      <CardContent>
        <div className="space-y-6">
          {missingSkills.map((skill, skillIndex) => {
            const resources = (skillResources as Record<string, any[]>)[skill] || [];
            
            return (
              <div key={skill} className="border-l-4 border-indigo-500 pl-4">
                <div className="flex items-center gap-2 mb-3">
                  <h3 className="text-lg font-semibold text-gray-900">{skill}</h3>
                  <Badge variant="secondary" className="bg-indigo-100 text-indigo-800">
                    Priority {skillIndex + 1}
                  </Badge>
                </div>
                
                <div className="grid md:grid-cols-2 gap-4">
                  {resources.map((resource: any, index: number) => (
                    <Card key={index} className="border-gray-200 hover:shadow-md transition-shadow">
                      <CardHeader className="pb-3">
                        <div className="flex items-start justify-between">
                          <div className="flex items-center gap-2">
                            <BookOpen className="w-4 h-4 text-indigo-600" />
                            <CardTitle className="text-base">{resource.title}</CardTitle>
                          </div>
                          <Badge variant="outline" className={`
                            ${resource.level === 'Beginner' ? 'bg-green-50 text-green-700 border-green-200' : ''}
                            ${resource.level === 'Intermediate' ? 'bg-yellow-50 text-yellow-700 border-yellow-200' : ''}
                            ${resource.level === 'Advanced' ? 'bg-red-50 text-red-700 border-red-200' : ''}
                          `}>
                            {resource.level}
                          </Badge>
                        </div>
                        <CardDescription className="text-sm">
                          {resource.description}
                        </CardDescription>
                      </CardHeader>
                      <CardContent className="pt-0">
                        <div className="flex items-center justify-between mb-3">
                          <div className="flex items-center gap-4 text-sm text-gray-600">
                            <div className="flex items-center gap-1">
                              <Clock className="w-3 h-3" />
                              {resource.duration}
                            </div>
                            <div className="flex items-center gap-1">
                              <Star className="w-3 h-3 text-yellow-500" />
                              {resource.rating}/5
                            </div>
                          </div>
                        </div>
                        <Button
                          onClick={() => window.open(resource.url, '_blank')}
                          size="sm"
                          className="w-full bg-indigo-600 hover:bg-indigo-700"
                        >
                          <ExternalLink className="w-3 h-3 mr-2" />
                          Start Learning
                        </Button>
                      </CardContent>
                    </Card>
                  ))}
                </div>
              </div>
            );
          })}
          
          {/* Motivational Section */}
          <div className="bg-gradient-to-r from-indigo-50 to-purple-50 rounded-lg p-6 border border-indigo-200">
            <div className="flex items-center gap-3 mb-3">
              <Lightbulb className="w-6 h-6 text-indigo-600" />
              <h3 className="text-lg font-semibold text-indigo-900">CareerPath AI Tip</h3>
            </div>
            <p className="text-indigo-800">
              Focus on one skill at a time and practice consistently. Most learners see significant improvement in 4-6 weeks when dedicating 10-15 hours per week. Remember, every expert was once a beginner!
            </p>
          </div>
        </div>
      </CardContent>
    </Card>
  );
}