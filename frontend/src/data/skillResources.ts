export interface Resource {
  title: string;
  url: string;
  description: string;
  type: string;
  level: string;
  duration?: string;
  rating?: string;
  tags?: string[];
  prerequisites?: string[];
  instructor?: string;
  platform?: string;
  thumbnail?: string;
  views?: string;
  lastUpdated?: string;
}

export interface SkillResource {
  skill: string;
  resources: Resource[];
}

export const skillResources: SkillResource[] = [
  {
    skill: "React",
    resources: [
      {
        title: "React Official Documentation",
        url: "https://react.dev/",
        description: "Official React documentation with tutorials and guides",
        type: "Documentation",
        level: "Beginner",
        duration: "Self-paced",
        rating: "4.9/5",
        tags: ["Frontend", "JavaScript", "Library"],
        prerequisites: ["JavaScript", "HTML5", "CSS3"],
        platform: "React"
      },
      {
        title: "React Tutorial - freeCodeCamp",
        url: "https://www.freecodecamp.org/news/learn-react-by-building-a-weather-app/",
        description: "Hands-on React tutorial building a weather application",
        type: "Tutorial",
        level: "Beginner",
        duration: "4 hours",
        rating: "4.8/5",
        tags: ["Frontend", "JavaScript", "Project"],
        prerequisites: ["JavaScript", "HTML5", "CSS3"],
        platform: "freeCodeCamp"
      },
      {
        title: "React - The Complete Guide (incl. Hooks, React Router, Redux)",
        url: "https://www.udemy.com/course/react-the-complete-guide-incl-redux/",
        description: "Comprehensive React course covering everything from basics to advanced",
        type: "Course",
        level: "Beginner",
        duration: "48 hours",
        rating: "4.7/5",
        tags: ["Frontend", "JavaScript", "Comprehensive"],
        prerequisites: ["JavaScript", "HTML5", "CSS3"],
        instructor: "Maximilian Schwarzmüller",
        platform: "Udemy"
      },
      {
        title: "React Tutorial for Beginners",
        url: "https://www.youtube.com/watch?v=SqcY0GlETPk",
        description: "Complete React tutorial for beginners by Programming with Mosh",
        type: "Video",
        level: "Beginner",
        duration: "5 hours",
        rating: "4.8/5",
        tags: ["Frontend", "JavaScript", "Video Tutorial"],
        prerequisites: ["JavaScript", "HTML5", "CSS3"],
        instructor: "Programming with Mosh",
        platform: "YouTube",
        views: "8.2M",
        thumbnail: "react-tutorial"
      },
      {
        title: "React Hooks Tutorial",
        url: "https://www.youtube.com/watch?v=TNhaISOUy6Q",
        description: "Deep dive into React Hooks with practical examples",
        type: "Video",
        level: "Intermediate",
        duration: "2 hours",
        rating: "4.9/5",
        tags: ["Frontend", "JavaScript", "Hooks"],
        prerequisites: ["React", "JavaScript"],
        instructor: "Web Dev Simplified",
        platform: "YouTube",
        views: "2.1M",
        thumbnail: "react-hooks"
      },
      {
        title: "Advanced React Patterns",
        url: "https://www.youtube.com/watch?v=mwEhGg4_j3Y",
        description: "Learn advanced React patterns and performance optimization",
        type: "Video",
        level: "Advanced",
        duration: "3 hours",
        rating: "4.7/5",
        tags: ["Frontend", "JavaScript", "Advanced"],
        prerequisites: ["React", "JavaScript", "Hooks"],
        instructor: "Kent C. Dodds",
        platform: "YouTube",
        views: "450K",
        thumbnail: "advanced-react"
      }
    ]
  },
  {
    skill: "JavaScript",
    resources: [
      {
        title: "JavaScript MDN Guide",
        url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide",
        description: "Comprehensive JavaScript guide from Mozilla Developer Network",
        type: "Documentation",
        level: "Beginner",
        duration: "Self-paced",
        rating: "4.9/5",
        tags: ["Frontend", "Backend", "Programming"],
        prerequisites: ["Basic Programming"],
        platform: "MDN"
      },
      {
        title: "JavaScript.info",
        url: "https://javascript.info/",
        description: "Modern JavaScript tutorial from basics to advanced",
        type: "Tutorial",
        level: "Beginner",
        duration: "Self-paced",
        rating: "4.8/5",
        tags: ["Frontend", "Backend", "Programming"],
        prerequisites: ["Basic Programming"],
        platform: "JavaScript.info"
      },
      {
        title: "JavaScript - The Complete Guide 2023",
        url: "https://www.udemy.com/course/the-complete-javascript-course/",
        description: "Most comprehensive JavaScript course online",
        type: "Course",
        level: "Beginner",
        duration: "68 hours",
        rating: "4.8/5",
        tags: ["Frontend", "Backend", "Comprehensive"],
        prerequisites: ["Basic Programming"],
        instructor: "Jonas Schmedtmann",
        platform: "Udemy"
      },
      {
        title: "JavaScript Tutorial for Beginners",
        url: "https://www.youtube.com/watch?v=W6NZfCO5SIk",
        description: "Complete JavaScript tutorial for beginners by Programming with Mosh",
        type: "Video",
        level: "Beginner",
        duration: "6 hours",
        rating: "4.9/5",
        tags: ["Frontend", "Backend", "Video Tutorial"],
        prerequisites: ["Basic Programming"],
        instructor: "Programming with Mosh",
        platform: "YouTube",
        views: "12M",
        thumbnail: "javascript-basics"
      },
      {
        title: "JavaScript: Understanding the Weird Parts",
        url: "https://www.udemy.com/course/understand-javascript/",
        description: "Deep dive into JavaScript concepts and how it works",
        type: "Course",
        level: "Advanced",
        duration: "12 hours",
        rating: "4.7/5",
        tags: ["Frontend", "Backend", "Advanced"],
        prerequisites: ["JavaScript Basics"],
        instructor: "Anthony Alicea",
        platform: "Udemy"
      },
      {
        title: "Async JavaScript Tutorial",
        url: "https://www.youtube.com/watch?v=vFn0k1Tnl5k",
        description: "Master async/await, promises, and callbacks in JavaScript",
        type: "Video",
        level: "Intermediate",
        duration: "1.5 hours",
        rating: "4.8/5",
        tags: ["Frontend", "Backend", "Async"],
        prerequisites: ["JavaScript Basics"],
        instructor: "Web Dev Simplified",
        platform: "YouTube",
        views: "1.8M",
        thumbnail: "async-javascript"
      }
    ]
  },
  {
    skill: "TypeScript",
    resources: [
      {
        title: "TypeScript Handbook",
        url: "https://www.typescriptlang.org/docs/",
        description: "Official TypeScript documentation and handbook",
        type: "Documentation",
        level: "Intermediate",
        duration: "Self-paced",
        rating: "4.8/5",
        tags: ["Frontend", "Backend", "Type Safety"],
        prerequisites: ["JavaScript"],
        platform: "TypeScript"
      },
      {
        title: "TypeScript Tutorial - W3Schools",
        url: "https://www.w3schools.com/typescript/",
        description: "Beginner-friendly TypeScript tutorial with examples",
        type: "Tutorial",
        level: "Beginner",
        duration: "3 hours",
        rating: "4.7/5",
        tags: ["Frontend", "Backend", "Type Safety"],
        prerequisites: ["JavaScript"],
        platform: "W3Schools"
      },
      {
        title: "TypeScript - The Complete Guide",
        url: "https://www.udemy.com/course/understanding-typescript/",
        description: "Master TypeScript from basics to advanced concepts",
        type: "Course",
        level: "Beginner",
        duration: "28 hours",
        rating: "4.8/5",
        tags: ["Frontend", "Backend", "Type Safety"],
        prerequisites: ["JavaScript"],
        instructor: "Maximilian Schwarzmüller",
        platform: "Udemy"
      },
      {
        title: "TypeScript Tutorial for Beginners",
        url: "https://www.youtube.com/watch?v=BwuLxPH8IDs",
        description: "Complete TypeScript tutorial for beginners",
        type: "Video",
        level: "Beginner",
        duration: "4 hours",
        rating: "4.8/5",
        tags: ["Frontend", "Backend", "Video Tutorial"],
        prerequisites: ["JavaScript"],
        instructor: "Programming with Mosh",
        platform: "YouTube",
        views: "5.2M",
        thumbnail: "typescript-basics"
      },
      {
        title: "Advanced TypeScript Patterns",
        url: "https://www.youtube.com/watch?v=9oHz5T2P_0s",
        description: "Advanced TypeScript patterns and best practices",
        type: "Video",
        level: "Advanced",
        duration: "2 hours",
        rating: "4.7/5",
        tags: ["Frontend", "Backend", "Advanced"],
        prerequisites: ["TypeScript", "JavaScript"],
        instructor: "Matt Pocock",
        platform: "YouTube",
        views: "380K",
        thumbnail: "advanced-typescript"
      }
    ]
  },
  {
    skill: "Node.js",
    resources: [
      {
        title: "Node.js Official Documentation",
        url: "https://nodejs.org/en/docs/",
        description: "Official Node.js documentation and API reference",
        type: "Documentation",
        level: "Intermediate",
        duration: "Self-paced",
        rating: "4.7/5",
        tags: ["Backend", "JavaScript", "Runtime"],
        prerequisites: ["JavaScript"],
        platform: "Node.js"
      },
      {
        title: "Node.js Tutorial - freeCodeCamp",
        url: "https://www.freecodecamp.org/news/learn-nodejs-full-course/",
        description: "Complete Node.js course for beginners",
        type: "Tutorial",
        level: "Beginner",
        duration: "6 hours",
        rating: "4.8/5",
        tags: ["Backend", "JavaScript", "Runtime"],
        prerequisites: ["JavaScript"],
        platform: "freeCodeCamp"
      },
      {
        title: "Node.js - The Complete Guide",
        url: "https://www.udemy.com/course/nodejs-the-complete-guide/",
        description: "Build scalable network applications with Node.js",
        type: "Course",
        level: "Beginner",
        duration: "40 hours",
        rating: "4.7/5",
        tags: ["Backend", "JavaScript", "Comprehensive"],
        prerequisites: ["JavaScript"],
        instructor: "Maximilian Schwarzmüller",
        platform: "Udemy"
      },
      {
        title: "Node.js Tutorial for Beginners",
        url: "https://www.youtube.com/watch?v=TlB_eWDSMt4",
        description: "Complete Node.js tutorial for beginners",
        type: "Video",
        level: "Beginner",
        duration: "7 hours",
        rating: "4.8/5",
        tags: ["Backend", "JavaScript", "Video Tutorial"],
        prerequisites: ["JavaScript"],
        instructor: "Programming with Mosh",
        platform: "YouTube",
        views: "6.5M",
        thumbnail: "nodejs-basics"
      },
      {
        title: "Node.js Advanced Concepts",
        url: "https://www.youtube.com/watch?v=Oe421JkE95Y",
        description: "Advanced Node.js concepts and performance optimization",
        type: "Video",
        level: "Advanced",
        duration: "3 hours",
        rating: "4.6/5",
        tags: ["Backend", "JavaScript", "Advanced"],
        prerequisites: ["Node.js", "JavaScript"],
        instructor: "Fireship",
        platform: "YouTube",
        views: "1.2M",
        thumbnail: "advanced-nodejs"
      }
    ]
  },
  {
    skill: "Python",
    resources: [
      {
        title: "Python Official Tutorial",
        url: "https://docs.python.org/3/tutorial/",
        description: "Official Python tutorial for beginners",
        type: "Documentation",
        level: "Beginner",
        duration: "Self-paced",
        rating: "4.8/5",
        tags: ["Backend", "Data Science", "Programming"],
        prerequisites: ["Basic Programming"],
        platform: "Python"
      },
      {
        title: "Python for Everybody",
        url: "https://www.py4e.com/lessons",
        description: "Free Python course from University of Michigan",
        type: "Tutorial",
        level: "Beginner",
        duration: "8 hours",
        rating: "4.9/5",
        tags: ["Backend", "Data Science", "Programming"],
        prerequisites: ["Basic Programming"],
        platform: "Coursera"
      },
      {
        title: "2023 Complete Python Bootcamp",
        url: "https://www.udemy.com/course/complete-python-bootcamp/",
        description: "Learn Python like a professional from scratch",
        type: "Course",
        level: "Beginner",
        duration: "22 hours",
        rating: "4.6/5",
        tags: ["Backend", "Data Science", "Comprehensive"],
        prerequisites: ["Basic Programming"],
        instructor: "Jose Portilla",
        platform: "Udemy"
      },
      {
        title: "Python Tutorial for Beginners",
        url: "https://www.youtube.com/watch?v=rfscVS0vtbw",
        description: "Complete Python tutorial for beginners by freeCodeCamp",
        type: "Video",
        level: "Beginner",
        duration: "4 hours",
        rating: "4.8/5",
        tags: ["Backend", "Data Science", "Video Tutorial"],
        prerequisites: ["Basic Programming"],
        instructor: "freeCodeCamp",
        platform: "YouTube",
        views: "15M",
        thumbnail: "python-basics"
      },
      {
        title: "Python for Data Science",
        url: "https://www.youtube.com/watch?v=0Lt9w-BxKFQ",
        description: "Learn Python specifically for data science and machine learning",
        type: "Video",
        level: "Intermediate",
        duration: "6 hours",
        rating: "4.7/5",
        tags: ["Data Science", "Machine Learning", "Video Tutorial"],
        prerequisites: ["Python Basics"],
        instructor: "freeCodeCamp",
        platform: "YouTube",
        views: "3.2M",
        thumbnail: "python-data-science"
      },
      {
        title: "Advanced Python Tutorial",
        url: "https://www.youtube.com/watch?v=cb8R_kqV_hA",
        description: "Advanced Python concepts and best practices",
        type: "Video",
        level: "Advanced",
        duration: "2 hours",
        rating: "4.6/5",
        tags: ["Backend", "Advanced", "Video Tutorial"],
        prerequisites: ["Python"],
        instructor: "Corey Schafer",
        platform: "YouTube",
        views: "2.1M",
        thumbnail: "advanced-python"
      }
    ]
  },
  {
    skill: "SQL",
    resources: [
      {
        title: "SQL Tutorial - W3Schools",
        url: "https://www.w3schools.com/sql/",
        description: "Comprehensive SQL tutorial with interactive examples",
        type: "Tutorial",
        level: "Beginner",
        duration: "4 hours",
        rating: "4.7/5",
        tags: ["Database", "Querying", "Data"],
        prerequisites: ["Basic Computer Skills"],
        platform: "W3Schools"
      },
      {
        title: "SQLBolt",
        url: "https://sqlbolt.com/",
        description: "Interactive SQL lessons and exercises",
        type: "Tutorial",
        level: "Beginner",
        duration: "3 hours",
        rating: "4.6/5",
        tags: ["Database", "Querying", "Data"],
        prerequisites: ["Basic Computer Skills"],
        platform: "SQLBolt"
      },
      {
        title: "SQL - The Complete Bootcamp",
        url: "https://www.udemy.com/course/the-complete-sql-bootcamp/",
        description: "Go from SQL beginner to advanced",
        type: "Course",
        level: "Beginner",
        duration: "8 hours",
        rating: "4.6/5",
        tags: ["Database", "Querying", "Comprehensive"],
        prerequisites: ["Basic Computer Skills"],
        instructor: "Jose Portilla",
        platform: "Udemy"
      },
      {
        title: "SQL Tutorial for Beginners",
        url: "https://www.youtube.com/watch?v=HXV3zeQKqGY",
        description: "Complete SQL tutorial for beginners",
        type: "Video",
        level: "Beginner",
        duration: "1 hour",
        rating: "4.8/5",
        tags: ["Database", "Querying", "Video Tutorial"],
        prerequisites: ["Basic Computer Skills"],
        instructor: "Programming with Mosh",
        platform: "YouTube",
        views: "7.8M",
        thumbnail: "sql-basics"
      },
      {
        title: "Advanced SQL Tutorial",
        url: "https://www.youtube.com/watch?v=FR4QIeZaPeM",
        description: "Advanced SQL concepts and optimization techniques",
        type: "Video",
        level: "Advanced",
        duration: "2 hours",
        rating: "4.7/5",
        tags: ["Database", "Advanced", "Video Tutorial"],
        prerequisites: ["SQL Basics"],
        instructor: "freeCodeCamp",
        platform: "YouTube",
        views: "1.5M",
        thumbnail: "advanced-sql"
      }
    ]
  },
  {
    skill: "Docker",
    resources: [
      {
        title: "Docker Documentation",
        url: "https://docs.docker.com/get-started/",
        description: "Official Docker getting started guide",
        type: "Documentation",
        level: "Intermediate",
        duration: "Self-paced",
        rating: "4.7/5",
        tags: ["DevOps", "Containers", "Deployment"],
        prerequisites: ["Linux Basics"],
        platform: "Docker"
      },
      {
        title: "Docker Tutorial - freeCodeCamp",
        url: "https://www.freecodecamp.org/news/learn-docker/",
        description: "Complete Docker tutorial for developers",
        type: "Tutorial",
        level: "Beginner",
        duration: "5 hours",
        rating: "4.8/5",
        tags: ["DevOps", "Containers", "Deployment"],
        prerequisites: ["Linux Basics"],
        platform: "freeCodeCamp"
      },
      {
        title: "Docker & Kubernetes - The Practical Guide",
        url: "https://www.udemy.com/course/docker-kubernetes-the-practical-guide/",
        description: "Learn Docker and Kubernetes with practical examples",
        type: "Course",
        level: "Beginner",
        duration: "22 hours",
        rating: "4.7/5",
        tags: ["DevOps", "Containers", "Comprehensive"],
        prerequisites: ["Linux Basics"],
        instructor: "Maximilian Schwarzmüller",
        platform: "Udemy"
      },
      {
        title: "Docker Tutorial for Beginners",
        url: "https://www.youtube.com/watch?v=p2YvG8k44F8",
        description: "Complete Docker tutorial for beginners",
        type: "Video",
        level: "Beginner",
        duration: "1 hour",
        rating: "4.8/5",
        tags: ["DevOps", "Containers", "Video Tutorial"],
        prerequisites: ["Linux Basics"],
        instructor: "Programming with Mosh",
        platform: "YouTube",
        views: "4.2M",
        thumbnail: "docker-basics"
      },
      {
        title: "Docker Compose Tutorial",
        url: "https://www.youtube.com/watch?v=DIQ8MtUPCvE",
        description: "Learn Docker Compose for multi-container applications",
        type: "Video",
        level: "Intermediate",
        duration: "45 minutes",
        rating: "4.7/5",
        tags: ["DevOps", "Containers", "Video Tutorial"],
        prerequisites: ["Docker"],
        instructor: "NetworkChuck",
        platform: "YouTube",
        views: "850K",
        thumbnail: "docker-compose"
      }
    ]
  },
  {
    skill: "Kubernetes",
    resources: [
      {
        title: "Kubernetes Documentation",
        url: "https://kubernetes.io/docs/tutorials/",
        description: "Official Kubernetes tutorials and documentation",
        type: "Documentation",
        level: "Advanced",
        duration: "Self-paced",
        rating: "4.6/5",
        tags: ["DevOps", "Containers", "Orchestration"],
        prerequisites: ["Docker", "Linux"],
        platform: "Kubernetes"
      },
      {
        title: "Kubernetes Tutorial - freeCodeCamp",
        url: "https://www.freecodecamp.org/news/learn-kubernetes-full-course/",
        description: "Complete Kubernetes course for beginners",
        type: "Tutorial",
        level: "Intermediate",
        duration: "7 hours",
        rating: "4.7/5",
        tags: ["DevOps", "Containers", "Orchestration"],
        prerequisites: ["Docker", "Linux"],
        platform: "freeCodeCamp"
      },
      {
        title: "Certified Kubernetes Administrator (CKA) with Practice Tests",
        url: "https://www.udemy.com/course/certified-kubernetes-administrator-with-practice-tests/",
        description: "Prepare for Kubernetes certification",
        type: "Course",
        level: "Advanced",
        duration: "24 hours",
        rating: "4.7/5",
        tags: ["DevOps", "Containers", "Certification"],
        prerequisites: ["Docker", "Linux"],
        instructor: "Mumshad Mannambeth",
        platform: "Udemy"
      },
      {
        title: "Kubernetes Tutorial for Beginners",
        url: "https://www.youtube.com/watch?v=X48VuDVv0do",
        description: "Complete Kubernetes tutorial for beginners",
        type: "Video",
        level: "Beginner",
        duration: "2 hours",
        rating: "4.8/5",
        tags: ["DevOps", "Containers", "Video Tutorial"],
        prerequisites: ["Docker", "Linux"],
        instructor: "KodeKloud",
        platform: "YouTube",
        views: "2.8M",
        thumbnail: "kubernetes-basics"
      },
      {
        title: "Kubernetes in 5 Minutes",
        url: "https://www.youtube.com/watch?v=PH-2FfFD2PU",
        description: "Quick overview of Kubernetes concepts",
        type: "Video",
        level: "Beginner",
        duration: "5 minutes",
        rating: "4.6/5",
        tags: ["DevOps", "Containers", "Quick Overview"],
        prerequisites: ["Docker"],
        instructor: "Fireship",
        platform: "YouTube",
        views: "1.1M",
        thumbnail: "kubernetes-quick"
      }
    ]
  },
  {
    skill: "AWS",
    resources: [
      {
        title: "AWS Free Tier Tutorial",
        url: "https://aws.amazon.com/free/",
        description: "Get started with AWS free tier and tutorials",
        type: "Tutorial",
        level: "Beginner",
        duration: "Self-paced",
        rating: "4.7/5",
        tags: ["Cloud", "Infrastructure", "Services"],
        prerequisites: ["Basic Networking"],
        platform: "AWS"
      },
      {
        title: "AWS Documentation",
        url: "https://docs.aws.amazon.com/",
        description: "Comprehensive AWS documentation and guides",
        type: "Documentation",
        level: "Intermediate",
        duration: "Self-paced",
        rating: "4.6/5",
        tags: ["Cloud", "Infrastructure", "Services"],
        prerequisites: ["Basic Networking"],
        platform: "AWS"
      },
      {
        title: "AWS Certified Solutions Architect - Associate",
        url: "https://www.udemy.com/course/aws-certified-solutions-architect-associate/",
        description: "Prepare for AWS Solutions Architect certification",
        type: "Course",
        level: "Intermediate",
        duration: "27 hours",
        rating: "4.7/5",
        tags: ["Cloud", "Certification", "Comprehensive"],
        prerequisites: ["Basic Networking"],
        instructor: "Stephane Maarek",
        platform: "Udemy"
      },
      {
        title: "AWS Tutorial for Beginners",
        url: "https://www.youtube.com/watch?v=ulprqHHWlng",
        description: "Complete AWS tutorial for beginners",
        type: "Video",
        level: "Beginner",
        duration: "3 hours",
        rating: "4.8/5",
        tags: ["Cloud", "Infrastructure", "Video Tutorial"],
        prerequisites: ["Basic Networking"],
        instructor: "freeCodeCamp",
        platform: "YouTube",
        views: "5.5M",
        thumbnail: "aws-basics"
      },
      {
        title: "AWS in 100 Seconds",
        url: "https://www.youtube.com/watch?v=a9__D53Wsus",
        description: "Quick overview of AWS services",
        type: "Video",
        level: "Beginner",
        duration: "2 minutes",
        rating: "4.6/5",
        tags: ["Cloud", "Quick Overview"],
        prerequisites: ["Basic Computer Skills"],
        instructor: "Fireship",
        platform: "YouTube",
        views: "2.3M",
        thumbnail: "aws-quick"
      }
    ]
  },
  {
    skill: "Git",
    resources: [
      {
        title: "Git Tutorial - W3Schools",
        url: "https://www.w3schools.com/git/",
        description: "Learn Git version control with examples",
        type: "Tutorial",
        level: "Beginner",
        duration: "3 hours",
        rating: "4.8/5",
        tags: ["Version Control", "Collaboration", "Tools"],
        prerequisites: ["Basic Computer Skills"],
        platform: "W3Schools"
      },
      {
        title: "Pro Git Book",
        url: "https://git-scm.com/book/en/v2",
        description: "Comprehensive Git guide by the creators",
        type: "Documentation",
        level: "Intermediate",
        duration: "Self-paced",
        rating: "4.9/5",
        tags: ["Version Control", "Collaboration", "Tools"],
        prerequisites: ["Basic Computer Skills"],
        platform: "Git"
      },
      {
        title: "Git & GitHub - The Complete Guide",
        url: "https://www.udemy.com/course/git-and-github-bootcamp/",
        description: "Master Git and GitHub from scratch",
        type: "Course",
        level: "Beginner",
        duration: "8 hours",
        rating: "4.7/5",
        tags: ["Version Control", "Collaboration", "Comprehensive"],
        prerequisites: ["Basic Computer Skills"],
        instructor: "Colt Steele",
        platform: "Udemy"
      },
      {
        title: "Git Tutorial for Beginners",
        url: "https://www.youtube.com/watch?v=RGOj5yH7evk",
        description: "Complete Git tutorial for beginners",
        type: "Video",
        level: "Beginner",
        duration: "1 hour",
        rating: "4.8/5",
        tags: ["Version Control", "Video Tutorial"],
        prerequisites: ["Basic Computer Skills"],
        instructor: "Programming with Mosh",
        platform: "YouTube",
        views: "9.1M",
        thumbnail: "git-basics"
      },
      {
        title: "Git & GitHub Crash Course",
        url: "https://www.youtube.com/watch?v=SWYqp7iY_Tc",
        description: "Quick Git and GitHub crash course",
        type: "Video",
        level: "Beginner",
        duration: "45 minutes",
        rating: "4.7/5",
        tags: ["Version Control", "Video Tutorial"],
        prerequisites: ["Basic Computer Skills"],
        instructor: "freeCodeCamp",
        platform: "YouTube",
        views: "3.8M",
        thumbnail: "git-crash"
      }
    ]
  },
  {
    skill: "Machine Learning",
    resources: [
      {
        title: "Machine Learning by Andrew Ng",
        url: "https://www.coursera.org/learn/machine-learning",
        description: "Classic machine learning course by Andrew Ng",
        type: "Course",
        level: "Beginner",
        duration: "60 hours",
        rating: "4.9/5",
        tags: ["Data Science", "AI", "Comprehensive"],
        prerequisites: ["Python", "Mathematics"],
        instructor: "Andrew Ng",
        platform: "Coursera"
      },
      {
        title: "Machine Learning Tutorial for Beginners",
        url: "https://www.youtube.com/watch?v=ukzFI9rgwfU",
        description: "Complete machine learning tutorial for beginners",
        type: "Video",
        level: "Beginner",
        duration: "2 hours",
        rating: "4.8/5",
        tags: ["Data Science", "AI", "Video Tutorial"],
        prerequisites: ["Python", "Mathematics"],
        instructor: "Programming with Mosh",
        platform: "YouTube",
        views: "3.5M",
        thumbnail: "ml-basics"
      },
      {
        title: "Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow",
        url: "https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032618/",
        description: "Comprehensive book on practical machine learning",
        type: "Book",
        level: "Intermediate",
        duration: "Self-paced",
        rating: "4.8/5",
        tags: ["Data Science", "AI", "Practical"],
        prerequisites: ["Python", "Mathematics"],
        platform: "O'Reilly"
      },
      {
        title: "Machine Learning A-Z",
        url: "https://www.udemy.com/course/machinelearning/",
        description: "Comprehensive machine learning course",
        type: "Course",
        level: "Beginner",
        duration: "44 hours",
        rating: "4.5/5",
        tags: ["Data Science", "AI", "Comprehensive"],
        prerequisites: ["Python", "Mathematics"],
        instructor: "Kirill Eremenko",
        platform: "Udemy"
      },
      {
        title: "Deep Learning with TensorFlow",
        url: "https://www.youtube.com/watch?v=tPYj3fFJGjk",
        description: "Learn deep learning with TensorFlow",
        type: "Video",
        level: "Advanced",
        duration: "4 hours",
        rating: "4.7/5",
        tags: ["Data Science", "AI", "Deep Learning"],
        prerequisites: ["Python", "Machine Learning"],
        instructor: "freeCodeCamp",
        platform: "YouTube",
        views: "1.8M",
        thumbnail: "tensorflow-tutorial"
      }
    ]
  },
  {
    skill: "Data Analysis",
    resources: [
      {
        title: "Data Analysis with Python",
        url: "https://www.coursera.org/learn/data-analysis-with-python",
        description: "Learn data analysis using Python",
        type: "Course",
        level: "Beginner",
        duration: "20 hours",
        rating: "4.7/5",
        tags: ["Data Science", "Python", "Analysis"],
        prerequisites: ["Python"],
        platform: "Coursera"
      },
      {
        title: "Python for Data Analysis, 2nd Edition",
        url: "https://www.oreilly.com/library/view/python-for-data/9781491957660/",
        description: "Comprehensive guide to data analysis with Python",
        type: "Book",
        level: "Intermediate",
        duration: "Self-paced",
        rating: "4.6/5",
        tags: ["Data Science", "Python", "Analysis"],
        prerequisites: ["Python"],
        platform: "O'Reilly"
      },
      {
        title: "Data Analysis Tutorial",
        url: "https://www.youtube.com/watch?v=8Dv5yO_2-c0",
        description: "Complete data analysis tutorial with Python",
        type: "Video",
        level: "Beginner",
        duration: "3 hours",
        rating: "4.8/5",
        tags: ["Data Science", "Python", "Video Tutorial"],
        prerequisites: ["Python"],
        instructor: "freeCodeCamp",
        platform: "YouTube",
        views: "2.1M",
        thumbnail: "data-analysis"
      },
      {
        title: "Pandas Tutorial",
        url: "https://www.youtube.com/watch?v=vmEHCJofslg",
        description: "Learn Pandas for data analysis",
        type: "Video",
        level: "Beginner",
        duration: "1 hour",
        rating: "4.7/5",
        tags: ["Data Science", "Python", "Pandas"],
        prerequisites: ["Python"],
        instructor: "Corey Schafer",
        platform: "YouTube",
        views: "1.5M",
        thumbnail: "pandas-tutorial"
      }
    ]
  },
  {
    skill: "REST API",
    resources: [
      {
        title: "REST API Tutorial",
        url: "https://www.restapitutorial.com/",
        description: "Learn REST API concepts and best practices",
        type: "Tutorial",
        level: "Beginner",
        duration: "Self-paced",
        rating: "4.6/5",
        tags: ["Backend", "API", "Web Services"],
        prerequisites: ["HTTP", "JSON"],
        platform: "REST API Tutorial"
      },
      {
        title: "Building REST APIs with Node.js and Express",
        url: "https://www.youtube.com/watch?v=fgTGADljAeg",
        description: "Build REST APIs using Node.js and Express",
        type: "Video",
        level: "Intermediate",
        duration: "2 hours",
        rating: "4.8/5",
        tags: ["Backend", "API", "Node.js"],
        prerequisites: ["Node.js", "JavaScript"],
        instructor: "Traversy Media",
        platform: "YouTube",
        views: "2.8M",
        thumbnail: "rest-api-nodejs"
      },
      {
        title: "REST API Design Best Practices",
        url: "https://www.youtube.com/watch?v=7YcW25PHnAA",
        description: "Learn REST API design best practices",
        type: "Video",
        level: "Advanced",
        duration: "1 hour",
        rating: "4.7/5",
        tags: ["Backend", "API", "Design"],
        prerequisites: ["HTTP", "API Basics"],
        instructor: "freeCodeCamp",
        platform: "YouTube",
        views: "1.2M",
        thumbnail: "rest-api-design"
      }
    ]
  },
  {
    skill: "Testing",
    resources: [
      {
        title: "Testing JavaScript Applications",
        url: "https://www.udemy.com/course/testing-javascript/",
        description: "Comprehensive testing course for JavaScript",
        type: "Course",
        level: "Intermediate",
        duration: "12 hours",
        rating: "4.7/5",
        tags: ["Testing", "JavaScript", "Quality"],
        prerequisites: ["JavaScript"],
        instructor: "Kent C. Dodds",
        platform: "Udemy"
      },
      {
        title: "Jest Testing Tutorial",
        url: "https://www.youtube.com/watch?v=7r4xVDI2zw0",
        description: "Learn Jest testing framework",
        type: "Video",
        level: "Beginner",
        duration: "1 hour",
        rating: "4.8/5",
        tags: ["Testing", "JavaScript", "Jest"],
        prerequisites: ["JavaScript"],
        instructor: "Web Dev Simplified",
        platform: "YouTube",
        views: "850K",
        thumbnail: "jest-testing"
      },
      {
        title: "Testing Best Practices",
        url: "https://www.youtube.com/watch?v=Af4M8G5JXp0",
        description: "Testing best practices and patterns",
        type: "Video",
        level: "Advanced",
        duration: "1.5 hours",
        rating: "4.6/5",
        tags: ["Testing", "Best Practices"],
        prerequisites: ["Testing Basics"],
        instructor: "Kent C. Dodds",
        platform: "YouTube",
        views: "420K",
        thumbnail: "testing-best-practices"
      }
    ]
  },
  {
    skill: "Security",
    resources: [
      {
        title: "Web Security for Developers",
        url: "https://www.udemy.com/course/web-security-for-developers/",
        description: "Learn web security fundamentals",
        type: "Course",
        level: "Intermediate",
        duration: "8 hours",
        rating: "4.6/5",
        tags: ["Security", "Web Development"],
        prerequisites: ["Web Development"],
        instructor: "PortSwigger",
        platform: "Udemy"
      },
      {
        title: "OWASP Top 10",
        url: "https://owasp.org/www-project-top-ten/",
        description: "Most critical web application security risks",
        type: "Documentation",
        level: "Intermediate",
        duration: "Self-paced",
        rating: "4.8/5",
        tags: ["Security", "OWASP"],
        prerequisites: ["Web Development"],
        platform: "OWASP"
      },
      {
        title: "Web Security Tutorial",
        url: "https://www.youtube.com/watch?v=3wQaZIq9j2A",
        description: "Web security fundamentals for developers",
        type: "Video",
        level: "Beginner",
        duration: "1 hour",
        rating: "4.7/5",
        tags: ["Security", "Web Development"],
        prerequisites: ["Web Development"],
        instructor: "freeCodeCamp",
        platform: "YouTube",
        views: "1.8M",
        thumbnail: "web-security"
      }
    ]
  },
  {
    skill: "System Design",
    resources: [
      {
        title: "Grokking the System Design Interview",
        url: "https://www.educative.io/courses/grokking-the-system-design-interview",
        description: "System design interview preparation",
        type: "Course",
        level: "Advanced",
        duration: "20 hours",
        rating: "4.7/5",
        tags: ["System Design", "Interview"],
        prerequisites: ["Backend Development"],
        platform: "Educative"
      },
      {
        title: "System Design Primer",
        url: "https://github.com/donnemartin/system-design-primer",
        description: "Learn how to design large-scale systems",
        type: "Documentation",
        level: "Advanced",
        duration: "Self-paced",
        rating: "4.9/5",
        tags: ["System Design", "Architecture"],
        prerequisites: ["Backend Development"],
        platform: "GitHub"
      },
      {
        title: "System Design Interview",
        url: "https://www.youtube.com/watch?v=Z_ikdlimd6A",
        description: "System design interview preparation",
        type: "Video",
        level: "Advanced",
        duration: "2 hours",
        rating: "4.8/5",
        tags: ["System Design", "Interview"],
        prerequisites: ["Backend Development"],
        instructor: "Gaurav Sen",
        platform: "YouTube",
        views: "2.5M",
        thumbnail: "system-design"
      }
    ]
  }
];