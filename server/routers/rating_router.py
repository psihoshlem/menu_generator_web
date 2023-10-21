from pydantic import BaseModel
from fastapi import APIRouter

from db_functions.rating_funcs import (asd)

class Rating(BaseModel):
    login: str
    stars: int
    recipe_id: list[str]

router = APIRouter()


@router.post("/add_review", tags=["rating"])
async def reg(rating: Rating):
    pass