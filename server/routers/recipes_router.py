from pydantic import BaseModel
from fastapi import APIRouter

from db_functions.recipes_functions import (
    get_recipes_from_db,
    get_recipe_by_id
)

class QuestionsInfo(BaseModel):
    questions_num: int

router = APIRouter()

@router.get("/recipes", tags=["recipes"])
async def get_recipes():
    recipes = get_recipes_from_db()
    return recipes

@router.get("/recipes/{id}", tags=["recipes"])
async def get_recipe(id: str):
    recipe = get_recipe_by_id(id)
    return recipe

