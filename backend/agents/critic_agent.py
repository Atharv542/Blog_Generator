from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def critic_agent(blog:str):
    llm= ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model="openai/gpt-oss-20b",
    temperature=0.3
)

    prompt=ChatPromptTemplate.from_messages([
    ("system","You are a strict editor"),
    ("user","""
          Improve the following blog:

        Focus on:
        - Grammar
        - Clarity
        - Depth
        - Flow

        Blog:
        {blog}
""")
])

    chain= prompt|llm
    response= chain.invoke({"blog":blog})
    return response
