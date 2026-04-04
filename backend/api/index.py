# Lightweight Flask API for Vercel serverless deployment
from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import os

app = Flask(__name__)
CORS(app, origins="*")

# Built-in comprehensive skill list
ALL_SKILLS = [
    'Python', 'JavaScript', 'TypeScript', 'Java', 'C++', 'C#', 'Go', 'Rust', 'PHP', 'Ruby',
    'Swift', 'Kotlin', 'Scala', 'R', 'MATLAB', 'Perl', 'Bash', 'Shell',
    'React', 'Angular', 'Vue', 'HTML', 'CSS', 'Node.js', 'Express', 'Flask', 'Django',
    'FastAPI', 'Spring', 'Spring Boot', 'Laravel', 'Rails', 'Next.js', 'Nuxt.js',
    'Tailwind', 'Bootstrap', 'jQuery', 'Redux', 'GraphQL', 'REST API', 'gRPC',
    'MongoDB', 'PostgreSQL', 'MySQL', 'SQLite', 'SQL', 'NoSQL', 'Redis', 'Cassandra',
    'Oracle', 'DynamoDB', 'Elasticsearch', 'Firebase', 'Supabase',
    'Docker', 'Kubernetes', 'AWS', 'Azure', 'GCP', 'CI/CD', 'Jenkins', 'GitHub Actions',
    'Git', 'Linux', 'Nginx', 'Apache', 'Terraform', 'Ansible', 'Prometheus', 'Grafana',
    'EC2', 'S3', 'Lambda', 'RDS',
    'Machine Learning', 'Deep Learning', 'TensorFlow', 'PyTorch', 'Scikit-learn',
    'NLP', 'Computer Vision', 'OpenCV', 'LangChain', 'RAG',
    'Pandas', 'NumPy', 'Matplotlib', 'Seaborn', 'Jupyter', 'Data Analysis',
    'PowerBI', 'Tableau', 'Excel', 'Apache Spark', 'Kafka',
    'Android', 'iOS', 'React Native', 'Flutter', 'Dart',
    'Figma', 'Adobe XD', 'Sketch', 'UI/UX', 'Wireframing', 'Prototyping',
    'Agile', 'Scrum', 'Jira', 'Project Management', 'Leadership',
    'Problem Solving', 'Teamwork', 'Communication',
    'Cybersecurity', 'Network Security', 'Penetration Testing',
    'Blockchain', 'Solidity', 'Web3',
    'OpenAI', 'HuggingFace', 'BERT', 'GPT',
    'RabbitMQ', 'Celery', 'WebSocket', 'OAuth', 'JWT', 'Microservices',
    'Unit Testing', 'Jest', 'Pytest', 'Selenium', 'Cypress',
]

