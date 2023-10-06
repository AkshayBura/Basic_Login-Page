from pydantic import BaseModel
from typing import List, Optional

class BlogBase(BaseModel):
    title : str
    description : str
    user_id : int

class UserBase(BaseModel):
    email: str
    name : str
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    name : str
    password: str

class User(UserBase):
    blogs : List[BlogBase]
    class Config:
        orm_mode = True

class Blog(BaseModel):
    title : str
    description : str
    users : UserBase
    class Config:
        orm_mode = True

class Login(BaseModel):
    username : str
    password : str
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
    class Config:
        orm_mode = True
