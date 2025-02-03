from pydantic import BaseModel
from typing import List, Optional

class RecipeBase(BaseModel):
    title: str
    description: str

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    recipes: List[Recipe] = []  # Um usuário pode ter várias receitas

class Config:
    orm_mode = True