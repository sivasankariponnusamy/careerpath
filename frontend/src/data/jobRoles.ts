export interface JobRole {
  id: string;
  title: string;
  description: string;
  requiredSkills: string[];
  averageSalary?: string;
  growthRate?: string;
  difficulty?: string;
  jobSearchLinks?: {
    platform: string;
    url: string;
    description: string;
  }[];
  careerResources?: {
    title: string;
    url: string;
    description: string;
  }[];
}

export const jobRoles: JobRole[] = [
  {
    id: "frontend-developer",
    title: "Frontend Developer",
    description: "Build user interfaces and web applications using modern JavaScript frameworks",
    requiredSkills: [
      "JavaScript",
      "HTML5",
      "CSS3",
      "React",
      "TypeScript",
      "Git",
      "REST API",
      "Responsive Design",
      "Testing",
      "Performance"
    ],
    averageSalary: "$70,000 - $120,000",
    growthRate: "15%",
    difficulty: "Intermediate",
    jobSearchLinks: [
      {
        platform: "LinkedIn",
        url: "https://www.linkedin.com/jobs/frontend-developer-jobs",
        description: "Professional networking and job board"
      },
      {
        platform: "Indeed",
        url: "https://www.indeed.com/q-Frontend-Developer-jobs.html",
        description: "Large job search engine"
      },
      {
        platform: "AngelList",
        url: "https://angel.co/job-roles/frontend-developer",
        description: "Startup job opportunities"
      },
      {
        platform: "Stack Overflow Jobs",
        url: "https://stackoverflow.com/jobs/developer-jobs",
        description: "Developer-focused job board"
      }
    ],
    careerResources: [
      {
        title: "Frontend Developer Roadmap",
        url: "https://roadmap.sh/frontend",
        description: "Comprehensive learning path for frontend development"
      },
      {
        title: "MDN Web Docs",
        url: "https://developer.mozilla.org/",
        description: "Comprehensive web development documentation"
      }
    ]
  },
  {
    id: "backend-developer",
    title: "Backend Developer",
    description: "Design and implement server-side logic, databases, and APIs",
    requiredSkills: [
      "Node.js",
      "Python",
      "SQL",
      "REST API",
      "Docker",
      "Git",
      "Testing",
      "Security",
      "Performance",
      "System Design"
    ],
    averageSalary: "$80,000 - $140,000",
    growthRate: "18%",
    difficulty: "Intermediate",
    jobSearchLinks: [
      {
        platform: "LinkedIn",
        url: "https://www.linkedin.com/jobs/backend-developer-jobs",
        description: "Professional networking and job board"
      },
      {
        platform: "Indeed",
        url: "https://www.indeed.com/q-Backend-Developer-jobs.html",
        description: "Large job search engine"
      },
      {
        platform: "Hired",
        url: "https://hired.com/",
        description: "Tech-focused job marketplace"
      },
      {
        platform: "Built In",
        url: "https://www.builtincolorado.com/jobs",
        description: "Tech hub job boards"
      }
    ],
    careerResources: [
      {
        title: "Backend Developer Roadmap",
        url: "https://roadmap.sh/backend",
        description: "Comprehensive learning path for backend development"
      },
      {
        title: "System Design Primer",
        url: "https://github.com/donnemartin/system-design-primer",
        description: "Learn system design concepts"
      }
    ]
  },
  {
    id: "fullstack-developer",
    title: "Full Stack Developer",
    description: "Work on both frontend and backend development of web applications",
    requiredSkills: [
      "JavaScript",
      "React",
      "Node.js",
      "Python",
      "SQL",
      "MongoDB",
      "Docker",
      "Git",
      "REST API",
      "System Design",
      "Testing",
      "Security"
    ],
    averageSalary: "$90,000 - $160,000",
    growthRate: "20%",
    difficulty: "Advanced",
    jobSearchLinks: [
      {
        platform: "LinkedIn",
        url: "https://www.linkedin.com/jobs/fullstack-developer-jobs",
        description: "Professional networking and job board"
      },
      {
        platform: "Indeed",
        url: "https://www.indeed.com/q-Full-Stack-Developer-jobs.html",
        description: "Large job search engine"
      },
      {
        platform: "AngelList",
        url: "https://angel.co/job-roles/full-stack-developer",
        description: "Startup job opportunities"
      },
      {
        platform: "Hired",
        url: "https://hired.com/",
        description: "Tech-focused job marketplace"
      }
    ],
    careerResources: [
      {
        title: "Full Stack Developer Roadmap",
        url: "https://roadmap.sh/full-stack",
        description: "Comprehensive learning path for full stack development"
      },
      {
        title: "FreeCodeCamp",
        url: "https://www.freecodecamp.org/",
        description: "Free coding bootcamp with full stack curriculum"
      }
    ]
  },
  {
    id: "data-scientist",
    title: "Data Scientist",
    description: "Analyze complex data to help companies make better business decisions",
    requiredSkills: [
      "Python",
      "Machine Learning",
      "Data Analysis",
      "SQL",
      "Statistics",
      "Pandas",
      "NumPy",
      "Data Visualization",
      "Deep Learning",
      "TensorFlow"
    ],
    averageSalary: "$95,000 - $165,000",
    growthRate: "22%",
    difficulty: "Advanced",
    jobSearchLinks: [
      {
        platform: "LinkedIn",
        url: "https://www.linkedin.com/jobs/data-scientist-jobs",
        description: "Professional networking and job board"
      },
      {
        platform: "Kaggle",
        url: "https://www.kaggle.com/jobs",
        description: "Data science competitions and jobs"
      },
      {
        platform: "Indeed",
        url: "https://www.indeed.com/q-Data-Scientist-jobs.html",
        description: "Large job search engine"
      },
      {
        platform: "Hired",
        url: "https://hired.com/",
        description: "Tech-focused job marketplace"
      }
    ],
    careerResources: [
      {
        title: "Data Scientist Roadmap",
        url: "https://roadmap.sh/data-scientist",
        description: "Comprehensive learning path for data science"
      },
      {
        title: "Kaggle Learn",
        url: "https://www.kaggle.com/learn",
        description: "Free data science courses"
      }
    ]
  },
  {
    id: "devops-engineer",
    title: "DevOps Engineer",
    description: "Bridge the gap between development and operations, automating and improving processes",
    requiredSkills: [
      "Docker",
      "Kubernetes",
      "CI/CD",
      "AWS",
      "Linux",
      "Git",
      "Terraform",
      "Monitoring",
      "Security",
      "Scripting"
    ],
    averageSalary: "$100,000 - $170,000",
    growthRate: "25%",
    difficulty: "Advanced",
    jobSearchLinks: [
      {
        platform: "LinkedIn",
        url: "https://www.linkedin.com/jobs/devops-engineer-jobs",
        description: "Professional networking and job board"
      },
      {
        platform: "DevOpsJobs",
        url: "https://devopsjobs.dev/",
        description: "DevOps-focused job board"
      },
      {
        platform: "Indeed",
        url: "https://www.indeed.com/q-DevOps-Engineer-jobs.html",
        description: "Large job search engine"
      },
      {
        platform: "Hired",
        url: "https://hired.com/",
        description: "Tech-focused job marketplace"
      }
    ],
    careerResources: [
      {
        title: "DevOps Engineer Roadmap",
        url: "https://roadmap.sh/devops",
        description: "Comprehensive learning path for DevOps"
      },
      {
        title: "Kubernetes Documentation",
        url: "https://kubernetes.io/docs/",
        description: "Official Kubernetes documentation"
      }
    ]
  },
  {
    id: "mobile-developer",
    title: "Mobile Developer",
    description: "Create applications for iOS and Android devices",
    requiredSkills: [
      "React Native",
      "Flutter",
      "JavaScript",
      "TypeScript",
      "Mobile UI/UX",
      "Git",
      "Testing",
      "Performance",
      "API Integration",
      "State Management"
    ],
    averageSalary: "$85,000 - $150,000",
    growthRate: "19%",
    difficulty: "Intermediate",
    jobSearchLinks: [
      {
        platform: "LinkedIn",
        url: "https://www.linkedin.com/jobs/mobile-developer-jobs",
        description: "Professional networking and job board"
      },
      {
        platform: "Indeed",
        url: "https://www.indeed.com/q-Mobile-Developer-jobs.html",
        description: "Large job search engine"
      },
      {
        platform: "AngelList",
        url: "https://angel.co/job-roles/mobile-developer",
        description: "Startup job opportunities"
      },
      {
        platform: "Built In",
        url: "https://www.builtincolorado.com/jobs",
        description: "Tech hub job boards"
      }
    ],
    careerResources: [
      {
        title: "Mobile Developer Roadmap",
        url: "https://roadmap.sh/mobile",
        description: "Comprehensive learning path for mobile development"
      },
      {
        title: "React Native Docs",
        url: "https://reactnative.dev/docs/getting-started",
        description: "Official React Native documentation"
      }
    ]
  },
  {
    id: "ui-ux-designer",
    title: "UI/UX Designer",
    description: "Design user interfaces and experiences for digital products",
    requiredSkills: [
      "User Research",
      "Wireframing",
      "Prototyping",
      "Visual Design",
      "Figma",
      "Adobe XD",
      "HTML5",
      "CSS3",
      "User Testing",
      "Design Systems"
    ],
    averageSalary: "$75,000 - $130,000",
    growthRate: "13%",
    difficulty: "Intermediate",
    jobSearchLinks: [
      {
        platform: "LinkedIn",
        url: "https://www.linkedin.com/jobs/ui-ux-designer-jobs",
        description: "Professional networking and job board"
      },
      {
        platform: "Indeed",
        url: "https://www.indeed.com/q-UI-UX-Designer-jobs.html",
        description: "Large job search engine"
      },
      {
        platform: "Dribbble",
        url: "https://dribbble.com/jobs",
        description: "Design-focused job board"
      },
      {
        platform: "Behance",
        url: "https://www.behance.net/joblist",
        description: "Adobe's creative job platform"
      }
    ],
    careerResources: [
      {
        title: "UI/UX Designer Roadmap",
        url: "https://roadmap.sh/ui-ux-design",
        description: "Comprehensive learning path for UI/UX design"
      },
      {
        title: "Figma Learn",
        url: "https://www.figma.com/resources/learn-design/",
        description: "Free design courses from Figma"
      }
    ]
  },
  {
    id: "cloud-engineer",
    title: "Cloud Engineer",
    description: "Design, implement, and manage cloud infrastructure and services",
    requiredSkills: [
      "AWS",
      "Google Cloud",
      "Azure",
      "Docker",
      "Kubernetes",
      "Terraform",
      "Linux",
      "Networking",
      "Security",
      "Monitoring"
    ],
    averageSalary: "$105,000 - $180,000",
    growthRate: "24%",
    difficulty: "Advanced",
    jobSearchLinks: [
      {
        platform: "LinkedIn",
        url: "https://www.linkedin.com/jobs/cloud-engineer-jobs",
        description: "Professional networking and job board"
      },
      {
        platform: "Cloud Careers",
        url: "https://cloudcareers.io/",
        description: "Cloud-focused job board"
      },
      {
        platform: "Indeed",
        url: "https://www.indeed.com/q-Cloud-Engineer-jobs.html",
        description: "Large job search engine"
      },
      {
        platform: "Hired",
        url: "https://hired.com/",
        description: "Tech-focused job marketplace"
      }
    ],
    careerResources: [
      {
        title: "Cloud Engineer Roadmap",
        url: "https://roadmap.sh/cloud",
        description: "Comprehensive learning path for cloud engineering"
      },
      {
        title: "AWS Training",
        url: "https://aws.amazon.com/training/",
        description: "Official AWS training and certification"
      }
    ]
  }
];