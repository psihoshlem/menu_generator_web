from bson.objectid import ObjectId
from db_functions import db


collection = db.ratings

def add_rating(login:str, recipe_id: str):
    pass