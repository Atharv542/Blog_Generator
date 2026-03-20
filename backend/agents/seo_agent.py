from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
from utils.json_utils import safe_parse_json

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def seo_agent(blog: str):
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model="openai/gpt-oss-20b",
        temperature=0
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an SEO expert."),
        ("user", """
Return ONLY JSON.
STRICT RULES:
- No explanation
- No markdown
- Output must start with {{ and end with }}
{{
  "title": "",
  "meta_description": "",
  "slug": "",
  "keywords": []
}}

Blog:
{blog}
""")
    ])

    chain = prompt | llm
    response = chain.invoke({"blog": blog}).content

    return safe_parse_json(response, {
        "title": "Generated Blog",
        "meta_description": "",
        "slug": "generated-blog",
        "keywords": []
    })