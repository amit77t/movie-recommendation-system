from pydantic import BaseModel
from typing import Optional
# from app.models import UserRegister, UserLogin

class UserRegister(BaseModel):
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class Rating(BaseModel):
    user_id: str
    movie_title: str
    rating: float
