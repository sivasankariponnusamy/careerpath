import { jobRoles } from "../data/jobRoles";

export interface SkillGapResult {
  missingSkills: string[];
  currentSkills: string[];
  matchPercentage: number;
  estimatedTime: string;
}

export function calculateSkillGap(
  userSkills: string[],
  targetRoleId: string
): SkillGapResult {
  const targetRole = jobRoles.find((role) => role.id === targetRoleId);
  
  if (!targetRole) {
    return {
      missingSkills: [],
      currentSkills: userSkills,
      matchPercentage: 0,
      estimatedTime: "Unknown"
    };
  }

  const requiredSkills = targetRole.requiredSkills;
  const missingSkills = requiredSkills.filter(
    (skill) => !userSkills.includes(skill)
  );
  
  const matchedSkills = requiredSkills.filter((skill) =>
    userSkills.includes(skill)
  );
  
  const matchPercentage = Math.round(
    (matchedSkills.length / requiredSkills.length) * 100
  );

  // Estimate learning time based on missing skills
  const estimatedMonths = Math.max(1, missingSkills.length * 1.5);
  const estimatedTime = estimatedMonths < 12 
    ? `${Math.round(estimatedMonths)} months`
    : `${Math.round(estimatedMonths / 12)} years`;

  return {
    missingSkills,
    currentSkills: matchedSkills,
    matchPercentage,
    estimatedTime
  };
}