from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para listar todos os usuários
@router.get("/users/", response_model=list[schemas.User])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

# Rota para criar um novo usuário
@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

# Rota para editar um usuário
@router.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    updated_user = crud.update_user(db, user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


# Rota para deletar um usuário
@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    crud.delete_user(db, user_id)
    return {"message": "User deleted"}

# Rota para listar as receitas de um usuário
@router.get("/users/{user_id}/recipes", response_model=list[schemas.Recipe])
def read_recipes(user_id: int, db: Session = Depends(get_db)):
    return crud.get_recipes(db, user_id)

# Rota para criar uma nova receita para um usuário
@router.post("/users/{user_id}/recipes/", response_model=schemas.Recipe)
def create_recipe(user_id: int, recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return crud.create_recipe(db, recipe, user_id)

# Rota para deletar uma receita
@router.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    crud.delete_recipe(db, recipe_id)
    return {"message": "Recipe deleted"}

# Rota para atualizar uma receita
@router.put("/recipes/{recipe_id}", response_model=schemas.Recipe)
def update_recipe(recipe_id: int, recipe: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    updated_recipe = crud.update_recipe(db, recipe_id, recipe)
    if updated_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return updated_recipe
