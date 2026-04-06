from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import re
import io
import json
import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

app = Flask(__name__)
CORS(app, origins="*")

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
    
    # Extracted content
    text_content = db.Column(db.Text, nullable=True)
    extracted_skills = db.Column(db.Text, nullable=True)
    categorized_skills = db.Column(db.Text, nullable=True)
    
    # Career analysis results
    suggested_roles = db.Column(db.Text, nullable=True)
    top_match_role = db.Column(db.String(200), nullable=True)
    top_match_percentage = db.Column(db.Float, nullable=True)
    
    # Metadata
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

# Initialize database tables
with app.app_context():
    try:
        db.create_all()
        print("✓ Database initialized successfully!")
    except Exception as e:
        print(f"⚠ Database initialization warning: {e}")

# Load datasets for ML model
DATASET_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'dataset')
df_encoded = pd.DataFrame()
all_skills = []

try:
    df_encoded = pd.read_csv(os.path.join(DATASET_PATH, 'job_dataset_encoded.csv'))
    all_skills = [col for col in df_encoded.columns if col != 'role']
    print(f"✓ Dataset loaded with {len(all_skills)} skills")
except Exception as e:
    print(f"⚠ Dataset not found, using built-in skill list: {e}")
    # Comprehensive built-in skill list for serverless deployment
    all_skills = [
        'Python', 'JavaScript', 'TypeScript', 'Java', 'C++', 'C#', 'Go', 'Rust', 'PHP', 'Ruby',
        'Swift', 'Kotlin', 'Scala', 'R', 'MATLAB', 'Perl', 'Bash', 'Shell',
        'React', 'Angular', 'Vue', 'HTML', 'CSS', 'Node.js', 'Express', 'Flask', 'Django',
        'FastAPI', 'Spring', 'Spring Boot', 'Laravel', 'Rails', 'ASP.NET', 'Next.js', 'Nuxt.js',
        'Tailwind', 'Bootstrap', 'jQuery', 'Redux', 'GraphQL', 'REST API', 'gRPC',
        'MongoDB', 'PostgreSQL', 'MySQL', 'SQLite', 'SQL', 'NoSQL', 'Redis', 'Cassandra',
        'Oracle', 'DynamoDB', 'Elasticsearch', 'Firebase', 'Supabase',
        'Docker', 'Kubernetes', 'AWS', 'Azure', 'GCP', 'CI/CD', 'Jenkins', 'GitHub Actions',
        'Git', 'Linux', 'Nginx', 'Apache', 'Terraform', 'Ansible', 'Prometheus', 'Grafana',
        'EC2', 'S3', 'Lambda', 'CloudFormation', 'EKS', 'ECS', 'RDS',
        'Machine Learning', 'Deep Learning', 'TensorFlow', 'PyTorch', 'Scikit-learn',
        'NLP', 'Computer Vision', 'OpenCV', 'LangChain', 'RAG', 'LLM',
        'Pandas', 'NumPy', 'Matplotlib', 'Seaborn', 'Jupyter', 'Data Analysis',
        'PowerBI', 'Tableau', 'Excel', 'Data Engineering', 'Apache Spark', 'Kafka',
        'Android', 'iOS', 'React Native', 'Flutter', 'Dart', 'Xcode',
        'Figma', 'Adobe XD', 'Sketch', 'UI/UX', 'Wireframing', 'Prototyping',
        'Agile', 'Scrum', 'Jira', 'Project Management', 'Leadership',
        'Problem Solving', 'Teamwork', 'Communication', 'Critical Thinking',
        'Cybersecurity', 'Network Security', 'Penetration Testing', 'OWASP',
        'Blockchain', 'Solidity', 'Web3', 'Smart Contracts',
        'OpenAI', 'HuggingFace', 'BERT', 'GPT', 'Stable Diffusion',
        'RabbitMQ', 'Celery', 'WebSocket', 'OAuth', 'JWT', 'Microservices',
        'Unit Testing', 'Jest', 'Pytest', 'Selenium', 'Cypress',
    ]

