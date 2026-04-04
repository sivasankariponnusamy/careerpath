from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import io

app = Flask(__name__)
CORS(app, origins="*")

SKILL_ALIASES = {
    'Python': ['python'],
    'JavaScript': ['javascript', r'\bjs\b'],
    'TypeScript': ['typescript'],
    'Java': [r'\bjava\b'],
    'C++': [r'c\+\+', r'\bcpp\b'],
    'C#': [r'c#', r'\bcsharp\b'],
    'Go': [r'\bgolang\b'],
    'Rust': [r'\brust\b'],
    'PHP': [r'\bphp\b'],
    'Ruby': [r'\bruby\b'],
    'Swift': [r'\bswift\b'],
    'Kotlin': [r'\bkotlin\b'],
    'Scala': [r'\bscala\b'],
    'Bash': [r'\bbash\b', r'\bshell scripting\b'],
    'React': [r'\breact\.?js\b', r'\breactjs\b', r'\breact\b'],
    'Angular': [r'\bangular\b'],
    'Vue': [r'\bvue\.?js\b', r'\bvuejs\b'],
    'HTML': [r'\bhtml5?\b'],
    'CSS': [r'\bcss3?\b'],
    'Node.js': [r'\bnode\.?js\b'],
    'Express': [r'\bexpress\.?js\b', r'\bexpress\b'],
    'Flask': [r'\bflask\b'],
    'Django': [r'\bdjango\b'],
    'FastAPI': [r'\bfastapi\b'],
    'Spring Boot': [r'\bspring boot\b'],
    'Spring': [r'\bspring\b'],
    'Next.js': [r'\bnext\.?js\b'],
    'Redux': [r'\bredux\b'],
    'Tailwind': [r'\btailwind\b'],
    'Bootstrap': [r'\bbootstrap\b'],
    'jQuery': [r'\bjquery\b'],
    'GraphQL': [r'\bgraphql\b'],
    'REST API': [r'\brest api\b', r'\brestful\b'],
    'MongoDB': [r'\bmongodb\b', r'\bmongo\b'],
    'PostgreSQL': [r'\bpostgresql\b', r'\bpostgres\b'],
    'MySQL': [r'\bmysql\b'],
    'SQL': [r'\bsql\b'],
    'NoSQL': [r'\bnosql\b'],
    'Redis': [r'\bredis\b'],
    'Elasticsearch': [r'\belasticsearch\b'],
    'Firebase': [r'\bfirebase\b'],
    'Docker': [r'\bdocker\b'],
    'Kubernetes': [r'\bkubernetes\b', r'\bk8s\b'],
    'AWS': [r'\baws\b', r'\bamazon web services\b'],
    'Azure': [r'\bazure\b', r'\bmicrosoft azure\b'],
    'GCP': [r'\bgcp\b', r'\bgoogle cloud\b'],
    'CI/CD': [r'\bci/cd\b', r'\bcicd\b', r'\bcontinuous integration\b'],
    'Git': [r'\bgit\b', r'\bgithub\b', r'\bgitlab\b'],
    'Linux': [r'\blinux\b', r'\bunix\b'],
    'Terraform': [r'\bterraform\b'],
    'Ansible': [r'\bansible\b'],
    'Machine Learning': [r'\bmachine learning\b'],
    'Deep Learning': [r'\bdeep learning\b'],
    'TensorFlow': [r'\btensorflow\b'],
    'PyTorch': [r'\bpytorch\b'],
    'Scikit-learn': [r'\bscikit.?learn\b', r'\bsklearn\b'],
    'NLP': [r'\bnlp\b', r'\bnatural language processing\b'],
    'Computer Vision': [r'\bcomputer vision\b'],
    'OpenCV': [r'\bopencv\b'],
    'LangChain': [r'\blangchain\b'],
    'Pandas': [r'\bpandas\b'],
    'NumPy': [r'\bnumpy\b'],
    'Matplotlib': [r'\bmatplotlib\b'],
    'Jupyter': [r'\bjupyter\b'],
    'Data Analysis': [r'\bdata analysis\b', r'\bdata analytics\b'],
    'PowerBI': [r'\bpower.?bi\b'],
    'Tableau': [r'\btableau\b'],
    'Excel': [r'\bexcel\b'],
    'Apache Spark': [r'\bapache spark\b', r'\bpyspark\b'],
    'Kafka': [r'\bkafka\b'],
    'Android': [r'\bandroid\b'],
    'iOS': [r'\bios development\b', r'\bios app\b'],
    'React Native': [r'\breact native\b'],
    'Flutter': [r'\bflutter\b'],
    'Figma': [r'\bfigma\b'],
    'Adobe XD': [r'\badobe xd\b'],
    'UI/UX': [r'\bui/ux\b', r'\bux design\b', r'\buser experience\b'],
    'Agile': [r'\bagile\b'],
    'Scrum': [r'\bscrum\b'],
    'Jira': [r'\bjira\b'],
    'Project Management': [r'\bproject management\b'],
    'Problem Solving': [r'\bproblem.?solving\b'],
    'Teamwork': [r'\bteamwork\b'],
    'Communication': [r'\bcommunication\b'],
    'Leadership': [r'\bleadership\b'],
    'Cybersecurity': [r'\bcybersecurity\b', r'\bcyber security\b'],
    'Blockchain': [r'\bblockchain\b'],
    'Solidity': [r'\bsolidity\b'],
    'OpenAI': [r'\bopenai\b', r'\bchatgpt\b'],
    'HuggingFace': [r'\bhugging.?face\b'],
    'Microservices': [r'\bmicroservices\b'],
    'JWT': [r'\bjwt\b'],
    'OAuth': [r'\boauth\b'],
    'Jest': [r'\bjest\b'],
    'Pytest': [r'\bpytest\b'],
    'Selenium': [r'\bselenium\b'],
    'Cypress': [r'\bcypress\b'],
}

