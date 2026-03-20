import re

SKILL_DB = ["python","machine learning","backend","api","sql","system design"]

def extract_skills(text):
    text = text.lower()
    skills = []

    for skill in SKILL_DB:
        if re.search(skill, text):
            skills.append(skill)

    return skills