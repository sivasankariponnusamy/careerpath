import { AssessmentQuestion } from "../types";

export const assessmentQuestions: AssessmentQuestion[] = [
  // JavaScript Questions
  {
    id: "js-1",
    skill: "JavaScript",
    question: "What is the output of: console.log(typeof null)?",
    options: ["null", "undefined", "object", "string"],
    correctAnswer: 2,
    difficulty: "Beginner",
    explanation: "In JavaScript, typeof null returns 'object'. This is a known bug in the language."
  },
  {
    id: "js-2",
    skill: "JavaScript",
    question: "Which method is used to add an element to the end of an array?",
    options: ["push()", "pop()", "shift()", "unshift()"],
    correctAnswer: 0,
    difficulty: "Beginner",
    explanation: "The push() method adds one or more elements to the end of an array."
  },
  {
    id: "js-3",
    skill: "JavaScript",
    question: "What is closure in JavaScript?",
    options: [
      "A function that returns another function",
      "A function that has access to variables in its outer scope",
      "A way to close browser windows",
      "A method to stop function execution"
    ],
    correctAnswer: 1,
    difficulty: "Intermediate",
    explanation: "A closure is a function that has access to variables in its outer (enclosing) lexical scope even when the outer function has finished executing."
  },
  {
    id: "js-4",
    skill: "JavaScript",
    question: "What does the 'async' keyword do?",
    options: [
      "Makes a function run faster",
      "Makes a function return a Promise",
      "Makes a function synchronous",
      "Makes a function run in parallel"
    ],
    correctAnswer: 1,
    difficulty: "Intermediate",
    explanation: "The async keyword makes a function return a Promise automatically."
  },
  
  // React Questions
  {
    id: "react-1",
    skill: "React",
    question: "What is JSX?",
    options: [
      "JavaScript XML",
      "Java Syntax Extension",
      "JSON XML",
      "JavaScript Extension"
    ],
    correctAnswer: 0,
    difficulty: "Beginner",
    explanation: "JSX stands for JavaScript XML. It is a syntax extension for JavaScript that allows you to write HTML-like code in your JavaScript files."
  },
  {
    id: "react-2",
    skill: "React",
    question: "Which hook is used for side effects?",
    options: ["useState", "useEffect", "useContext", "useReducer"],
    correctAnswer: 1,
    difficulty: "Beginner",
    explanation: "useEffect is the hook used for side effects in functional components."
  },
  {
    id: "react-3",
    skill: "React",
    question: "What is the purpose of React.memo?",
    options: [
      "To memoize function results",
      "To prevent unnecessary re-renders",
      "To store component state",
      "To handle component lifecycle"
    ],
    correctAnswer: 1,
    difficulty: "Intermediate",
    explanation: "React.memo is a higher-order component that memoizes the rendered output and prevents unnecessary re-renders if props haven't changed."
  },
  
  // Python Questions
  {
    id: "python-1",
    skill: "Python",
    question: "What is the correct file extension for Python files?",
    options: [".py", ".python", ".pt", ".pyt"],
    correctAnswer: 0,
    difficulty: "Beginner",
    explanation: "Python files use the .py extension."
  },
  {
    id: "python-2",
    skill: "Python",
    question: "Which keyword is used to define a function in Python?",
    options: ["function", "def", "func", "define"],
    correctAnswer: 1,
    difficulty: "Beginner",
    explanation: "The 'def' keyword is used to define a function in Python."
  },
  {
    id: "python-3",
    skill: "Python",
    question: "What is a Python decorator?",
    options: [
      "A function that modifies another function",
      "A way to decorate code with colors",
      "A GUI component",
      "A data structure"
    ],
    correctAnswer: 0,
    difficulty: "Intermediate",
    explanation: "A decorator is a function that takes another function as input and extends or modifies its behavior without changing its source code."
  },
  
  // SQL Questions
  {
    id: "sql-1",
    skill: "SQL",
    question: "Which SQL statement is used to retrieve data from a database?",
    options: ["GET", "RETRIEVE", "SELECT", "FETCH"],
    correctAnswer: 2,
    difficulty: "Beginner",
    explanation: "The SELECT statement is used to retrieve data from a database."
  },
  {
    id: "sql-2",
    skill: "SQL",
    question: "What does JOIN do in SQL?",
    options: [
      "Combines rows from two or more tables",
      "Creates a new table",
      "Deletes data",
      "Updates data"
    ],
    correctAnswer: 0,
    difficulty: "Beginner",
    explanation: "JOIN clauses are used to combine rows from two or more tables based on a related column."
  },
  {
    id: "sql-3",
    skill: "SQL",
    question: "What is the difference between INNER JOIN and LEFT JOIN?",
    options: [
      "INNER JOIN returns all rows, LEFT JOIN returns matching rows",
      "INNER JOIN returns matching rows, LEFT JOIN returns all rows from left table",
      "They are the same",
      "LEFT JOIN is faster than INNER JOIN"
    ],
    correctAnswer: 1,
    difficulty: "Intermediate",
    explanation: "INNER JOIN returns only the matching rows from both tables, while LEFT JOIN returns all rows from the left table and matching rows from the right table."
  },
  
  // Docker Questions
  {
    id: "docker-1",
    skill: "Docker",
    question: "What is a Docker image?",
    options: [
      "A running container",
      "A template for creating containers",
      "A virtual machine",
      "A configuration file"
    ],
    correctAnswer: 1,
    difficulty: "Beginner",
    explanation: "A Docker image is a read-only template used to create containers."
  },
  {
    id: "docker-2",
    skill: "Docker",
    question: "Which command is used to build a Docker image?",
    options: ["docker run", "docker build", "docker create", "docker make"],
    correctAnswer: 1,
    difficulty: "Beginner",
    explanation: "The 'docker build' command is used to build Docker images from a Dockerfile."
  },
  {
    id: "docker-3",
    skill: "Docker",
    question: "What is Docker Compose used for?",
    options: [
      "Building single containers",
      "Managing multi-container applications",
      "Container networking",
      "Container security"
    ],
    correctAnswer: 1,
    difficulty: "Intermediate",
    explanation: "Docker Compose is used for defining and running multi-container Docker applications."
  }
];