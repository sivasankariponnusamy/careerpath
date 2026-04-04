from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()

class Resume(db.Model):
    """Database model for storing resume information"""
    __tablename__ = 'resumes'
    
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(500), nullable=True)  # Path to stored file
    file_type = db.Column(db.String(50), nullable=False)  # pdf, docx, pptx, txt
    file_size = db.Column(db.Integer, nullable=False)  # Size in bytes
    
    # Extracted content
    text_content = db.Column(db.Text, nullable=True)  # Full text content
    extracted_skills = db.Column(db.Text, nullable=True)  # JSON array of skills
    categorized_skills = db.Column(db.Text, nullable=True)  # JSON object of categorized skills
    
    # Career analysis results
    suggested_roles = db.Column(db.Text, nullable=True)  # JSON array of suggested roles
    top_match_role = db.Column(db.String(200), nullable=True)
    top_match_percentage = db.Column(db.Float, nullable=True)
    
    # Metadata
    upload_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    processed = db.Column(db.Boolean, default=False, nullable=False)
    processing_error = db.Column(db.Text, nullable=True)
    
    # Optional: User information (if you have user authentication)
    user_email = db.Column(db.String(200), nullable=True)
    user_name = db.Column(db.String(200), nullable=True)
    
    def __repr__(self):
        return f'<Resume {self.id}: {self.filename}>'
    
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
            'processed': self.processed,
            'user_email': self.user_email,
            'user_name': self.user_name
        }
    
    @staticmethod
    def get_all_resumes(limit=50):
        """Get all resumes from database"""
        return Resume.query.order_by(Resume.upload_date.desc()).limit(limit).all()
    
    @staticmethod
    def get_resume_by_id(resume_id):
        """Get a specific resume by ID"""
        return Resume.query.get(resume_id)
    
    @staticmethod
    def delete_resume(resume_id):
        """Delete a resume from database"""
        resume = Resume.query.get(resume_id)
        if resume:
            db.session.delete(resume)
            db.session.commit()
            return True
        return False


class SkillGapAnalysis(db.Model):
    """Database model for storing skill gap analysis results"""
    __tablename__ = 'skill_gap_analyses'
    
    id = db.Column(db.Integer, primary_key=True)
    resume_id = db.Column(db.Integer, db.ForeignKey('resumes.id'), nullable=True)
    
    # Analysis parameters
    user_skills = db.Column(db.Text, nullable=False)  # JSON array
    target_role = db.Column(db.String(200), nullable=False)
    
    # Analysis results
    match_percentage = db.Column(db.Float, nullable=False)
    missing_skills = db.Column(db.Text, nullable=True)  # JSON array
    matching_skills = db.Column(db.Text, nullable=True)  # JSON array
    recommended_skills = db.Column(db.Text, nullable=True)  # JSON array
    
    # AI-generated insights
    ai_explanation = db.Column(db.Text, nullable=True)
    learning_roadmap = db.Column(db.Text, nullable=True)
    
    # Metadata
    analysis_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    # Relationship
    resume = db.relationship('Resume', backref=db.backref('analyses', lazy=True))
    
    def __repr__(self):
        return f'<SkillGapAnalysis {self.id}: {self.target_role}>'
    
    def to_dict(self):
        """Convert analysis object to dictionary"""
        return {
            'id': self.id,
            'resume_id': self.resume_id,
            'user_skills': json.loads(self.user_skills) if self.user_skills else [],
            'target_role': self.target_role,
            'match_percentage': self.match_percentage,
            'missing_skills': json.loads(self.missing_skills) if self.missing_skills else [],
            'matching_skills': json.loads(self.matching_skills) if self.matching_skills else [],
            'recommended_skills': json.loads(self.recommended_skills) if self.recommended_skills else [],
            'ai_explanation': self.ai_explanation,
            'learning_roadmap': self.learning_roadmap,
            'analysis_date': self.analysis_date.isoformat() if self.analysis_date else None
        }
