from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def editor_agent(text: str, instruction: str):
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model="openai/gpt-oss-20b",
        temperature=0.7
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert content editor."),
        ("user", """
Rewrite the given text based on instruction.

Instruction:
{instruction}

Rules:
- Keep meaning same
- Improve quality
- Return ONLY rewritten text
- No explanation

Text:
{text}
""")
    ])

    chain = prompt | llm
    response = chain.invoke({
        "text": text,
        "instruction": instruction
    })

    return response.content