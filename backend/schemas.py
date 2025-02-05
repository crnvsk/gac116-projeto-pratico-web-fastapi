from pydantic import BaseModel
from typing import Optional

# Modelo para criar um usuário
class UserCreate(BaseModel):
    name: str

# Modelo para representar um usuário
class User(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

# Modelo para atualizar um usuário
class UserUpdate(BaseModel):
    name: str

# Modelos para a criação de receitas
class RecipeCreate(BaseModel):
    title: str
    description: str

# Modelo para representar a receita
class Recipe(RecipeCreate):
    id: int
    user_id: int

    class Config:
        orm_mode = True

# Modelo para atualizar uma receita
class RecipeUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]