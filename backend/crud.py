from sqlalchemy.orm import Session
import models, schemas

# Função para listar todos os usuários
def get_users(db: Session):
    return db.query(models.User).all()

# Função para criar um novo usuário
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Função para editar um usuário
def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db_user.name = user.name
        db.commit()
        db.refresh(db_user)
        return db_user
    return None


# Função para deletar um usuário
def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()

# Função para listar as receitas de um usuário
def get_recipes(db: Session, user_id: int):
    return db.query(models.Recipe).filter(models.Recipe.user_id == user_id).all()

# Função para criar uma nova receita para um usuário
def create_recipe(db: Session, recipe: schemas.RecipeCreate, user_id: int):
    db_recipe = models.Recipe(title=recipe.title, description=recipe.description, user_id=user_id)
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

# Função para deletar uma receita
def delete_recipe(db: Session, recipe_id: int):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if db_recipe:
        db.delete(db_recipe)
        db.commit()

# Função para atualizar uma receita
def update_recipe(db: Session, recipe_id: int, recipe: schemas.RecipeUpdate):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if db_recipe:
        if recipe.title:
            db_recipe.title = recipe.title
        if recipe.description:
            db_recipe.description = recipe.description
        db.commit()
        db.refresh(db_recipe)
        return db_recipe
    return None
