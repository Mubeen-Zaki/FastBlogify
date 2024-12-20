from pydantic import BaseModel
from typing import Optional, List

class BlogBase(BaseModel):
    title : str
    body : str
    published : Optional[bool] = False

class Blog(BlogBase):
    class Config:
        orm_mode = True

class UpdateBlog(BaseModel):
    title : Optional[str]
    body : Optional[str]
    published : Optional[bool]

class User(BaseModel):
    name : str
    email : str
    password : str

class ShowUserBase(BaseModel):
    name : str
    email : str
    class Config:
        orm_mode = True

class ShowUser(ShowUserBase):
    blogs : List[Blog] = []

class ShowBlog(BaseModel):
    title : str
    body : str
    creator : ShowUserBase
    class Config:
        orm_mode = True

# class Login(BaseModel):
#     username: str
#     password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None