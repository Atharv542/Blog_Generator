from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def writer_agent(research_data:str):
    llm= ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model="openai/gpt-oss-20b",
        temperature=0.7
    )

    prompt=ChatPromptTemplate.from_messages([
        ("system", "You are a professional blog writer."),
        ("user","""
          Convert the following research into a blog.

        Requirements:
        - Engaging introduction
        - Clear headings
        - Easy to understand

        Research:
        {research}
""")
    ])

    chain= prompt|llm
    response= chain.invoke({"research":research_data})
    return response.content