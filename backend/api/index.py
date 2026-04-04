# Lightweight Flask API for Vercel serverless deployment
from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import io

app = Flask(__name__)
CORS(app, origins="*")

# ─── Skill aliases: canonical name → list of patterns to search ───────────────
SKILL_ALIASES = {
    'Python':            ['python'],
    'JavaScript':        ['javascript', r'\bjs\b', 'node\.js', 'nodejs'],
    'TypeScript':        ['typescript', r'\bts\b'],
    'Java':              [r'\bjava\b'],
    'C++':               [r'c\+\+', r'\bcpp\b'],
    'C#':                [r'c#', r'\bcsharp\b'],
    'Go':                [r'\bgolang\b', r'\bgo\b'],
    'Rust':              [r'\brust\b'],
    'PHP':               [r'\bphp\b'],
    'Ruby':              [r'\bruby\b'],
    'Swift':             [r'\bswift\b'],
    'Kotlin':            [r'\bkotlin\b'],
    'Scala':             [r'\bscala\b'],
    'R':                 [r'\blanguage r\b', r'\bprogramming r\b', r'\br programming\b'],
    'Bash':              [r'\bbash\b', r'\bshell scripting\b'],
    'React':             [r'\breact\.?js\b', r'\breactjs\b', r'\breact\b'],
    'Angular':           [r'\bangular\b'],
    'Vue':               [r'\bvue\.?js\b', r'\bvuejs\b'],
    'HTML':              [r'\bhtml5?\b'],
    'CSS':               [r'\bcss3?\b'],
    'Node.js':           [r'\bnode\.?js\b', r'\bnodejs\b'],
    'Express':           [r'\bexpress\.?js\b', r'\bexpress\b'],
    'Flask':             [r'\bflask\b'],
    'Django':            [r'\bdjango\b'],
    'FastAPI':           [r'\bfastapi\b'],
    'Spring Boot':       [r'\bspring boot\b'],
    'Spring':            [r'\bspring\b'],
    'Laravel':           [r'\blaravel\b'],
    'Next.js':           [r'\bnext\.?js\b', r'\bnextjs\b'],
    'Nuxt.js':           [r'\bnuxt\.?js\b'],
    'Redux':             [r'\bredux\b'],
    'Tailwind':          [r'\btailwind\b', r'\btailwindcss\b'],
    'Bootstrap':         [r'\bbootstrap\b'],
    'jQuery':            [r'\bjquery\b'],
    'GraphQL':           [r'\bgraphql\b'],
    'REST API':          [r'\brest api\b', r'\brestful\b', r'\brest\b'],
    'gRPC':              [r'\bgrpc\b'],
    'MongoDB':           [r'\bmongodb\b', r'\bmongo\b'],
    'PostgreSQL':        [r'\bpostgresql\b', r'\bpostgres\b'],
    'MySQL':             [r'\bmysql\b'],
    'SQLite':            [r'\bsqlite\b'],
    'SQL':               [r'\bsql\b'],
    'NoSQL':             [r'\bnosql\b'],
    'Redis':             [r'\bredis\b'],
    'Cassandra':         [r'\bcassandra\b'],
    'Oracle':            [r'\boracle\b'],
    'DynamoDB':          [r'\bdynamodb\b'],
    'Elasticsearch':     [r'\belasticsearch\b'],
    'Firebase':          [r'\bfirebase\b'],
    'Supabase':          [r'\bsupabase\b'],
    'Docker':            [r'\bdocker\b'],
    'Kubernetes':        [r'\bkubernetes\b', r'\bk8s\b'],
    'AWS':               [r'\baws\b', r'\bamazon web services\b'],
    'Azure':             [r'\bazure\b', r'\bmicrosoft azure\b'],
    'GCP':               [r'\bgcp\b', r'\bgoogle cloud\b'],
    'CI/CD':             [r'\bci/cd\b', r'\bcicd\b', r'\bcontinuous integration\b'],
    'Jenkins':           [r'\bjenkins\b'],
    'GitHub Actions':    [r'\bgithub actions\b'],
    'Git':               [r'\bgit\b', r'\bgithub\b', r'\bgitlab\b'],
    'Linux':             [r'\blinux\b', r'\bunix\b'],
    'Nginx':             [r'\bnginx\b'],
    'Terraform':         [r'\bterraform\b'],
    'Ansible':           [r'\bansible\b'],
    'EC2':               [r'\bec2\b'],
    'S3':                [r'\bamazon s3\b', r'\bs3 bucket\b'],
    'Lambda':            [r'\baws lambda\b', r'\blambda function\b'],
    'Machine Learning':  [r'\bmachine learning\b', r'\bml\b'],
    'Deep Learning':     [r'\bdeep learning\b', r'\bdl\b'],
    'TensorFlow':        [r'\btensorflow\b'],
    'PyTorch':           [r'\bpytorch\b'],
    'Scikit-learn':      [r'\bscikit-?learn\b', r'\bsklearn\b'],
    'NLP':               [r'\bnlp\b', r'\bnatural language processing\b'],
    'Computer Vision':   [r'\bcomputer vision\b'],
    'OpenCV':            [r'\bopencv\b'],
    'LangChain':         [r'\blangchain\b'],
    'RAG':               [r'\brag\b', r'\bretrieval augmented\b'],
    'Pandas':            [r'\bpandas\b'],
    'NumPy':             [r'\bnumpy\b'],
    'Matplotlib':        [r'\bmatplotlib\b'],
    'Seaborn':           [r'\bseaborn\b'],
    'Jupyter':           [r'\bjupyter\b'],
    'Data Analysis':     [r'\bdata analysis\b', r'\bdata analytics\b'],
    'PowerBI':           [r'\bpower ?bi\b'],
    'Tableau':           [r'\btableau\b'],
    'Excel':             [r'\bexcel\b', r'\bms excel\b'],
    'Apache Spark':      [r'\bapache spark\b', r'\bpyspark\b', r'\bspark\b'],
    'Kafka':             [r'\bkafka\b'],
    'Android':           [r'\bandroid\b'],
    'iOS':               [r'\bios\b', r'\biphone\b'],
    'React Native':      [r'\breact native\b'],
    'Flutter':           [r'\bflutter\b'],
    'Dart':              [r'\bdart\b'],
    'Figma':             [r'\bfigma\b'],
    'Adobe XD':          [r'\badobe xd\b', r'\bxd\b'],
    'UI/UX':             [r'\bui/ux\b', r'\bux design\b', r'\buser experience\b', r'\bui design\b'],
    'Wireframing':       [r'\bwireframing\b', r'\bwireframe\b'],
    'Agile':             [r'\bagile\b'],
    'Scrum':             [r'\bscrum\b'],
    'Jira':              [r'\bjira\b'],
    'Project Management':[r'\bproject management\b'],
    'Problem Solving':   [r'\bproblem.?solving\b'],
    'Teamwork':          [r'\bteamwork\b', r'\bteam collaboration\b'],
    'Communication':     [r'\bcommunication skills\b', r'\bcommunication\b'],
    'Leadership':        [r'\bleadership\b'],
    'Cybersecurity':     [r'\bcybersecurity\b', r'\bcyber security\b'],
    'Blockchain':        [r'\bblockchain\b'],
    'Solidity':          [r'\bsolidity\b'],
    'Web3':              [r'\bweb3\b'],
    'OpenAI':            [r'\bopenai\b', r'\bgpt-?[34]?\b', r'\bchatgpt\b'],
    'HuggingFace':       [r'\bhugging ?face\b'],
    'BERT':              [r'\bbert\b'],
    'Microservices':     [r'\bmicroservices?\b'],
    'JWT':               [r'\bjwt\b'],
    'OAuth':             [r'\boauth\b'],
    'WebSocket':         [r'\bwebsockets?\b', r'\bsocket\.?io\b'],
    'Jest':              [r'\bjest\b'],
    'Pytest':            [r'\bpytest\b'],
    'Selenium':          [r'\bselenium\b'],
    'Cypress':           [r'\bcypress\b'],
    'RabbitMQ':          [r'\brabbitmq\b'],
    'Celery':            [r'\bcelery\b'],
}

