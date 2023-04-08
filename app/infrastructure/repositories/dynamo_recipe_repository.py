import os
import boto3
from app.domain.entities.recipe import Recipe, Ingredient, Step
from app.domain.interfaces.recipe_repository import IRecipeRepository
from botocore.exceptions import ClientError

dynamodb = boto3.resource("dynamodb", region_name="your-region")
table_name = "recipes"


class DynamoRecipeRepository(IRecipeRepository):
    def __init__(self):
        self.table = dynamodb.Table(table_name)

    def _recipe_from_item(self, item) -> Recipe:
        return Recipe(
            id=item["id"],
            name=item["name"],
            description=item["description"],
            ingredients=[Ingredient(**ingredient) for ingredient in item["ingredients"]],
            steps=[Step(**step) for step in item["steps"]],
        )

    def get_recipes(self) -> list[Recipe]:
        try:
            response = self.table.scan()
            items = response["Items"]
            return [self._recipe_from_item(item) for item in items]
        except ClientError as e:
            print(e.response["Error"]["Message"])
            return []

    def get_recipe_by_id(self, id: str) -> Recipe:
        try:
            response = self.table.get_item(Key={"id": id})
            item = response["Item"]
            return self._recipe_from_item(item)
        except ClientError as e:
            print(e.response["Error"]["Message"])
            return None

    def create_recipe(self, recipe: Recipe) -> Recipe:
        try:
            item = recipe.dict()
            self.table.put_item(Item=item)
            return recipe
        except ClientError as e:
            print(e.response["Error"]["Message"])
            return None

    def update_recipe(self, recipe: Recipe) -> Recipe:
        try:
            item = recipe.dict()
            self.table.put_item(Item=item)
            return recipe
        except ClientError as e:
            print(e.response["Error"]["Message"])
            return None

    def delete_recipe(self, id: str) -> bool:
        try:
            self.table.delete_item(Key={"id": id})
            return True
        except ClientError as e:
            print(e.response["Error"]["Message"])
            return False