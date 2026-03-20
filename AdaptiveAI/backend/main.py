from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AdaptiveAI Backend")

# ✅ CORS (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ ROOT CHECK
@app.get("/")
def root():
    return {"message": "AdaptiveAI Running 🚀"}

# ✅ UPLOAD API
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