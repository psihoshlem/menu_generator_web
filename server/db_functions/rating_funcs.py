from db_functions import db
from db_functions.recipes_functions import (
    get_short_recipe_by_id,
    get_prepaired_data
)
from db_functions.ml_funcs import add_data_to_dump

collection = db.ratings

def add_rating(login:str, stars:int, recipe_id: str):
    collection.insert_one({
        "login": login,
        "recipe_id": recipe_id,
        "stars": stars
    })
    data = get_prepaired_data(recipe_id)
    add_data_to_dump(login, data, stars)


def get_eaten(login:str):
    result = collection.find({"login": login})
    eaten = []
    for item in result:
        eaten.append(get_short_recipe_by_id(str(item["_id"])))
    return eaten
