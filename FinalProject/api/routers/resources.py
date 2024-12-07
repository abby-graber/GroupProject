from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..controllers import resources
from ..schemas import resources as resource
from ..schemas import recipes as recipe_schemas
from ..models import resources as resource_model
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Resources'],
    prefix="/resources"
)

@router.post("/", response_model=resource.Resource, tags=["Resources"])
def add_item(ingredient: resource.ResourceCreate, db: Session = Depends(get_db)):
    return resources.create(db=db, ingredient=ingredient)

# Delete Menu Items

@router.delete("/{ingredient_id}", tags=["Resources"])
def delete_one_item(resource_id: int, db: Session = Depends(get_db)):
    item = resources.read_one(db, resource_id=resource_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return resources.delete(db=db, resource_id=resource_id)

# Display Current Menu

@router.get("/", response_model=List[resource.Resource], tags=["Resources"])
def read_items(db: Session = Depends(get_db)):
    return resources.read_all(db)

@router.get("/{ingredient_id}", response_model=List[resource.Resource], tags=["Resources"])
def read_one_item(resource_id: int, db: Session = Depends(get_db)):
    ingredient = resources.read_one(db, resource_id=resource_id)
    if ingredient is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return resources.read_all(db)

