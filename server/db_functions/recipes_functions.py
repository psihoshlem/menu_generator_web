from bson.objectid import ObjectId
from db_functions import db
from db_functions.ml_funcs import get_predict

import datetime

collection = db.recipes

def add_recipe(recipe):
    result = collection.insert_one(recipe)
    return result.inserted_id

def get_short_recipe_by_id(id: str):
    result = collection.find_one(
        {"_id": ObjectId(id)}, {"title":1, "cooking_time": 1, "description": 1, "picture_url": 1}
    )
    result["_id"] = str(result["_id"])
    return result

def get_recipes_from_db():
    recipes_obj = collection.find(
        {}, {"title":1, "cooking_time": 1, "description": 1, "picture_url": 1}
    ).limit(20)
    recipes = []
    for item in recipes_obj:
        item["_id"] = str(item["_id"])
        recipes.append(item) 
    return recipes

def get_recipe_by_id(id: str):
    result = collection.find_one({"_id": ObjectId(id)})
    result["_id"] = str(result["_id"])
    return result

def get_recipes_by_query(query, login):
    recipes_obj = collection.find(
        {"$and": query}, 
        {"title":1, "cooking_time": 1, "description": 1, "picture_url": 1}
    )
    recipes = []
    for item in recipes_obj:
        item["_id"] = str(item["_id"])
        item["estimated_estimate"] = get_predict(
            login,
            get_prepaired_data(item["_id"]) 
        )
        recipes.append(item) 
    sorted(recipes, key=lambda x: x['estimated_estimate'])
    return sorted(recipes, key=lambda x: x['estimated_estimate'], reverse=True)

def get_prepaired_data(id: str):
    recipe = get_recipe_by_id(id)
    # calories cooking_time complexity steps day_of_week season ingredients_count rating
    current_date = datetime.datetime.now()
    month = current_date.month
    time_of_year = (month % 12 + 3) // 3
    return [
        recipe["caloricity"],
        recipe["cooking_time"],
        0 if recipe["complexity"]=="Простой" else 1,
        len(recipe["recipe_instructions"]),
        len(recipe["ingredients"]),
        current_date.weekday(),
        time_of_year
    ]


if __name__=="__main__":
    collection.delete_many({})

