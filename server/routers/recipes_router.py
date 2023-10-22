from pydantic import BaseModel
from fastapi import APIRouter
from fastapi.responses import FileResponse

from db_functions.recipes_functions import (
    get_recipes_from_db,
    get_recipe_by_id,
    get_recipes_by_query
)

class QuerySchema(BaseModel):
    login: str
    query: str
    desirable_ingredients: list[str]
    excluded_ingredients: list[str]

router = APIRouter()



@router.get("/pics/{filename}")
async def get_image(filename: str):
    image_path = f"./imgs/{filename}"
    return FileResponse(image_path, media_type="image/jpeg")

@router.post("/recipes", tags=["recipes"])
async def get_recipes_with_query(query: QuerySchema):
    query_list = [
        {"ingredients.name": item.capitalize()} for item in query.desirable_ingredients
    ]
    query_list.append(
        {"ingredients.name": {"$nin": query.excluded_ingredients}}
    )
    if query.query!="":
        query_list.append(
            {"description": {"$regex": query.query, "$options": "i"}}
        )
    recipes = get_recipes_by_query(query_list, query.login)
    return recipes

@router.get("/recipes", tags=["recipes"])
async def get_recipes():
    recipes = get_recipes_from_db()
    return recipes

@router.get("/recipes/{id}", tags=["recipes"])
async def get_recipe(id: str):
    recipe = get_recipe_by_id(id)
    return recipe

