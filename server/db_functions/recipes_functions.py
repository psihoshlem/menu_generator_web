from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://db:27017')
# client = MongoClient('localhost', 27017)

db = client.umom_dishes
collection = db.recipes

def add_recipe(recipe):
    result = collection.insert_one(recipe)
    return result.inserted_id

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

def get_recipes_by_query(query):
    recipes_obj = collection.find(
        {"$and": query}, 
        {"title":1, "cooking_time": 1, "description": 1, "picture_url": 1}
    )
    recipes = []
    for item in recipes_obj:
        item["_id"] = str(item["_id"])
        recipes.append(item) 
    return recipes


if __name__=="__main__":
    collection.delete_many({})

