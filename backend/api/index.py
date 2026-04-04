# Vercel serverless function for Flask app
import sys
import os

# Add backend directory to Python path
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, backend_dir)

# Import Flask app
from main import app

# Export for Vercel
app = app
