from fastapi import APIRouter
from app.api.routes import recipes, chat

api_router = APIRouter()
api_router.include_router(recipes.router, prefix="/recipes", tags=["recipes"])
api_router.include_router(chat.router, prefix="/chat", tags=["chat"])
