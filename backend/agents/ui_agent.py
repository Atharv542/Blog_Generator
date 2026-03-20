from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def ui_agent(structured_blog: dict):
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model="openai/gpt-oss-20b",
        temperature=0.7
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a professional frontend developer."),
        ("user", """
Create a BEAUTIFUL modern blog website using HTML + CSS.

Requirements:
- Hero section (title + subtitle)
- Sections with spacing
- Cards layout
- Smooth animations (CSS)
- Gradient background
- Responsive design
- Use Google Fonts
- Add images using Unsplash

IMPORTANT:
- Return ONLY pure HTML
- Do NOT return JSON
- Do NOT explain anything

Blog Data:
{data}
""")
    ])

    chain = prompt | llm
    html = chain.invoke({"data": structured_blog}).content

    return {
        "preview_html": html,
        "files": {}   # skip React for now (we fix later)
    }