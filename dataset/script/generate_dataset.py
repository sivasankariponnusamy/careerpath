import pandas as pd
import numpy as np
import random
from itertools import combinations

# Define skills categories and job roles
skills_pool = {
    'programming': ['Python', 'Java', 'JavaScript', 'C++', 'R', 'SQL', 'C#', 'Go', 'Ruby', 'PHP', 'TypeScript', 'Scala'],
    'web_dev': ['React', 'Angular', 'Vue.js', 'Node.js', 'Django', 'Flask', 'HTML', 'CSS', 'RESTful APIs', 'GraphQL'],
    'data_science': ['Machine Learning', 'Deep Learning', 'TensorFlow', 'PyTorch', 'Scikit-learn', 'Pandas', 'NumPy', 'Data Visualization', 'Statistics'],
    'cloud': ['AWS', 'Azure', 'Google Cloud', 'Docker', 'Kubernetes', 'CI/CD', 'Terraform'],
    'database': ['MongoDB', 'PostgreSQL', 'MySQL', 'Redis', 'Cassandra', 'Oracle', 'SQL Server'],
    'mobile': ['Android', 'iOS', 'React Native', 'Flutter', 'Swift', 'Kotlin'],
    'devops': ['Jenkins', 'Git', 'Linux', 'Docker', 'Kubernetes', 'Ansible', 'Monitoring'],
    'analytics': ['Tableau', 'Power BI', 'Excel', 'Data Analysis', 'Business Intelligence', 'A/B Testing'],
    'security': ['Cybersecurity', 'Penetration Testing', 'Network Security', 'Cryptography', 'OWASP'],
    'soft_skills': ['Communication', 'Leadership', 'Problem Solving', 'Teamwork', 'Agile', 'Project Management']
}

# Define job role skill profiles
role_profiles = {
    'Data Scientist': {
        'required': ['Python', 'Machine Learning', 'Statistics', 'Pandas', 'NumPy'],
        'preferred': ['TensorFlow', 'PyTorch', 'Deep Learning', 'SQL', 'Data Visualization', 'R'],
        'bonus': ['AWS', 'Docker', 'Scikit-learn', 'Spark']
    },
    'Software Engineer': {
        'required': ['Python', 'Java', 'Git', 'Problem Solving'],
        'preferred': ['SQL', 'RESTful APIs', 'JavaScript', 'Docker', 'CI/CD'],
        'bonus': ['AWS', 'Kubernetes', 'Agile', 'TypeScript']
    },
    'Frontend Developer': {
        'required': ['JavaScript', 'HTML', 'CSS', 'React'],
        'preferred': ['TypeScript', 'Vue.js', 'Angular', 'RESTful APIs'],
        'bonus': ['Node.js', 'Git', 'Agile', 'GraphQL']
    },
    'Backend Developer': {
        'required': ['Python', 'Java', 'SQL', 'RESTful APIs'],
        'preferred': ['Node.js', 'PostgreSQL', 'MongoDB', 'Docker'],
        'bonus': ['Kubernetes', 'Redis', 'AWS', 'CI/CD']
    },
    'Full Stack Developer': {
        'required': ['JavaScript', 'Python', 'SQL', 'React', 'Node.js'],
        'preferred': ['HTML', 'CSS', 'RESTful APIs', 'Git', 'MongoDB'],
        'bonus': ['Docker', 'AWS', 'TypeScript', 'PostgreSQL']
    },
    'DevOps Engineer': {
        'required': ['Docker', 'Kubernetes', 'Linux', 'CI/CD', 'Git'],
        'preferred': ['AWS', 'Terraform', 'Jenkins', 'Ansible', 'Python'],
        'bonus': ['Monitoring', 'Azure', 'Google Cloud']
    },
    'Machine Learning Engineer': {
        'required': ['Python', 'Machine Learning', 'TensorFlow', 'Deep Learning'],
        'preferred': ['PyTorch', 'Docker', 'AWS', 'Scikit-learn', 'NumPy'],
        'bonus': ['Kubernetes', 'MLOps', 'Scala', 'Spark']
    },
    'Data Analyst': {
        'required': ['SQL', 'Excel', 'Data Analysis', 'Statistics'],
        'preferred': ['Python', 'Tableau', 'Power BI', 'Pandas'],
        'bonus': ['R', 'Business Intelligence', 'A/B Testing']
    },
    'Mobile Developer': {
        'required': ['Android', 'Kotlin', 'iOS', 'Swift'],
        'preferred': ['React Native', 'Flutter', 'Git', 'RESTful APIs'],
        'bonus': ['JavaScript', 'Firebase', 'CI/CD']
    },
    'Cloud Architect': {
        'required': ['AWS', 'Azure', 'Cloud Architecture', 'Terraform'],
        'preferred': ['Kubernetes', 'Docker', 'Microservices', 'CI/CD'],
        'bonus': ['Google Cloud', 'Security', 'Python', 'Monitoring']
    },
    'Security Engineer': {
        'required': ['Cybersecurity', 'Network Security', 'Penetration Testing'],
        'preferred': ['OWASP', 'Cryptography', 'Linux', 'Python'],
        'bonus': ['AWS', 'Docker', 'Compliance', 'Incident Response']
    },
    'Product Manager': {
        'required': ['Project Management', 'Communication', 'Leadership', 'Agile'],
        'preferred': ['Data Analysis', 'SQL', 'Business Intelligence'],
        'bonus': ['Python', 'A/B Testing', 'Tableau', 'Excel']
    }
}

