import { Check, X, Target, TrendingUp } from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle } from "../components/ui/card";
import { Progress } from "../components/ui/progress";

interface SkillGapAnalysisProps {
  matchedSkills: string[];
  missingSkills: string[];
  totalRequired: number;
}

export function SkillGapAnalysis({ matchedSkills, missingSkills, totalRequired }: SkillGapAnalysisProps) {
  const completionPercentage = (matchedSkills.length / totalRequired) * 100;

  return (
    <div className="space-y-6">
      {/* Progress Overview */}
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <Target className="w-5 h-5 text-blue-600" />
            Skill Gap Overview
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              <span className="text-sm font-medium text-gray-700">Readiness Score</span>
              <span className="text-2xl font-bold text-blue-600">
                {Math.round(completionPercentage)}%
              </span>
            </div>
            <Progress value={completionPercentage} className="h-3" />
            <div className="grid grid-cols-3 gap-4 text-center">
              <div>
                <div className="text-2xl font-bold text-green-600">{matchedSkills.length}</div>
                <div className="text-sm text-gray-600">Skills You Have</div>
              </div>
              <div>
                <div className="text-2xl font-bold text-red-600">{missingSkills.length}</div>
                <div className="text-sm text-gray-600">Skills Needed</div>
              </div>
              <div>
                <div className="text-2xl font-bold text-blue-600">{totalRequired}</div>
                <div className="text-sm text-gray-600">Total Required</div>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Skills Comparison */}
      <div className="grid md:grid-cols-2 gap-6">
        {/* Matched Skills */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2 text-green-700">
              <Check className="w-5 h-5" />
              Your Current Skills
            </CardTitle>
          </CardHeader>
          <CardContent>
            {matchedSkills.length > 0 ? (
              <div className="space-y-2">
                {matchedSkills.map((skill) => (
                  <div
                    key={skill}
                    className="flex items-center gap-3 p-3 bg-green-50 rounded-lg border border-green-200"
                  >
                    <Check className="w-5 h-5 text-green-600 flex-shrink-0" />
                    <span className="font-medium text-green-800">{skill}</span>
                  </div>
                ))}
              </div>
            ) : (
              <p className="text-gray-500 text-center py-4">No matching skills yet</p>
            )}
          </CardContent>
        </Card>

        {/* Missing Skills */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2 text-red-700">
              <X className="w-5 h-5" />
              Skills to Develop
            </CardTitle>
          </CardHeader>
          <CardContent>
            {missingSkills.length > 0 ? (
              <div className="space-y-2">
                {missingSkills.map((skill) => (
                  <div
                    key={skill}
                    className="flex items-center gap-3 p-3 bg-red-50 rounded-lg border border-red-200"
                  >
                    <X className="w-5 h-5 text-red-600 flex-shrink-0" />
                    <span className="font-medium text-red-800">{skill}</span>
                  </div>
                ))}
              </div>
            ) : (
              <div className="text-center py-4">
                <TrendingUp className="w-12 h-12 text-green-600 mx-auto mb-2" />
                <p className="text-green-700 font-medium">Congratulations!</p>
                <p className="text-gray-600 text-sm">You have all the required skills</p>
              </div>
            )}
          </CardContent>
        </Card>
      </div>
    </div>
  );
}