SKILL_CATEGORIES = {
    'Programming Languages': ['Python','JavaScript','TypeScript','Java','C++','C#','Go','Rust','PHP','Ruby','Swift','Kotlin','Scala','R','Dart','Bash'],
    'Web Technologies':      ['React','Angular','Vue','HTML','CSS','Node.js','Express','Flask','Django','FastAPI','Spring Boot','Spring','Laravel','Next.js','Nuxt.js','Redux','Tailwind','Bootstrap','jQuery','GraphQL','REST API','gRPC'],
    'Databases':             ['MongoDB','PostgreSQL','MySQL','SQLite','SQL','NoSQL','Redis','Cassandra','Oracle','DynamoDB','Elasticsearch','Firebase','Supabase'],
    'DevOps & Cloud':        ['Docker','Kubernetes','AWS','Azure','GCP','CI/CD','Jenkins','GitHub Actions','Git','Linux','Nginx','Terraform','Ansible','EC2','S3','Lambda'],
    'AI & Machine Learning': ['Machine Learning','Deep Learning','TensorFlow','PyTorch','Scikit-learn','NLP','Computer Vision','OpenCV','LangChain','RAG','OpenAI','HuggingFace','BERT'],
    'Data & Analytics':      ['Pandas','NumPy','Matplotlib','Seaborn','Jupyter','Data Analysis','PowerBI','Tableau','Excel','Apache Spark','Kafka'],
    'Mobile':                ['Android','iOS','React Native','Flutter'],
    'Design':                ['Figma','Adobe XD','UI/UX','Wireframing'],
    'Practices & Tools':     ['Agile','Scrum','Jira','Project Management','Microservices','JWT','OAuth','WebSocket','Jest','Pytest','Selenium','Cypress','RabbitMQ','Blockchain','Cybersecurity'],
    'Soft Skills':           ['Problem Solving','Teamwork','Communication','Leadership'],
}

