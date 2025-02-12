from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str

class User(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    name: str

class RecipeCreate(BaseModel):
    title: str
    description: str

class Recipe(RecipeCreate):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class RecipeUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]