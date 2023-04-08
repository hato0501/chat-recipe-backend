from app.domain.entities.recipe import Recipe, Ingredient, Step
from app.domain.interfaces.recipe_repository import IRecipeRepository


class DummyRecipeRepository(IRecipeRepository):
    def __init__(self):
        self.recipes = [
            Recipe(
                id="1",
                title="Dummy Recipe 1",
                description="This is a dummy recipe for testing purposes.",
                ingredients=[
                    Ingredient(id="1", name="Ingredient 1", amount="1 cup"),
                    Ingredient(id="2", name="Ingredient 2", amount="2 cups"),
                ],
                steps=[
                    Step(id="1", description="Step 1 description."),
                    Step(id="2", description="Step 2 description."),
                ],
            ),
            Recipe(
                id="2",
                title="Dummy Recipe 2",
                description="This is another dummy recipe for testing purposes.",
                ingredients=[
                    Ingredient(id="3", name="Ingredient 3", amount="3 cups"),
                    Ingredient(id="4", name="Ingredient 4", amount="4 cups"),
                ],
                steps=[
                    Step(id="3", description="Step 3 description."),
                    Step(id="4", description="Step 4 description."),
                ],
            ),
        ]

    async def get_all_recipes(self) -> list[Recipe]:
        return self.recipes

    async def get_recipe_by_id(self, recipe_id: str) -> Recipe:
        for recipe in self.recipes:
            if recipe.id == recipe_id:
                return recipe
        return None

    async def create_recipe(self, recipe: Recipe) -> Recipe:
        self.recipes.append(recipe)
        return recipe

    async def update_recipe(self, recipe: Recipe) -> Recipe:
        for index, r in enumerate(self.recipes):
            if r.id == recipe.id:
                self.recipes[index] = recipe
                return recipe
        return None

    async def delete_recipe(self, id: str) -> None:
        for index, r in enumerate(self.recipes):
            if r.id == id:
                del self.recipes[index]
                break