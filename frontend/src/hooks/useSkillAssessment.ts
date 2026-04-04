import { useState } from "react";
import { assessmentQuestions } from "../data/assessmentQuestions";
import { SkillAssessment } from "../types";

export function useSkillAssessment() {
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [answers, setAnswers] = useState<number[]>([]);
  const [selectedSkill, setSelectedSkill] = useState<string>("");
  const [isAssessmentComplete, setIsAssessmentComplete] = useState(false);
  const [assessment, setAssessment] = useState<SkillAssessment | null>(null);

  const getQuestionsForSkill = (skill: string) => {
    return assessmentQuestions.filter(q => q.skill === skill);
  };

  const startAssessment = (skill: string) => {
    setSelectedSkill(skill);
    setCurrentQuestionIndex(0);
    setAnswers([]);
    setIsAssessmentComplete(false);
    setAssessment(null);
  };

  const answerQuestion = (answerIndex: number) => {
    const newAnswers = [...answers, answerIndex];
    setAnswers(newAnswers);

    const questions = getQuestionsForSkill(selectedSkill);
    
    if (currentQuestionIndex < questions.length - 1) {
      setCurrentQuestionIndex(currentQuestionIndex + 1);
    } else {
      completeAssessment(newAnswers);
    }
  };

  const completeAssessment = (finalAnswers: number[]) => {
    const questions = getQuestionsForSkill(selectedSkill);
    const correctAnswers = finalAnswers.filter((answer, index) => 
      answer === questions[index].correctAnswer
    ).length;
    
    const score = Math.round((correctAnswers / questions.length) * 100);
    
    let level: 'Beginner' | 'Intermediate' | 'Advanced';
    if (score >= 80) {
      level = 'Advanced';
    } else if (score >= 50) {
      level = 'Intermediate';
    } else {
      level = 'Beginner';
    }

    const recommendations = generateRecommendations(selectedSkill, score, level);
    const nextSteps = generateNextSteps(selectedSkill, level);

    setAssessment({
      skill: selectedSkill,
      score,
      level,
      recommendations,
      nextSteps
    });
    
    setIsAssessmentComplete(true);
  };

  const generateRecommendations = (skill: string, score: number, level: string): string[] => {
    const recommendations: string[] = [];
    
    if (score < 50) {
      recommendations.push(`Focus on ${skill} fundamentals and basic concepts`);
      recommendations.push(`Practice with beginner-level exercises and tutorials`);
      recommendations.push(`Consider taking a structured course on ${skill}`);
    } else if (score < 80) {
      recommendations.push(`Strengthen your understanding of intermediate ${skill} concepts`);
      recommendations.push(`Work on small projects to apply your knowledge`);
      recommendations.push(`Study advanced topics and best practices`);
    } else {
      recommendations.push(`Explore advanced ${skill} topics and specializations`);
      recommendations.push(`Contribute to open-source projects`);
      recommendations.push(`Mentor others and share your knowledge`);
    }
    
    return recommendations;
  };

  const generateNextSteps = (skill: string, level: string): string[] => {
    const nextSteps: string[] = [];
    
    switch (skill) {
      case "JavaScript":
        if (level === 'Beginner') {
          nextSteps.push("Learn about data types and variables");
          nextSteps.push("Practice with arrays and objects");
          nextSteps.push("Understand functions and scope");
        } else if (level === 'Intermediate') {
          nextSteps.push("Master closures and prototypes");
          nextSteps.push("Learn async/await and promises");
          nextSteps.push("Study design patterns");
        } else {
          nextSteps.push("Explore performance optimization");
          nextSteps.push("Learn about memory management");
          nextSteps.push("Study advanced ES6+ features");
        }
        break;
      case "React":
        if (level === 'Beginner') {
          nextSteps.push("Learn JSX and components");
          nextSteps.push("Understand props and state");
          nextSteps.push("Practice with hooks");
        } else if (level === 'Intermediate') {
          nextSteps.push("Master context and reducers");
          nextSteps.push("Learn about performance optimization");
          nextSteps.push("Study custom hooks");
        } else {
          nextSteps.push("Explore server-side rendering");
          nextSteps.push("Learn about advanced patterns");
          nextSteps.push("Study React internals");
        }
        break;
      default:
        nextSteps.push("Continue practicing and building projects");
        nextSteps.push("Stay updated with latest developments");
        nextSteps.push("Join communities and forums");
    }
    
    return nextSteps;
  };

  const resetAssessment = () => {
    setCurrentQuestionIndex(0);
    setAnswers([]);
    setSelectedSkill("");
    setIsAssessmentComplete(false);
    setAssessment(null);
  };

  return {
    currentQuestionIndex,
    answers,
    selectedSkill,
    isAssessmentComplete,
    assessment,
    startAssessment,
    answerQuestion,
    resetAssessment,
    getQuestionsForSkill
  };
}