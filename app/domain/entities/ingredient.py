from pydantic import BaseModel

class Ingredient(BaseModel):
    id: str
    name: str
    amount: str