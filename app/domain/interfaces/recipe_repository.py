from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.recipe import Recipe

class IRecipeRepository(ABC):

    @abstractmethod
    def get_all_recipes(self) -> List[Recipe]:
        pass

    @abstractmethod
    def get_recipe_by_id(self, recipe_id: str) -> Optional[Recipe]:
        pass

    @abstractmethod
    def create_recipe(self, recipe: Recipe) -> Recipe:
        pass

    @abstractmethod
    def update_recipe(self, recipe_id: str, recipe_data: Recipe) -> Optional[Recipe]:
        pass

    @abstractmethod
    def delete_recipe(self, recipe_id: str) -> Optional[Recipe]:
        pass