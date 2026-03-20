from fastapi import FastAPI
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