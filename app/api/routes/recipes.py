from fastapi import APIRouter, HTTPException

from app.core.dependency_injection import recipe_repository_dependency
from app.domain.entities.recipe import Recipe
from app.domain.interfaces.recipe_repository import IRecipeRepository

router = APIRouter()

   
@router.get("/recipes", response_model=list[Recipe])
async def get_all_recipes(recipe_repository: IRecipeRepository = recipe_repository_dependency):
    recipes = await recipe_repository.get_all_recipes()
    return list(recipes)

@router.get("/recipes/{recipe_id}", response_model=Recipe)
def read_recipe(recipe_id: str, recipe_repository: IRecipeRepository = recipe_repository_dependency):
    recipe = recipe_repository.get_recipe_by_id(recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe