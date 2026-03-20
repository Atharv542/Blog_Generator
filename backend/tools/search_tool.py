from langchain_core.tools import StructuredTool 
from pydantic import BaseModel, Field
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

class SearchInput(BaseModel):
    query: str = Field(..., description="Search query")

search = DuckDuckGoSearchAPIWrapper()

def search_func(query: str):
    """Search the web for real-time information."""
    return search.run(query)

def search_tool():
   
    return StructuredTool.from_function(
        func=search_func,
        name="web_search",
        description="Search the web for latest information",
        args_schema=SearchInput
    )