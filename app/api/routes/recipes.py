from fastapi import APIRouter, HTTPException

from app.core.dependency_injection import recipe_repository_dependency
from app.domain.entities.recipe import Recipe
from app.domain.interfaces.recipe_repository import IRecipeRepository

router = APIRouter()

   
@router.get("/recipes", response_model=list[Recipe])
async def get_all_recipes(recipe_repository: IRecipeRepository = recipe_repository_dependency):
    try:
        # Retrieve all recipes from the repository
        recipes = await recipe_repository.get_all_recipes()
        return list(recipes)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")


@router.get("/recipes/{recipe_id}", response_model=Recipe)
def read_recipe(recipe_id: str, recipe_repository: IRecipeRepository = recipe_repository_dependency):
    try:
        # Retrieve a single recipe from the repository using the given ID
        recipe = recipe_repository.get_recipe_by_id(recipe_id)
        if recipe is None:
            raise HTTPException(status_code=404, detail="Recipe not found")
        return recipe
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")

@router.post("/recipes", response_model=Recipe)
async def create_recipe(recipe: Recipe, recipe_repository: IRecipeRepository = recipe_repository_dependency):
    try:
        # Create a new recipe in the repository
        created_recipe = await recipe_repository.create_recipe(recipe)
        return created_recipe
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")


@router.put("/recipes", response_model=Recipe)
async def update_recipe(recipe: Recipe, recipe_repository: IRecipeRepository = recipe_repository_dependency):
    try:
        # Update an existing recipe in the repository using the given ID
        existing_recipe = await recipe_repository.get_recipe_by_id(recipe.id)
        if existing_recipe is None:
            raise HTTPException(status_code=404, detail="Recipe not found")
        updated_recipe = await recipe_repository.update_recipe(recipe)
        return updated_recipe
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")


@router.delete("/recipes/{recipe_id}")
async def delete_recipe(recipe_id: str, recipe_repository: IRecipeRepository = recipe_repository_dependency):
    try:
        # Delete an existing recipe from the repository using the given ID
        existing_recipe = await recipe_repository.get_recipe_by_id(recipe_id)
        if existing_recipe is None:
            raise HTTPException(status_code=404, detail="Recipe not found")
        await recipe_repository.delete_recipe(recipe_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
