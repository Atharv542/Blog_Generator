from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
from tools.wiki_tool import get_wiki_tool
from tools.arxiv_tool import arxiv_tool
from tools.search_tool import search_tool
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_research_agent():
    llm= ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model="openai/gpt-oss-20b",
        temperature=0
    )

    tools=[get_wiki_tool(),arxiv_tool(),search_tool()]

    system_prompt = """
You are a research expert AI.

STRICT RULES:
- ALWAYS use tools for factual topics
- Use Wikipedia tool for people (Virat Kohli, MS Dhoni)
- Use search tool for general topics (cricket, comparisons)
- Combine results from multiple tools

TASK:
1. Understand the topic clearly
2. If multiple names → compare them
3. Use tools to fetch real information
4. Return detailed bullet points

OUTPUT:
- Well-structured bullet points
- Include:
  - Overview
  - Key facts
  - Achievements
  - Comparison (if multiple entities)

DO NOT:
- Return empty or short answers
- Skip tool usage
    You are a research expert AI.

    - Use tools when needed
    - Gather accurate and factual information
    - Return structured bullet points
    - Do NOT hallucinate
    
    You are a research expert AI.

Understand the user topic clearly.

If topic contains:
- People → include biography, achievements
- Sports → include history, players, impact
- Multiple names → compare them

Return:
- Clear bullet points
- Well structured
- Enough content to write a full blog

DO NOT return empty or short answers."""

    agent= create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_prompt
    )

    return agent