def generate_skill_set(role_profile, skill_coverage=0.7):
    """Generate a realistic skill set for a given role profile"""
    skills = []
    
    # Always include most required skills
    num_required = int(len(role_profile['required']) * random.uniform(0.8, 1.0))
    skills.extend(random.sample(role_profile['required'], num_required))
    
    # Add some preferred skills
    num_preferred = int(len(role_profile['preferred']) * random.uniform(0.4, 0.7))
    skills.extend(random.sample(role_profile['preferred'], num_preferred))
    
    # Occasionally add bonus skills
    if random.random() > 0.5:
        num_bonus = int(len(role_profile['bonus']) * random.uniform(0.2, 0.5))
        skills.extend(random.sample(role_profile['bonus'], num_bonus))
    
    # Add some random noise (skills from other domains)
    all_skills = [skill for category in skills_pool.values() for skill in category]
    noise_skills = random.sample([s for s in all_skills if s not in skills], 
                                 random.randint(0, 3))
    skills.extend(noise_skills)
    
    return list(set(skills))  # Remove duplicates

def create_dataset(num_samples=1000):
    """Create a dataset with skills as features and job roles as labels"""
    data = []
    
    roles = list(role_profiles.keys())
    
    for _ in range(num_samples):
        # Select a role
        role = random.choice(roles)
        
        # Generate skills for this role
        skills = generate_skill_set(role_profiles[role])
        
        data.append({
            'skills': ', '.join(sorted(skills)),
            'num_skills': len(skills),
            'role': role
        })
    
    return pd.DataFrame(data)

def create_one_hot_encoded_dataset(num_samples=1000):
    """Create a dataset with one-hot encoded skills"""
    # Get all unique skills
    all_skills = list(set([skill for category in skills_pool.values() for skill in category]))
    all_skills.sort()
    
    data = []
    roles_list = []
    
    roles = list(role_profiles.keys())
    
    for _ in range(num_samples):
        # Select a role
        role = random.choice(roles)
        
        # Generate skills for this role
        skills = generate_skill_set(role_profiles[role])
        
        # Create one-hot encoded row
        row = {skill: 1 if skill in skills else 0 for skill in all_skills}
        data.append(row)
        roles_list.append(role)
    
    df = pd.DataFrame(data)
    df['role'] = roles_list
    
    return df

if __name__ == "__main__":
    # Set random seed for reproducibility
    random.seed(42)
    np.random.seed(42)
    
    print("Generating job recommendation dataset...")
    print(f"Total number of unique skills: {sum(len(v) for v in skills_pool.values())}")
    print(f"Number of job roles: {len(role_profiles)}")
    print("\nJob roles:", list(role_profiles.keys()))
    
    # Generate dataset with skills as comma-separated strings
    df_text = create_dataset(num_samples=2000)
    print(f"\n✓ Generated {len(df_text)} samples with text-based skills")
    print(f"Sample:\n{df_text.head()}")
    df_text.to_csv('job_dataset_text.csv', index=False)
    print("\n✓ Saved to 'job_dataset_text.csv'")
    
    # Generate dataset with one-hot encoded skills
    df_encoded = create_one_hot_encoded_dataset(num_samples=2000)
    print(f"\n✓ Generated {len(df_encoded)} samples with one-hot encoded skills")
    print(f"Dataset shape: {df_encoded.shape}")
    print(f"Sample:\n{df_encoded.head()}")
    df_encoded.to_csv('job_dataset_encoded.csv', index=False)
    print("\n✓ Saved to 'job_dataset_encoded.csv'")
    
    # Display role distribution
    print("\n" + "="*50)
    print("Role Distribution:")
    print("="*50)
    print(df_text['role'].value_counts())
    
    print("\n" + "="*50)
    print("Dataset generation complete!")
    print("="*50)
    print("\nGenerated files:")
    print("1. job_dataset_text.csv - Skills as comma-separated text")
    print("2. job_dataset_encoded.csv - Skills as one-hot encoded features (ready for Random Forest)")
