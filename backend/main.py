from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator.pipeline import generate_blog_pipeline
from fastapi.middleware.cors import CORSMiddleware
from agents.editor_agent import editor_agent
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class BlogRequest(BaseModel):
    topic: str

class EditRequest(BaseModel):
    text: str
    instruction: str

@app.get("/")
def home():
    return {"message": "AI Blog Generator Running"}

@app.post("/generate")
def generate(req: BlogRequest):
    try:
        result = generate_blog_pipeline(req.topic)
        return result
    except Exception as e:
        return {"error": str(e)}



@app.post("/edit")
def edit_text(req: EditRequest):
    try:
        result = editor_agent(req.text, req.instruction)
        return {"edited_text": result}
    except Exception as e:
        return {"error": str(e)}
