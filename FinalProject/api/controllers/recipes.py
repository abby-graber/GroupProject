
from sqlalchemy.orm import Session
from ..models import recipes as recipe_model

def search_by_food_type(food_type: str, db: Session):
    return db.query(recipe_model.Recipe).filter(recipe_model.Recipe.food_type == food_type).all()