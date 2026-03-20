from fastapi import APIRouter
from backend.schemas import TextInput
from ai_engine.skill_extractor import extract_skills
from ai_engine.matcher import skill_gap

router = APIRouter(prefix="/analysis")

@router.post("/extract-skills")
def extract(data: TextInput):
    skills = extract_skills(data.text)
    return {"skills": skills}

@router.post("/skill-gap")
def gap(data: dict):
    resume_skills = extract_skills(data["resume"])
    jd_skills = extract_skills(data["jd"])

    result = skill_gap(resume_skills, jd_skills)
    return result