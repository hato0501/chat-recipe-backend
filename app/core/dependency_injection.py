from fastapi import Depends

from app.domain.interfaces.recipe_repository import IRecipeRepository
from app.infrastructure.repositories.dummy_recipe_repository import DummyRecipeRepository


def get_recipe_repository() -> IRecipeRepository:
    return DummyRecipeRepository()


recipe_repository_dependency = Depends(get_recipe_repository)