from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import re
import io
import json
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "OPTIONS"], "allow_headers": ["Content-Type"]}})

# Database Configuration
# Use environment variable for database path in production, or local SQLite in development
db_path = os.environ.get('DATABASE_URL', 'sqlite:///career_path.db')
if db_path.startswith('postgres://'):
    db_path = db_path.replace('postgres://', 'postgresql://', 1)
    
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class Resume(db.Model):
    """Database model for storing resume information"""
    __tablename__ = 'resumes'
    
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    file_type = db.Column(db.String(50), nullable=False)
    file_size = db.Column(db.Integer, nullable=False)
    text_content = db.Column(db.Text, nullable=True)
    extracted_skills = db.Column(db.Text, nullable=True)
    categorized_skills = db.Column(db.Text, nullable=True)
    suggested_roles = db.Column(db.Text, nullable=True)
    top_match_role = db.Column(db.String(200), nullable=True)
    top_match_percentage = db.Column(db.Float, nullable=True)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    processed = db.Column(db.Boolean, default=False, nullable=False)
    
    def to_dict(self):
        """Convert resume object to dictionary"""
        return {
            'id': self.id,
            'filename': self.filename,
            'file_type': self.file_type,
            'file_size': self.file_size,
            'extracted_skills': json.loads(self.extracted_skills) if self.extracted_skills else [],
            'categorized_skills': json.loads(self.categorized_skills) if self.categorized_skills else {},
            'suggested_roles': json.loads(self.suggested_roles) if self.suggested_roles else [],
            'top_match_role': self.top_match_role,
            'top_match_percentage': self.top_match_percentage,
            'upload_date': self.upload_date.isoformat() if self.upload_date else None,
            'processed': self.processed
        }

# Initialize database
with app.app_context():
    try:
        db.create_all()
        print("✓ Database initialized successfully!")
    except Exception as e:
        print(f"⚠ Database initialization warning: {e}")

def predict_career_roles(user_skills):
    """Rule-based career role prediction"""
    skills_lower = [s.lower() for s in user_skills]
    role_scores = {
        'Frontend Developer': sum(1 for s in ['react', 'angular', 'vue', 'html', 'css', 'javascript', 'typescript', 'tailwind', 'next.js'] if s in skills_lower),
        'Backend Developer': sum(1 for s in ['python', 'java', 'node.js', 'flask', 'django', 'fastapi', 'spring', 'postgresql', 'mysql', 'rest api'] if s in skills_lower),
        'Full Stack Developer': sum(1 for s in ['react', 'node.js', 'python', 'javascript', 'mongodb', 'postgresql', 'html', 'css'] if s in skills_lower),
        'Data Scientist': sum(1 for s in ['python', 'machine learning', 'pandas', 'numpy', 'tensorflow', 'pytorch', 'data analysis'] if s in skills_lower),
        'DevOps Engineer': sum(1 for s in ['docker', 'kubernetes', 'aws', 'azure', 'ci/cd', 'linux', 'terraform', 'jenkins', 'git'] if s in skills_lower),
        'Mobile Developer': sum(1 for s in ['android', 'ios', 'react native', 'flutter', 'swift', 'kotlin', 'dart'] if s in skills_lower),
        'UI/UX Designer': sum(1 for s in ['figma', 'adobe xd', 'sketch', 'ui/ux', 'wireframing', 'prototyping'] if s in skills_lower),
    }
    
    sorted_roles = sorted(role_scores.items(), key=lambda x: x[1], reverse=True)
    predictions = []
    
    for role, score in sorted_roles[:5]:
        if score > 0:
            confidence = min(score * 15, 95)
            predictions.append({
                'role': role,
                'match_percentage': round(confidence, 2),
                'confidence': 'High' if confidence > 70 else 'Medium' if confidence > 50 else 'Low'
            })
    
    return predictions if predictions else [{'role': 'Software Developer', 'match_percentage': 50, 'confidence': 'Low'}]

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


def read_file_content(file):
    filename = file.filename.lower()
    if filename.endswith('.pdf'):
        try:
            from PyPDF2 import PdfReader
            reader = PdfReader(io.BytesIO(file.read()))
            text = '\n'.join(page.extract_text() or '' for page in reader.pages)
            return text, None if text.strip() else (None, "PDF appears empty")
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

    original_filename = file.filename
    file_type = original_filename.split('.')[-1] if '.' in original_filename else 'unknown'
    
    file.seek(0, os.SEEK_END)
    file_size = file.tell()
    file.seek(0)

    content, err = read_file_content(file)
    if err:
        return jsonify({'error': err}), 400
    if not content or not content.strip():
        return jsonify({'error': 'No text content found'}), 400

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

    suggested_roles = predict_career_roles(found_skills)
    top_match = None
    if suggested_roles:
        top = suggested_roles[0]
        top_match = {
            'role': top['role'],
            'match_percentage': top['match_percentage'],
            'message': f"Based on your resume, you're best suited for {top['role']} role with {top['match_percentage']}% match!"
        }

    # Save to database
    resume_id = None
    saved_to_db = False
    try:
        resume = Resume(
            filename=original_filename,
            file_type=file_type,
            file_size=file_size,
            text_content=content[:10000],
            extracted_skills=json.dumps(found_skills),
            categorized_skills=json.dumps(categorized),
            suggested_roles=json.dumps(suggested_roles),
            top_match_role=top_match['role'] if top_match else None,
            top_match_percentage=top_match['match_percentage'] if top_match else None,
            processed=True,
            upload_date=datetime.utcnow()
        )
        db.session.add(resume)
        db.session.commit()
        resume_id = resume.id
        saved_to_db = True
    except Exception as e:
        print(f"⚠ Database error: {str(e)}")
        try:
            db.session.rollback()
        except:
            pass

    return jsonify({
        'resume_id': resume_id,
        'skills': found_skills,
        'categorized_skills': categorized,
        'suggested_roles': suggested_roles,
        'top_match': top_match,
        'total_skills': len(found_skills),
        'saved_to_database': saved_to_db
    })


@app.route('/api/skills', methods=['GET'])
def get_skills():
    return jsonify({'skills': list(SKILL_ALIASES.keys())})


@app.route('/api/resumes', methods=['GET'])
def get_resumes():
    try:
        resumes = Resume.query.order_by(Resume.upload_date.desc()).limit(50).all()
        return jsonify({'resumes': [resume.to_dict() for resume in resumes], 'count': len(resumes)})
    except Exception as e:
        return jsonify({'error': str(e), 'resumes': [], 'count': 0}), 500

@app.route('/api/resumes/<int:resume_id>', methods=['GET'])
def get_resume(resume_id):
    try:
        resume = Resume.query.get(resume_id)
        return jsonify({'resume': resume.to_dict()}) if resume else (jsonify({'error': 'Not found'}), 404)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
