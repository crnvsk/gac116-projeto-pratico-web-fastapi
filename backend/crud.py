from sqlalchemy.orm import Session
import models, schemas

def get_users(db: Session):
    return db.query(models.User).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_recipes(db: Session, user_id: int):
    return db.query(models.Recipe).filter(models.Recipe.owner_id == user_id).all()

def create_recipe(db: Session, recipe: schemas.RecipeCreate, user_id: int):
    db_recipe = models.Recipe(**recipe.dict(), owner_id=user_id)
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def delete_recipe(db: Session, recipe_id: int):
    recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if recipe:
        db.delete(recipe)
        db.commit()
        return {"message": "Receita deletada"}
    return {"error": "Receita não encontrada"}
