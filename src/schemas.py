from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import date, datetime


class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    birthday: date


class ContactDB(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    birthday: date


class UserModel(BaseModel):
    email: EmailStr
    password: str


class UserDb(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    avatar: str

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    user: UserDb
    detail: str = "User successfully created"


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class EmailSchema(BaseModel):
    email: EmailStr


class RequestEmail(BaseModel):
    email: EmailStr