from fastapi import APIRouter

router = APIRouter(prefix="/reasoning")

@router.post("/")
def reasoning(data: dict):
    output = []
    for skill in data["missing"]:
        output.append({
            "skill": skill,
            "reason": "Missing in resume but required in JD",
            "confidence": 0.9
        })
    return output