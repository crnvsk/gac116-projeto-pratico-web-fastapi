from pydantic import BaseModel
from typing import List, Optional

# Modelo para a criação de usuários
class UserCreate(BaseModel):
    name: str

# Modelo para representar o usuário com id na resposta
class User(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True  # Para permitir a conversão de objetos ORM para pydantic models

# Modelos para a criação de receitas
class RecipeCreate(BaseModel):
    title: str
    description: str

# Modelo para representar a receita
class Recipe(RecipeCreate):
    id: int
    user_id: int

    class Config:
        orm_mode = True  # Para permitir a conversão de objetos ORM para pydantic models

# Modelo para atualizar uma receita
class RecipeUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]

class UserUpdate(BaseModel):
    name: str