ROLE_KEYWORDS = {
    'Frontend Developer':       {'react':3,'angular':3,'vue':3,'html':2,'css':2,'javascript':3,'typescript':2,'tailwind':2,'next.js':2,'redux':2,'bootstrap':1,'jquery':1},
    'Backend Developer':        {'python':2,'java':2,'node.js':3,'flask':3,'django':3,'fastapi':3,'spring boot':3,'postgresql':2,'mysql':2,'rest api':2,'mongodb':2,'redis':1},
    'Full Stack Developer':     {'react':2,'node.js':2,'python':2,'javascript':2,'mongodb':2,'postgresql':2,'html':1,'css':1,'express':2,'next.js':2},
    'Data Scientist':           {'python':2,'machine learning':3,'pandas':3,'numpy':3,'scikit-learn':3,'tensorflow':2,'pytorch':2,'data analysis':3,'r':2,'jupyter':2,'matplotlib':2,'seaborn':2},
    'DevOps Engineer':          {'docker':3,'kubernetes':3,'aws':2,'azure':2,'ci/cd':3,'linux':2,'terraform':3,'jenkins':2,'git':1,'ansible':2,'gcp':2},
    'Mobile Developer':         {'android':3,'ios':3,'react native':3,'flutter':3,'swift':3,'kotlin':3,'dart':2},
    'Machine Learning Engineer':{'machine learning':3,'deep learning':3,'tensorflow':3,'pytorch':3,'scikit-learn':2,'nlp':2,'computer vision':2,'python':2,'huggingface':2,'bert':2,'langchain':2},
    'Data Engineer':            {'python':2,'apache spark':3,'kafka':3,'sql':2,'aws':2,'data analysis':2,'pandas':2,'postgresql':2,'airflow':3},
    'Cloud Engineer':           {'aws':3,'azure':3,'gcp':3,'docker':2,'kubernetes':3,'terraform':3,'ec2':2,'s3':2,'lambda':2},
    'UI/UX Designer':           {'figma':3,'adobe xd':3,'ui/ux':3,'wireframing':3,'css':1,'prototyping':2,'user experience':2},
    'DevSecOps / Security':     {'cybersecurity':3,'penetration testing':2,'docker':2,'kubernetes':2,'aws':2,'ci/cd':2,'linux':2},
    'Blockchain Developer':     {'blockchain':3,'solidity':3,'web3':3,'javascript':1,'python':1},
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


def extract_text_from_file(file):
    filename = file.filename.lower()
    if filename.endswith('.pdf'):
        try:
            from PyPDF2 import PdfReader
            reader = PdfReader(io.BytesIO(file.read()))
            text = '\n'.join(page.extract_text() or '' for page in reader.pages)
            # If PyPDF2 gives blank text, that's a scanned PDF
            if not text.strip():
                return None, "PDF appears to be scanned/image-based. Please upload a text-based PDF or .txt file."
            return text, None
        except Exception as e:
            return None, f"Could not parse PDF: {str(e)}"

    elif filename.endswith('.docx'):
        try:
            from docx import Document
            doc = Document(io.BytesIO(file.read()))
            text = '\n'.join(p.text for p in doc.paragraphs)
            return text, None
        except Exception as e:
            return None, f"Could not parse DOCX: {str(e)}"

    else:
        # Treat everything else as plain text
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

    content, err = extract_text_from_file(file)
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

    # Categorize
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

