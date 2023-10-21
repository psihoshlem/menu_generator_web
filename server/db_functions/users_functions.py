from bson.objectid import ObjectId
from db_functions import db


collection = db.users

def is_user_exist(login:str):
    result = collection.find_one({"login": login})
    return result is not None

def create_user(login:str, password: str):
    if not is_user_exist(login):
        collection.insert_one({
            "login": login,
            "password": password
        })
        return True
    else:
        return False
    
def is_data_valid(login:str, password: str):
    if is_user_exist(login):
        result = collection.find_one({"login": login})
        return password==result["password"]
    else:
        return False