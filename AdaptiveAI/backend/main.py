from fastapi import FastAPI
from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    return {
        "skills": ["Python", "ML", "System Design"],
        "role": "Backend Developer",
        "roadmap": [
            "Week 1: Backend Basics",
            "Week 2: APIs",
            "Week 3: Databases",
            "Week 4: System Design"
        ]
    }
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import upload, analysis, roadmap, reasoning

app = FastAPI(title="AdaptiveAI Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router)
app.include_router(analysis.router)
app.include_router(roadmap.router)
app.include_router(reasoning.router)

@app.get("/")
def root():
    return {"message": "AdaptiveAI Running 🚀"}