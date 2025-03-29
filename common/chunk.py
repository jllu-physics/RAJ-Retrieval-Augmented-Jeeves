from pydantic import BaseModel
from typing import List, Optional

class Chunk(BaseModel):
    chunk_id: str
    text: str
    key: str
    embedding: List[float]
    source: Optional[str]