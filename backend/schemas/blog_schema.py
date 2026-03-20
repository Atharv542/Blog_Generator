from pydantic import BaseModel
from typing import List

class BlogSEO(BaseModel):
    title: str
    meta_description: str
    slug: str
    keywords: List[str]