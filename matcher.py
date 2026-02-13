import numpy as np
from openai import OpenAI

client = OpenAI()

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

def calculate_match_score(resume_text, job_text):
    resume_emb = get_embedding(resume_text)
    job_emb = get_embedding(job_text)

    similarity = cosine_similarity(resume_emb, job_emb)
    return round(similarity * 100, 2)

def get_ai_suggestions(resume, job):
    prompt = f"""
    Resume:
    {resume}

    Job Description:
    {job}

    Suggest how the resume can be improved to better match the job.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content