class CareerRecommendationSystem:
    """AI-Driven Career Recommendation System using Random Forest Classifier"""
    def __init__(self):
        self.rf_model = None
        self.label_encoder = LabelEncoder()
        self.train_model()
    
    def train_model(self):
        """Train Random Forest Classifier on the dataset"""
        if df_encoded.empty:
            print("⚠ No dataset available, using rule-based predictions")
            return
        
        print("Training Random Forest Classifier...")
        
        # Prepare features and labels
        X = df_encoded[all_skills].values
        y = df_encoded['role'].values
        
        # Encode labels
        y_encoded = self.label_encoder.fit_transform(y)
        
        # Split data for training
        X_train, X_test, y_train, y_test = train_test_split(
            X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
        )
        
        # Train Random Forest Classifier
        self.rf_model = RandomForestClassifier(
            n_estimators=100,
            max_depth=20,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=42,
            n_jobs=-1
        )
        
        self.rf_model.fit(X_train, y_train)
        
        # Calculate accuracy
        train_accuracy = self.rf_model.score(X_train, y_train)
        test_accuracy = self.rf_model.score(X_test, y_test)
        
        print(f"✓ Model trained successfully!")
        print(f"  Training Accuracy: {train_accuracy * 100:.2f}%")
        print(f"  Testing Accuracy: {test_accuracy * 100:.2f}%")
    
    def predict_career(self, user_skills):
        """Predict career role using Random Forest Classifier"""
        if self.rf_model is None or not all_skills:
            # Fallback: rule-based role detection when no ML model
            return self._rule_based_predict(user_skills)

        # Create user skill vector
        user_vector = np.zeros(len(all_skills))
        for skill in user_skills:
            if skill in all_skills:
                idx = all_skills.index(skill)
                user_vector[idx] = 1
        
        # Reshape for prediction
        user_vector = user_vector.reshape(1, -1)
        
        # Get prediction probabilities
        probabilities = self.rf_model.predict_proba(user_vector)[0]
        
        # Get top predictions
        top_indices = np.argsort(probabilities)[::-1][:5]
        predictions = []
        
        for idx in top_indices:
            role = self.label_encoder.inverse_transform([idx])[0]
            confidence = probabilities[idx] * 100
            predictions.append({
                'role': role,
                'match_percentage': round(confidence, 2),
                'confidence': 'High' if confidence > 70 else 'Medium' if confidence > 50 else 'Low'
            })
        
        return predictions

    def _rule_based_predict(self, user_skills):
        """Rule-based role prediction when ML model is not available"""
        skills_lower = [s.lower() for s in user_skills]
        role_scores = {
            'Frontend Developer': sum(1 for s in ['react', 'angular', 'vue', 'html', 'css', 'javascript', 'typescript', 'tailwind', 'next.js'] if s in skills_lower),
            'Backend Developer': sum(1 for s in ['python', 'java', 'node.js', 'flask', 'django', 'fastapi', 'spring', 'postgresql', 'mysql', 'rest api'] if s in skills_lower),
            'Full Stack Developer': sum(1 for s in ['react', 'node.js', 'python', 'javascript', 'mongodb', 'postgresql', 'html', 'css'] if s in skills_lower),
            'Data Scientist': sum(1 for s in ['python', 'machine learning', 'pandas', 'numpy', 'scikit-learn', 'tensorflow', 'pytorch', 'data analysis', 'r'] if s in skills_lower),
            'DevOps Engineer': sum(1 for s in ['docker', 'kubernetes', 'aws', 'azure', 'ci/cd', 'linux', 'terraform', 'jenkins', 'git'] if s in skills_lower),
            'Mobile Developer': sum(1 for s in ['android', 'ios', 'react native', 'flutter', 'swift', 'kotlin', 'dart'] if s in skills_lower),
            'Machine Learning Engineer': sum(1 for s in ['machine learning', 'deep learning', 'tensorflow', 'pytorch', 'scikit-learn', 'nlp', 'computer vision', 'python'] if s in skills_lower),
            'Data Engineer': sum(1 for s in ['python', 'apache spark', 'kafka', 'sql', 'aws', 'data engineering', 'pandas'] if s in skills_lower),
            'Cloud Engineer': sum(1 for s in ['aws', 'azure', 'gcp', 'docker', 'kubernetes', 'terraform', 'ec2', 's3'] if s in skills_lower),
            'UI/UX Designer': sum(1 for s in ['figma', 'adobe xd', 'sketch', 'ui/ux', 'wireframing', 'prototyping', 'css'] if s in skills_lower),
        }
        sorted_roles = sorted(role_scores.items(), key=lambda x: x[1], reverse=True)
        predictions = []
        for role, score in sorted_roles[:5]:
            if score > 0:
                confidence = min(score * 15, 95)
                predictions.append({'role': role, 'match_percentage': confidence, 'confidence': 'High' if confidence > 70 else 'Medium' if confidence > 50 else 'Low'})
        return predictions if predictions else [{'role': 'Software Developer', 'match_percentage': 50, 'confidence': 'Low'}]
    
    def recommend_roles(self, user_skills, top_n=5):
        """Recommend top matching roles using ML model predictions"""
        return self.predict_career(user_skills)[:top_n]

# Initialize ML model
career_system = CareerRecommendationSystem()

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

# Old keyword-based role detection removed - now using ML model (CareerRecommendationSystem)


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

    original_filename = file.filename
    file_type = original_filename.split('.')[-1] if '.' in original_filename else 'unknown'
    
    # Get file size
    file.seek(0, os.SEEK_END)
    file_size = file.tell()
    file.seek(0)

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

    # Use ML model for role recommendations (same as local backend)
    suggested_roles = career_system.recommend_roles(found_skills, top_n=3)
    top_match = None
    if suggested_roles:
        top = suggested_roles[0]
        top_match = {
            'role': top['role'],
            'match_percentage': top['match_percentage'],
            'message': f"Based on your resume, you're best suited for {top['role']} role with {top['match_percentage']}% match!" if top else "Upload your resume to get role suggestions"
        }

    # Save resume to database
    resume_id = None
    saved_to_db = False
    try:
        resume = Resume(
            filename=original_filename,
            file_type=file_type,
            file_size=file_size,
            text_content=content[:10000],  # Store first 10000 chars
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
        print(f"✓ Resume saved to database with ID: {resume_id}")
        
    except Exception as e:
        print(f"⚠ Error saving resume to database: {str(e)}")
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
    """Get all stored resumes from database"""
    try:
        resumes = Resume.query.order_by(Resume.upload_date.desc()).limit(50).all()
        return jsonify({
            'resumes': [resume.to_dict() for resume in resumes],
            'count': len(resumes)
        })
    except Exception as e:
        return jsonify({'error': str(e), 'resumes': [], 'count': 0}), 500


@app.route('/api/resumes/<int:resume_id>', methods=['GET'])
def get_resume(resume_id):
    """Get a specific resume by ID"""
    try:
        resume = Resume.query.get(resume_id)
        if resume:
            return jsonify({'resume': resume.to_dict()})
        else:
            return jsonify({'error': 'Resume not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
