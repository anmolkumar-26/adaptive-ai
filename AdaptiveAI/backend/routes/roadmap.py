from fastapi import APIRouter
from ai_engine.roadmap_engine import generate_roadmap

router = APIRouter(prefix="/roadmap")

@router.post("/")
def roadmap(data: dict):
    return generate_roadmap(data["missing_skills"])