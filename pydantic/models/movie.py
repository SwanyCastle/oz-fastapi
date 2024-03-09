from pydantic import BaseModel
from uuid import UUID
from typing import List, Optional

class Movie(BaseModel):
    id: UUID
    name: str
    plot: Optional[str] = None
    genres: List[str] = None
    casts: List[str] = None

class CreateMovie(BaseModel):
    name: str
    plot: Optional[str] = None
    genres: List[str] = None
    casts: List[str] = None

class SearchMovie(BaseModel):
    results: List[Movie]
