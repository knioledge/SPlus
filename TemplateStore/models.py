from pydantic import BaseModel, Field
from typing import Union, List, Dict, Any

class Template(BaseModel):
    id: str
    name: str
    type: str
    variables: List[str]
    content: Dict[str, Any]  # <--- updated
    tags: List[str] = []
    difficulty: str
