from fastapi import FastAPI
from matcher import calculate_match_score, get_ai_suggestions
from utils import find_missing_skills

app = FastAPI()

@app.post("/match")
def match_resume(resume: str, job: str):
    score = calculate_match_score(resume, job)
    missing_skills = find_missing_skills(resume, job)
    suggestions = get_ai_suggestions(resume, job)

    return {
        "match_score": score,
        "missing_skills": missing_skills,
        "suggestions": suggestions
    }
