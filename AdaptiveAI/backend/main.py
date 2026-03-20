from fastapi import FastAPI
from backend.routes import upload, analysis, roadmap, reasoning

app = FastAPI(title="AdaptiveAI Backend")

app.include_router(upload.router)
app.include_router(analysis.router)
app.include_router(roadmap.router)
app.include_router(reasoning.router)

@app.get("/")
def root():
    return {"message": "AdaptiveAI Running 🚀"}