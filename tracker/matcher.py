import re
from pypdf import PdfReader

SKILLS = [
    'python', 'java', 'c++', 'javascript', 'typescript', 'html', 'css', 'bootstrap',
    'django', 'flask', 'react', 'node.js', 'sql', 'mysql', 'postgresql', 'sqlite',
    'mongodb', 'git', 'github', 'rest api', 'docker', 'linux', 'aws', 'excel',
    'power bi', 'tableau', 'pandas', 'numpy', 'machine learning', 'data analysis',
    'oop', 'dbms', 'data structures', 'algorithms', 'communication',
    'problem solving', 'teamwork',
]


def extract_text(pdf_file):
    reader = PdfReader(pdf_file)
    pages = [page.extract_text() or '' for page in reader.pages]
    return '\n'.join(pages)


def find_skills(text):
    text = text.lower()
    found = set()
    for skill in SKILLS:
        pattern = r'(?<![a-z0-9+#])' + re.escape(skill) + r'(?![a-z0-9+#])'
        if re.search(pattern, text):
            found.add(skill)
    return found


def match_resume(resume_text, job_text):
    resume_skills = find_skills(resume_text)
    job_skills = find_skills(job_text)
    matched = sorted(job_skills & resume_skills)
    missing = sorted(job_skills - resume_skills)
    percent = round(len(matched) / len(job_skills) * 100) if job_skills else 0
    return percent, matched, missing, len(job_skills)