def extract_skills(text):
    skills = [
        "python", "sql", "machine learning", "deep learning",
        "fastapi", "docker", "aws", "llm", "nlp"
    ]
    found = [skill for skill in skills if skill in text.lower()]
    return set(found)

def find_missing_skills(resume, job):
    resume_skills = extract_skills(resume)
    job_skills = extract_skills(job)
    return list(job_skills - resume_skills)
