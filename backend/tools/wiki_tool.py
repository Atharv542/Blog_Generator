from langchain_core.tools import StructuredTool 
from pydantic import BaseModel, Field
import wikipedia

class WikiInput(BaseModel):
    query: str = Field(..., description="Search query for Wikipedia")

def wiki_func(query: str):
    """Search Wikipedia and return a summary of the topic."""
    try:
        return wikipedia.summary(query, sentences=5)
    except Exception:
        return "No result found"

def get_wiki_tool():
    return StructuredTool.from_function(
        func=wiki_func,
        name="wiki_search",
        description="Search Wikipedia for facts about people, places, or topics",
        args_schema=WikiInput
    )