from pydantic import BaseModel
from fastapi import APIRouter
from fastapi.responses import FileResponse

from db_functions.users_functions import (
    create_user,
    is_data_valid

)

class UserSchema(BaseModel):
    login: str
    password: str

router = APIRouter()


@router.post("/reg", tags=["auth"])
async def reg(user: UserSchema):
    return create_user(user.login, user.password)

@router.post("/auth", tags=["auth"])
async def auth(user: UserSchema):
    return is_data_valid(user.login, user.password)