SKILL_CATEGORIES = {
    'Programming Languages': ['Python','JavaScript','TypeScript','Java','C++','C#','Go','Rust','PHP','Ruby','Swift','Kotlin','Scala','Bash'],
    'Web Technologies': ['React','Angular','Vue','HTML','CSS','Node.js','Express','Flask','Django','FastAPI','Spring Boot','Spring','Next.js','Redux','Tailwind','Bootstrap','jQuery','GraphQL','REST API'],
    'Databases': ['MongoDB','PostgreSQL','MySQL','SQL','NoSQL','Redis','Elasticsearch','Firebase'],
    'DevOps & Cloud': ['Docker','Kubernetes','AWS','Azure','GCP','CI/CD','Git','Linux','Terraform','Ansible'],
    'AI & Machine Learning': ['Machine Learning','Deep Learning','TensorFlow','PyTorch','Scikit-learn','NLP','Computer Vision','OpenCV','LangChain','OpenAI','HuggingFace'],
    'Data & Analytics': ['Pandas','NumPy','Matplotlib','Jupyter','Data Analysis','PowerBI','Tableau','Excel','Apache Spark','Kafka'],
    'Mobile': ['Android','iOS','React Native','Flutter'],
    'Design': ['Figma','Adobe XD','UI/UX'],
    'Practices & Tools': ['Agile','Scrum','Jira','Project Management','Microservices','JWT','OAuth','Jest','Pytest','Selenium','Cypress','Blockchain','Cybersecurity'],
    'Soft Skills': ['Problem Solving','Teamwork','Communication','Leadership'],
}

