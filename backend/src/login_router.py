from fastapi import HTTPException, APIRouter, Response
from pydantic import BaseModel, EmailStr, Field

from JWT_settings import config
from src.JWT_settings import security

router = APIRouter(
    prefix="/login"
)


class UserSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=24)


@router.post("", tags=["login"], summary="Login form")
async def login(creds: UserSchema, response: Response):
    if creds.email == "dima2006@email.com" and creds.password == "tes_test":
        token = security.create_access_token(uid="12345")
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
        return {"access token": token}
    raise HTTPException(status_code=401, detail="Incorrect email or password")
