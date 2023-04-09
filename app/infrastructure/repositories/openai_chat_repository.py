from app.domain.entities.message import Message
from app.domain.interfaces.chat_repository import IChatRepository
from app.core.config import settings
from fastapi import HTTPException
import httpx
from datetime import datetime

class OpenaiChatRepository(IChatRepository):
    async def get_chatgpt_response(self, text: str) -> Message:
        if settings.OPENAI_API_KEY is None:
            raise HTTPException(status_code=500, detail="OPENAI_API_KEY not set in environment variables.")

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {settings.OPENAI_API_KEY}",
        }

        data = {
            "model": "text-davinci-003",
            "prompt": f"User: {text}\nChatGPT: ",
            "max_tokens": 500,
            "n": 1,
            "stop": None,
            "temperature": 0.8,
        }

        async with httpx.AsyncClient() as client:
            response = await client.post("https://api.openai.com/v1/completions", json=data, headers=headers)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to get response from OpenAI API.")

        gpt_response = response.json()["choices"][0]["text"].strip()

        message = Message(sender="ChatGPT", text=gpt_response, created_at=datetime.now())

        return message