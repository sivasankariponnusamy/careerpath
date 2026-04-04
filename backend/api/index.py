from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import io

app = Flask(__name__)
CORS(app, origins="*")

SKILL_ALIASES = {
    'Python': [r'\bpython\b'],
    'JavaScript': [r'\bjavascript\b', r'\bes6\b'],
    'TypeScript': [r'\btypescript\b'],
    'Java': [r'\bjava\b(?!\s*script)'],
    'C++': [r'c\+\+', r'\bcpp\b'],
    'C#': [r'c#', r'\.net\b'],
    'Go': [r'\bgolang\b'],
    'Rust': [r'\brust\b'],
    'PHP': [r'\bphp\b'],
    'Ruby': [r'\bruby\b'],
    'Swift': [r'\bswift\b'],
    'Kotlin': [r'\bkotlin\b'],
    'Scala': [r'\bscala\b'],
    'Dart': [r'\bdart\b'],
    'Bash': [r'\bbash\b', r'\bshell scripting\b'],
    'React': [r'\breact\.?js\b', r'\breactjs\b', r'\breact\b'],
    'Angular': [r'\bangular\b'],
    'Vue': [r'\bvue\.?js\b'],
    'HTML': [r'\bhtml5?\b'],
    'CSS': [r'\bcss3?\b', r'\bsass\b'],
    'Node.js': [r'\bnode\.?js\b'],
    'Express': [r'\bexpress\.?js\b', r'\bexpress\b'],
    'Flask': [r'\bflask\b'],
    'Django': [r'\bdjango\b'],
    'FastAPI': [r'\bfastapi\b'],
    'Spring Boot': [r'\bspring boot\b'],
    'Next.js': [r'\bnext\.?js\b'],
    'Redux': [r'\bredux\b'],
    'Tailwind': [r'\btailwind\b'],
    'Bootstrap': [r'\bbootstrap\b'],
    'jQuery': [r'\bjquery\b'],
    'GraphQL': [r'\bgraphql\b'],
    'REST API': [r'\brest api\b', r'\brestful\b', r'\bapi development\b'],
    'MongoDB': [r'\bmongodb\b', r'\bmongo\b'],
    'PostgreSQL': [r'\bpostgresql\b', r'\bpostgres\b'],
    'MySQL': [r'\bmysql\b'],
    'SQL': [r'\bsql\b', r'\brdbms\b'],
    'NoSQL': [r'\bnosql\b'],
    'Redis': [r'\bredis\b'],
    'Elasticsearch': [r'\belasticsearch\b'],
    'Firebase': [r'\bfirebase\b'],
    'Docker': [r'\bdocker\b', r'\bcontainerization\b'],
    'Kubernetes': [r'\bkubernetes\b', r'\bk8s\b'],
    'AWS': [r'\baws\b', r'\bamazon web services\b'],
    'Azure': [r'\bazure\b', r'\bmicrosoft azure\b'],
    'GCP': [r'\bgcp\b', r'\bgoogle cloud\b'],
    'CI/CD': [r'\bci/cd\b', r'\bcontinuous integration\b'],
    'Jenkins': [r'\bjenkins\b'],
    'Git': [r'\bgit\b', r'\bgithub\b', r'\bgitlab\b'],
    'Linux': [r'\blinux\b', r'\bunix\b', r'\bubuntu\b'],
    'Terraform': [r'\bterraform\b'],
    'Ansible': [r'\bansible\b'],
    'Machine Learning': [r'\bmachine learning\b', r'\bml model\b'],
    'Deep Learning': [r'\bdeep learning\b', r'\bneural network\b'],
    'TensorFlow': [r'\btensorflow\b'],
    'PyTorch': [r'\bpytorch\b'],
    'Scikit-learn': [r'\bscikit.?learn\b', r'\bsklearn\b'],
    'NLP': [r'\bnlp\b', r'\bnatural language processing\b', r'\bsentiment analysis\b'],
    'Computer Vision': [r'\bcomputer vision\b', r'\bimage recognition\b'],
    'OpenCV': [r'\bopencv\b'],
    'LangChain': [r'\blangchain\b'],
    'OpenAI': [r'\bopenai\b', r'\bchatgpt\b', r'\bgpt-?[34o]?\b', r'\bllm\b'],
    'HuggingFace': [r'\bhugging.?face\b', r'\btransformers\b'],
    'Pandas': [r'\bpandas\b'],
    'NumPy': [r'\bnumpy\b'],
    'Matplotlib': [r'\bmatplotlib\b'],
    'Jupyter': [r'\bjupyter\b'],
    'Data Analysis': [r'\bdata analysis\b', r'\bdata analytics\b', r'\beda\b'],
    'PowerBI': [r'\bpower.?bi\b'],
    'Tableau': [r'\btableau\b'],
    'Excel': [r'\bexcel\b'],
    'Apache Spark': [r'\bapache spark\b', r'\bpyspark\b'],
    'Kafka': [r'\bkafka\b'],
    'Airflow': [r'\bairflow\b'],
    'Android': [r'\bandroid\b'],
    'iOS': [r'\bios development\b', r'\bxcode\b'],
    'React Native': [r'\breact native\b'],
    'Flutter': [r'\bflutter\b'],
    'Figma': [r'\bfigma\b'],
    'Adobe XD': [r'\badobe xd\b'],
    'UI/UX': [r'\bui/ux\b', r'\bux design\b', r'\buser experience\b'],
    'Wireframing': [r'\bwireframing\b', r'\bprototyping\b'],
    'Agile': [r'\bagile\b'],
    'Scrum': [r'\bscrum\b'],
    'Jira': [r'\bjira\b'],
    'Project Management': [r'\bproject management\b'],
    'Microservices': [r'\bmicroservices\b'],
    'JWT': [r'\bjwt\b'],
    'OAuth': [r'\boauth\b'],
    'Cybersecurity': [r'\bcybersecurity\b', r'\bnetwork security\b', r'\bpenetration testing\b'],
    'Blockchain': [r'\bblockchain\b'],
    'Solidity': [r'\bsolidity\b'],
    'Jest': [r'\bjest\b'],
    'Pytest': [r'\bpytest\b'],
    'Selenium': [r'\bselenium\b'],
    'OOP': [r'\boop\b', r'\bobject.?oriented\b'],
    'Data Structures': [r'\bdata structures?\b', r'\bdsa\b'],
    'Problem Solving': [r'\bproblem.?solving\b', r'\balgorithms?\b'],
    'Teamwork': [r'\bteamwork\b', r'\bcollaboration\b'],
    'Communication': [r'\bcommunication skills\b'],
    'Leadership': [r'\bleadership\b', r'\bteam lead\b'],
}

