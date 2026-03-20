from fastapi import APIRouter, UploadFile, File

router = APIRouter(prefix="/upload")

@router.post("/resume")
async def upload_resume(file: UploadFile = File(...)):
    content = await file.read()
    return {"message": "Resume uploaded", "size": len(content)}