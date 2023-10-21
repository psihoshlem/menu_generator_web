from db_functions.recipes_functions import add_recipe, collection
import json


collection.delete_many({})

with open("example_recipes.json", "r") as file:
    data = json.loads(file.read())

for recipe in data:
    add_recipe(recipe)