SKILL_ALIASES = {
    'Python': ['python'],
    'JavaScript': ['javascript', 'js'],
    'TypeScript': ['typescript', 'ts'],
    'Java': ['java'],
    'C++': ['c++', 'cpp'],
    'C#': ['c#', 'csharp'],
    'Go': ['golang', 'go'],
    'React': ['react', 'reactjs', 'react.js'],
    'Angular': ['angular', 'angularjs'],
    'Vue': ['vue', 'vuejs', 'vue.js'],
    'HTML': ['html', 'html5'],
    'CSS': ['css', 'css3'],
    'Node.js': ['node.js', 'nodejs', 'node'],
    'Flask': ['flask'],
    'Django': ['django'],
    'FastAPI': ['fastapi', 'fast api'],
    'Spring Boot': ['spring boot'],
    'Spring': ['spring'],
    'MongoDB': ['mongodb', 'mongo'],
    'PostgreSQL': ['postgresql', 'postgres'],
    'MySQL': ['mysql'],
    'SQL': ['sql'],
    'Redis': ['redis'],
    'Docker': ['docker'],
    'Kubernetes': ['kubernetes', 'k8s'],
    'AWS': ['aws', 'amazon web services'],
    'Azure': ['azure', 'microsoft azure'],
    'GCP': ['gcp', 'google cloud'],
    'Git': ['git', 'github', 'gitlab'],
    'Linux': ['linux', 'unix'],
    'Machine Learning': ['machine learning', 'ml'],
    'Deep Learning': ['deep learning', 'dl'],
    'TensorFlow': ['tensorflow'],
    'PyTorch': ['pytorch'],
    'Scikit-learn': ['scikit-learn', 'sklearn', 'scikit learn'],
    'NLP': ['nlp', 'natural language processing'],
    'Computer Vision': ['computer vision'],
    'OpenCV': ['opencv'],
    'Pandas': ['pandas'],
    'NumPy': ['numpy'],
    'Data Analysis': ['data analysis', 'data analytics'],
    'PowerBI': ['powerbi', 'power bi'],
    'Tableau': ['tableau'],
    'Apache Spark': ['apache spark', 'spark'],
    'Kafka': ['kafka'],
    'React Native': ['react native'],
    'Flutter': ['flutter'],
    'Figma': ['figma'],
    'REST API': ['rest api', 'restful', 'rest'],
    'GraphQL': ['graphql'],
    'Docker': ['docker'],
    'CI/CD': ['ci/cd', 'cicd'],
    'Microservices': ['microservices', 'microservice'],
    'Agile': ['agile'],
    'Scrum': ['scrum'],
    'JWT': ['jwt'],
    'OAuth': ['oauth'],
    'Tailwind': ['tailwind', 'tailwindcss'],
    'Bootstrap': ['bootstrap'],
    'Next.js': ['next.js', 'nextjs'],
    'Jest': ['jest'],
    'Pytest': ['pytest'],
    'Selenium': ['selenium'],
    'Blockchain': ['blockchain'],
    'Solidity': ['solidity'],
    'Firebase': ['firebase'],
    'Elasticsearch': ['elasticsearch'],
    'Terraform': ['terraform'],
    'Ansible': ['ansible'],
    'Kotlin': ['kotlin'],
    'Swift': ['swift'],
    'LangChain': ['langchain'],
    'HuggingFace': ['huggingface', 'hugging face'],
    'OpenAI': ['openai'],
    'GPT': ['gpt', 'chatgpt'],
}

SKILL_CATEGORIES = {
    'Programming Languages': ['Python', 'JavaScript', 'TypeScript', 'Java', 'C++', 'C#', 'Go', 'Rust', 'PHP', 'Ruby', 'Swift', 'Kotlin', 'Scala', 'R'],
    'Web Technologies': ['React', 'Angular', 'Vue', 'HTML', 'CSS', 'Flask', 'Django', 'Node.js', 'Express', 'FastAPI', 'Spring Boot', 'Tailwind', 'Bootstrap', 'Next.js', 'Redux', 'jQuery'],
    'Databases': ['MongoDB', 'PostgreSQL', 'MySQL', 'SQL', 'NoSQL', 'Redis', 'Cassandra', 'Oracle', 'DynamoDB', 'Firebase', 'Elasticsearch'],
    'DevOps & Cloud': ['Docker', 'Kubernetes', 'AWS', 'Azure', 'GCP', 'CI/CD', 'Jenkins', 'GitHub Actions', 'Git', 'Linux', 'Terraform', 'Ansible'],
    'AI & Machine Learning': ['Machine Learning', 'Deep Learning', 'TensorFlow', 'PyTorch', 'Scikit-learn', 'NLP', 'Computer Vision', 'OpenCV', 'LangChain', 'OpenAI', 'HuggingFace'],
    'Data': ['Pandas', 'NumPy', 'Data Analysis', 'PowerBI', 'Tableau', 'Apache Spark', 'Kafka', 'Jupyter'],
    'Mobile': ['Android', 'iOS', 'React Native', 'Flutter'],
    'Tools & Practices': ['Agile', 'Scrum', 'Jira', 'REST API', 'GraphQL', 'Microservices', 'JWT', 'OAuth'],
    'Design': ['Figma', 'Adobe XD', 'UI/UX', 'Wireframing'],
    'Soft Skills': ['Problem Solving', 'Teamwork', 'Communication', 'Leadership', 'Project Management'],
}

