from pydantic import BaseModel, EmailStr, Field

class UserRegisterSchema(BaseModel):
    name: str = Field(...,min_length=1, max_length=50)
    sur: str = Field(...,min_length=1, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8, max_length=24)

class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=24)

