from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from app.domain.entities.ingredient import Ingredient
from app.domain.entities.step import Step

class Recipe(BaseModel):
    id: Optional[str]
    title: str
    description: str
    ingredients: list[Ingredient]
    steps: list[Step]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