def detect_role(skills_lower):
    role_scores = {
        'Frontend Developer': ['react', 'angular', 'vue', 'html', 'css', 'javascript', 'typescript', 'tailwind', 'next.js', 'redux'],
        'Backend Developer': ['python', 'java', 'node.js', 'flask', 'django', 'fastapi', 'spring boot', 'postgresql', 'mysql', 'rest api'],
        'Full Stack Developer': ['react', 'node.js', 'python', 'javascript', 'mongodb', 'postgresql', 'html', 'css', 'express'],
        'Data Scientist': ['python', 'machine learning', 'pandas', 'numpy', 'scikit-learn', 'tensorflow', 'pytorch', 'data analysis', 'r', 'jupyter'],
        'DevOps Engineer': ['docker', 'kubernetes', 'aws', 'azure', 'ci/cd', 'linux', 'terraform', 'jenkins', 'git', 'ansible'],
        'Mobile Developer': ['android', 'ios', 'react native', 'flutter', 'swift', 'kotlin', 'dart'],
        'Machine Learning Engineer': ['machine learning', 'deep learning', 'tensorflow', 'pytorch', 'scikit-learn', 'nlp', 'computer vision', 'python', 'huggingface'],
        'Data Engineer': ['python', 'apache spark', 'kafka', 'sql', 'aws', 'data analysis', 'pandas', 'airflow'],
        'Cloud Engineer': ['aws', 'azure', 'gcp', 'docker', 'kubernetes', 'terraform', 'ec2', 's3', 'lambda'],
        'UI/UX Designer': ['figma', 'adobe xd', 'ui/ux', 'wireframing', 'prototyping', 'css', 'sketch'],
    }
    scores = {role: sum(1 for s in keywords if s in skills_lower) for role, keywords in role_scores.items()}
    sorted_roles = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    result = []
    for role, score in sorted_roles[:3]:
        if score > 0:
            pct = min(score * 12, 90)
            result.append({'role': role, 'match_percentage': pct, 'confidence': 'High' if pct > 60 else 'Medium'})
    return result


@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'service': 'CareerPath AI Backend'})


@app.route('/api/extract-skills', methods=['POST'])
def extract_skills():
    if 'resume' not in request.files:
        return jsonify({'error': 'No resume file provided'}), 400

    file = request.files['resume']
    if not file.filename:
        return jsonify({'error': 'No file selected'}), 400

    filename = file.filename.lower()
    content = ''

    try:
        if filename.endswith('.txt'):
            content = file.read().decode('utf-8', errors='ignore')

        elif filename.endswith('.pdf'):
            try:
                from PyPDF2 import PdfReader
                import io
                pdf_reader = PdfReader(io.BytesIO(file.read()))
                for page in pdf_reader.pages:
                    content += (page.extract_text() or '') + '\n'
            except ImportError:
                return jsonify({'error': 'PDF parsing not available. Please upload a .txt file.'}), 400

        elif filename.endswith('.docx'):
            try:
                from docx import Document
                import io
                doc = Document(io.BytesIO(file.read()))
                content = '\n'.join(p.text for p in doc.paragraphs)
            except ImportError:
                return jsonify({'error': 'DOCX parsing not available. Please upload a .txt file.'}), 400

        else:
            content = file.read().decode('utf-8', errors='ignore')

    except Exception as e:
        return jsonify({'error': f'Could not read file: {str(e)}'}), 400

    if not content.strip():
        return jsonify({'error': 'No text content found in the file'}), 400

    content_lower = content.lower()

    # Match skills using aliases
    found_skills = set()
    for canonical, aliases in SKILL_ALIASES.items():
        for alias in aliases:
            pattern = r'\b' + re.escape(alias) + r'\b'
            if re.search(pattern, content_lower):
                found_skills.add(canonical)
                break

    # Also direct match against ALL_SKILLS
    for skill in ALL_SKILLS:
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, content_lower):
            found_skills.add(skill)

    found_skills = list(found_skills)

    # Categorize
    categorized = {}
    for skill in found_skills:
        for cat, skills_list in SKILL_CATEGORIES.items():
            if skill in skills_list:
                categorized.setdefault(cat, []).append(skill)
                break

    skills_lower = [s.lower() for s in found_skills]
    suggested_roles = detect_role(skills_lower)
    top_match = None
    if suggested_roles:
        top = suggested_roles[0]
        top_match = {
            'role': top['role'],
            'match_percentage': top['match_percentage'],
            'message': f"Your skills match {top['role']} ({top['match_percentage']:.0f}% match)"
        }

    return jsonify({
        'skills': found_skills,
        'categorized_skills': categorized,
        'suggested_roles': suggested_roles,
        'top_match': top_match,
        'total_skills': len(found_skills)
    })


@app.route('/api/skills', methods=['GET'])
def get_skills():
    return jsonify({'skills': ALL_SKILLS})

