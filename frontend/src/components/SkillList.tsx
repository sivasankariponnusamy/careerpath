import { CheckCircle, XCircle } from "lucide-react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Progress } from "@/components/ui/progress";

interface SkillListProps {
  title: string;
  skills: string[];
  type: "current" | "missing";
}

export function SkillList({ title, skills, type }: SkillListProps) {
  const getIcon = () => {
    return type === "current" ? (
      <CheckCircle className="w-5 h-5 text-green-600" />
    ) : (
      <XCircle className="w-5 h-5 text-red-600" />
    );
  };

  const getBgColor = () => {
    return type === "current" ? "bg-green-50 border-green-200" : "bg-red-50 border-red-200";
  };

  const getTextColor = () => {
    return type === "current" ? "text-green-800" : "text-red-800";
  };

  return (
    <Card className={`${getBgColor()} border-2`}>
      <CardHeader className="pb-3">
        <CardTitle className="flex items-center gap-2 text-lg">
          {getIcon()}
          {title}
        </CardTitle>
        <CardDescription>
          {type === "current" 
            ? "Skills you already have mastered"
            : "Skills you need to develop"
          }
        </CardDescription>
      </CardHeader>
      <CardContent>
        <div className="space-y-2">
          {skills.map((skill) => (
            <div
              key={skill}
              className={`flex items-center gap-2 p-2 rounded-lg ${getBgColor()}`}
            >
              {getIcon()}
              <span className={`font-medium ${getTextColor()}`}>{skill}</span>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>
  );
}