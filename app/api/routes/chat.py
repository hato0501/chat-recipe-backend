from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

from app.core.dependency_injection import chat_repository_dependency
from app.domain.entities.message import Message
from app.domain.interfaces.chat_repository import IChatRepository

router = APIRouter()

class ChatInputs(BaseModel):
    text: str
    text_history: str

@router.post("/chatgpt", response_model=Message)
async def get_chatgpt_response(inputs: ChatInputs, chat_repository: IChatRepository = chat_repository_dependency):
    try:
        # Retrieve all recipes from the repository
        message = await chat_repository.get_chatgpt_response(text=inputs.text)
        return message
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")