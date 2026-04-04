# Vercel serverless function for Flask app
import sys
import os

# Add backend directory to Python path
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, backend_dir)

# Configure paths for Vercel serverless environment (read-only filesystem except /tmp)
os.environ['UPLOAD_FOLDER'] = '/tmp/uploads'
os.environ['DB_PATH'] = '/tmp/career_path.db'
os.makedirs('/tmp/uploads', exist_ok=True)

# Import Flask app
from main import app

# Override config for Vercel
app.config['UPLOAD_FOLDER'] = '/tmp/uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/career_path.db'

# Export for Vercel
app = app
