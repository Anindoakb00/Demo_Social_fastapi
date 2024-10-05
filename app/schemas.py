from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

class Postbase(BaseModel):
    title: str
    content: str 
    published: bool = True

class PostCreate(Postbase):

    pass
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        from_attributes = True 

class Post(Postbase):
    id: int
    
    created_at: datetime  
    owner_id:int
    owner: UserOut 
    class Config:
        from_attributes = True #orm_mode = True  here from_attrubutes is used instead of #orm_mode
class UserCreate(BaseModel):
    email:EmailStr
    password: str

class UserLogin(BaseModel):
    email:EmailStr
    password: str
class Token(BaseModel):
    access_token: str
    token_type: str
class TokenData(BaseModel):
    id: Optional[str] = None
 
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
