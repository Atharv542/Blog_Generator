from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
from utils.json_utils import safe_parse_json

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def structure_agent(blog: str):
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model="openai/gpt-oss-20b",
        temperature=0
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "Convert blog into structured JSON."),
        ("user", """
Return ONLY valid JSON.

STRICT RULES:
- No explanation
- No markdown
- Output must start with {{ and end with }}

Format:
{{
  "title": "",
  "sections": [
    {{
      "heading": "",
      "content": ""
    }}
  ],
  "image_prompts": []
}}

Blog:
{blog}
""")
    ])

    chain = prompt | llm
    response = chain.invoke({"blog": blog}).content

    return safe_parse_json(response, {
        "title": "Generated Blog",
        "sections": [{"heading": "Content", "content": blog}],
        "image_prompts": []
    })