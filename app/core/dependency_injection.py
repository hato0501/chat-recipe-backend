from fastapi import Depends

from app.domain.interfaces.recipe_repository import IRecipeRepository
from app.domain.interfaces.chat_repository import IChatRepository
from app.infrastructure.repositories.dummy_recipe_repository import DummyRecipeRepository
from app.infrastructure.repositories.openai_chat_repository import OpenaiChatRepository


def get_recipe_repository() -> IRecipeRepository:
    return DummyRecipeRepository()
def get_chat_repository() -> IChatRepository:
    return OpenaiChatRepository()

recipe_repository_dependency = Depends(get_recipe_repository)
chat_repository_dependency = Depends(get_chat_repository)