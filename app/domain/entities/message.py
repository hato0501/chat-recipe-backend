from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Message(BaseModel):
    id: Optional[str]
    sender: str
    text: str
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True
