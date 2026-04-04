import { useState, useEffect } from "react";
import { availableSkills } from "../data/skills";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
import { Search, Plus, X, TrendingUp, Star } from "lucide-react";

interface SkillSelectorProps {
  selectedSkills: string[];
  onSkillsChange: (skills: string[]) => void;
}

export function SkillSelector({ selectedSkills, onSkillsChange }: SkillSelectorProps) {
  const [searchTerm, setSearchTerm] = useState("");
  const [customSkill, setCustomSkill] = useState("");

  const filteredSkills = availableSkills.filter((skill) =>
    skill.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const popularSkills = availableSkills.slice(0, 8);

  const addSkill = (skill: string) => {
    if (!selectedSkills.includes(skill)) {
      onSkillsChange([...selectedSkills, skill]);
    }
  };

  const removeSkill = (skill: string) => {
    onSkillsChange(selectedSkills.filter((s) => s !== skill));
  };

  const addCustomSkill = () => {
    if (customSkill.trim() && !selectedSkills.includes(customSkill.trim())) {
      onSkillsChange([...selectedSkills, customSkill.trim()]);
      setCustomSkill("");
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === "Enter") {
      addCustomSkill();
    }
  };

  return (
    <Card>
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          <Search className="w-5 h-5 text-blue-600" />
          Select Your Current Skills
        </CardTitle>
        <CardDescription>
          Choose the skills you already have. You can search or add custom skills.
        </CardDescription>
      </CardHeader>
      <CardContent className="space-y-4">
        {/* Search Input */}
        <div className="relative">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-4 h-4" />
          <Input
            placeholder="Search skills..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="pl-10"
          />
        </div>

        {/* Custom Skill Input */}
        <div className="flex gap-2">
          <Input
            placeholder="Add a custom skill..."
            value={customSkill}
            onChange={(e) => setCustomSkill(e.target.value)}
            onKeyPress={handleKeyPress}
          />
          <Button onClick={addCustomSkill} size="sm">
            <Plus className="w-4 h-4" />
          </Button>
        </div>

        {/* Popular Skills */}
        {!searchTerm && (
          <div>
            <h4 className="font-medium text-gray-900 mb-2 flex items-center gap-2">
              <TrendingUp className="w-4 h-4" />
              Popular Skills
            </h4>
            <div className="flex flex-wrap gap-2">
              {popularSkills.map((skill) => (
                <Button
                  key={skill.name}
                  variant={selectedSkills.includes(skill.name) ? "default" : "outline"}
                  size="sm"
                  onClick={() => addSkill(skill.name)}
                  className="text-xs"
                >
                  {skill.name}
                </Button>
              ))}
            </div>
          </div>
        )}

        {/* Search Results */}
        {searchTerm && filteredSkills.length > 0 && (
          <div>
            <h4 className="font-medium text-gray-900 mb-2">Search Results</h4>
            <div className="flex flex-wrap gap-2">
              {filteredSkills.map((skill) => (
                <Button
                  key={skill.name}
                  variant={selectedSkills.includes(skill.name) ? "default" : "outline"}
                  size="sm"
                  onClick={() => addSkill(skill.name)}
                  className="text-xs"
                >
                  {skill.name}
                </Button>
              ))}
            </div>
          </div>
        )}

        {/* Selected Skills */}
        {selectedSkills.length > 0 && (
          <div>
            <h4 className="font-medium text-gray-900 mb-2 flex items-center gap-2">
              <Star className="w-4 h-4" />
              Your Skills ({selectedSkills.length})
            </h4>
            <div className="flex flex-wrap gap-2">
              {selectedSkills.map((skill) => (
                <Badge
                  key={skill}
                  variant="secondary"
                  className="text-xs bg-blue-100 text-blue-800 border-blue-200"
                >
                  {skill}
                  <button
                    onClick={() => removeSkill(skill)}
                    className="ml-1 hover:text-blue-600"
                  >
                    <X className="w-3 h-3" />
                  </button>
                </Badge>
              ))}
            </div>
          </div>
        )}

        {/* No Results */}
        {searchTerm && filteredSkills.length === 0 && (
          <div className="text-center py-4">
            <p className="text-gray-500 text-sm">No skills found. Try adding it as a custom skill.</p>
          </div>
        )}
      </CardContent>
    </Card>
  );
}