ROLE_KEYWORDS = {
    'Frontend Developer': {'react':3,'angular':3,'vue':3,'html':2,'css':2,'javascript':3,'typescript':2,'tailwind':2,'next.js':2,'redux':2},
    'Backend Developer': {'python':2,'java':2,'node.js':3,'flask':3,'django':3,'fastapi':3,'spring boot':3,'postgresql':2,'mysql':2,'rest api':2,'mongodb':2},
    'Full Stack Developer': {'react':2,'node.js':2,'python':2,'javascript':2,'mongodb':2,'postgresql':2,'html':1,'css':1,'express':2},
    'Data Scientist': {'python':3,'machine learning':3,'pandas':3,'numpy':3,'scikit-learn':3,'tensorflow':2,'pytorch':2,'data analysis':3,'jupyter':2},
    'DevOps Engineer': {'docker':3,'kubernetes':3,'aws':2,'azure':2,'ci/cd':3,'linux':2,'terraform':3,'git':1,'ansible':2},
    'Mobile Developer': {'android':3,'ios':3,'react native':3,'flutter':3,'swift':3,'kotlin':3},
    'Machine Learning Engineer': {'machine learning':3,'deep learning':3,'tensorflow':3,'pytorch':3,'scikit-learn':2,'nlp':2,'computer vision':2,'python':2,'huggingface':2},
    'Data Engineer': {'python':2,'apache spark':3,'kafka':3,'sql':2,'aws':2,'data analysis':2,'pandas':2},
    'Cloud Engineer': {'aws':3,'azure':3,'gcp':3,'docker':2,'kubernetes':3,'terraform':3},
    'UI/UX Designer': {'figma':3,'adobe xd':3,'ui/ux':3,'css':1},
    'Blockchain Developer': {'blockchain':3,'solidity':3,'javascript':1,'python':1},
}

def detect_roles(skills):
    sl = [s.lower() for s in skills]
    scores = {}
    for role, kw_weights in ROLE_KEYWORDS.items():
        score = sum(w for kw, w in kw_weights.items() if kw in sl)
        if score > 0:
            scores[role] = score
    if not scores:
        return []
    max_score = max(scores.values())
    result = []
    for role, score in sorted(scores.items(), key=lambda x: -x[1])[:5]:
        pct = min(round((score / max_score) * 90, 1), 95)
        result.append({
            'role': role,
            'match_percentage': pct,
            'confidence': 'High' if pct >= 70 else 'Medium' if pct >= 40 else 'Low'
        })
    return result


def read_file_content(file):
    filename = file.filename.lower()
    if filename.endswith('.pdf'):
        try:
            from PyPDF2 import PdfReader
            reader = PdfReader(io.BytesIO(file.read()))
            text = '\n'.join(page.extract_text() or '' for page in reader.pages)
            if not text.strip():
                return None, "PDF appears scanned. Please upload a text-based PDF or .txt file."
            return text, None
        except Exception as e:
            return None, f"Could not parse PDF: {str(e)}"
    elif filename.endswith('.docx'):
        try:
            from docx import Document
            doc = Document(io.BytesIO(file.read()))
            return '\n'.join(p.text for p in doc.paragraphs), None
        except Exception as e:
            return None, f"Could not parse DOCX: {str(e)}"
    else:
        try:
            return file.read().decode('utf-8', errors='ignore'), None
        except Exception as e:
            return None, f"Could not read file: {str(e)}"


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

    content, err = read_file_content(file)
    if err:
        return jsonify({'error': err}), 400
    if not content or not content.strip():
        return jsonify({'error': 'No text content found in the file'}), 400

    content_lower = content.lower()
    found_skills = set()
    for canonical, patterns in SKILL_ALIASES.items():
        for pat in patterns:
            try:
                if re.search(pat, content_lower):
                    found_skills.add(canonical)
                    break
            except re.error:
                pass

    found_skills = list(found_skills)

    categorized = {}
    for skill in found_skills:
        for cat, skills_list in SKILL_CATEGORIES.items():
            if skill in skills_list:
                categorized.setdefault(cat, []).append(skill)
                break

    suggested_roles = detect_roles(found_skills)
    top_match = None
    if suggested_roles:
        top = suggested_roles[0]
        top_match = {
            'role': top['role'],
            'match_percentage': top['match_percentage'],
            'message': f"Your skills best match {top['role']} ({top['match_percentage']}% match)"
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
    return jsonify({'skills': list(SKILL_ALIASES.keys())})