SKILL_CATEGORIES = {
    'Programming Languages': ['Python','JavaScript','TypeScript','Java','C++','C#','Go','Rust','PHP','Ruby','Swift','Kotlin','Scala','Dart','Bash'],
    'Web Technologies': ['React','Angular','Vue','HTML','CSS','Node.js','Express','Flask','Django','FastAPI','Spring Boot','Next.js','Redux','Tailwind','Bootstrap','jQuery','GraphQL','REST API'],
    'Databases': ['MongoDB','PostgreSQL','MySQL','SQL','NoSQL','Redis','Elasticsearch','Firebase'],
    'DevOps & Cloud': ['Docker','Kubernetes','AWS','Azure','GCP','CI/CD','Jenkins','Git','Linux','Terraform','Ansible'],
    'AI & Machine Learning': ['Machine Learning','Deep Learning','TensorFlow','PyTorch','Scikit-learn','NLP','Computer Vision','OpenCV','LangChain','OpenAI','HuggingFace'],
    'Data & Analytics': ['Pandas','NumPy','Matplotlib','Jupyter','Data Analysis','PowerBI','Tableau','Excel','Apache Spark','Kafka','Airflow'],
    'Mobile': ['Android','iOS','React Native','Flutter'],
    'Design': ['Figma','Adobe XD','UI/UX','Wireframing'],
    'Practices & Tools': ['Agile','Scrum','Jira','Project Management','Microservices','JWT','OAuth','Jest','Pytest','Selenium','Blockchain','Cybersecurity'],
    'Fundamentals': ['OOP','Data Structures','Problem Solving'],
    'Soft Skills': ['Teamwork','Communication','Leadership'],
}

ROLE_KEYWORDS = {
    'Frontend Developer':        {'react':4,'angular':4,'vue':4,'html':3,'css':3,'javascript':3,'typescript':2,'tailwind':2,'next.js':3,'redux':2,'jquery':1},
    'Backend Developer':         {'python':2,'java':2,'node.js':3,'flask':4,'django':4,'fastapi':4,'spring boot':4,'postgresql':3,'mysql':3,'rest api':3,'mongodb':2,'redis':2},
    'Full Stack Developer':      {'react':3,'node.js':3,'javascript':2,'python':2,'mongodb':2,'postgresql':2,'html':2,'css':2,'express':3,'rest api':2},
    'Data Scientist':            {'python':3,'machine learning':4,'pandas':4,'numpy':4,'scikit-learn':4,'tensorflow':3,'pytorch':3,'data analysis':4,'jupyter':3},
    'Machine Learning Engineer': {'machine learning':4,'deep learning':4,'tensorflow':4,'pytorch':4,'scikit-learn':3,'nlp':3,'computer vision':3,'python':3,'huggingface':3,'langchain':3},
    'DevOps Engineer':           {'docker':4,'kubernetes':4,'aws':3,'azure':3,'ci/cd':4,'linux':3,'terraform':4,'ansible':3,'jenkins':3},
    'Cloud Engineer':            {'aws':4,'azure':4,'gcp':4,'docker':3,'kubernetes':3,'terraform':3},
    'Data Engineer':             {'python':2,'apache spark':4,'kafka':4,'airflow':4,'sql':3,'aws':2,'pandas':3},
    'Mobile Developer':          {'android':4,'ios':4,'react native':4,'flutter':4,'swift':4,'kotlin':4,'dart':3},
    'UI/UX Designer':            {'figma':4,'adobe xd':4,'ui/ux':4,'wireframing':4,'css':2},
    'Blockchain Developer':      {'blockchain':4,'solidity':4},
    'Cybersecurity Engineer':    {'cybersecurity':4,'network security':3,'linux':2,'python':2},
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
        pct = min(round((score / max_score) * 92, 1), 95)
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
