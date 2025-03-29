from pydantic import BaseModel
from typing import List, Optional

class Query(BaseModel):
    text: str
    embedding: List[float]