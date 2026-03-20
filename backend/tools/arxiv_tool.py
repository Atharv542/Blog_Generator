from langchain_core.tools import StructuredTool 
from pydantic import BaseModel, Field
from langchain_community.utilities import ArxivAPIWrapper

class ArxivInput(BaseModel):
    query: str = Field(..., description="Search query for research papers")

arxiv = ArxivAPIWrapper(
    top_k_results=2,
    doc_content_chars_max=1000
)

def arxiv_func(query: str):
    """Search research papers from Arxiv."""
    return arxiv.run(query)

def arxiv_tool():

    return StructuredTool.from_function(
        func=arxiv_func,
        name="arxiv_search",
        description="Search research papers from Arxiv",
        args_schema=ArxivInput
    )