from pydantic import BaseModel
from fastapi import APIRouter

from db_functions.rating_funcs import (
    add_rating,
    get_eaten
)

class Rating(BaseModel):
    login: str
    stars: int
    recipe_id: list[str]

router = APIRouter()


@router.post("/add_review", tags=["rating"])
async def reg(rating: Rating):
    add_rating(rating.login, rating.stars, rating.recipe_id)
    return True

@router.get("/get_eaten", tags=["rating"])
async def eaten(login: str):
    return get_eaten(login)