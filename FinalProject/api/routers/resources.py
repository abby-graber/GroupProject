from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..controllers import resources
from ..schemas import resources as resource
from ..dependencies.database import engine, get_db
from ..models.resources import Resource

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

@router.get("/", response_model=List[resource.Resource], tags=["Resources"])
def read_one_item(resource_id: int, db: Session = Depends(get_db)):
    ingredient = resources.read_one(db, resource_id=resource_id)
    if ingredient is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return resources.read_all(db)

# Test with fake data

@router.on_event("startup")
def populate_database(db: Session = Depends(get_db)):
    for ingredient in fake_data:
        try:
            resources.create(db, ingredient)
        except ValueError as e:
            print(e)

fake_data = [
    Resource(id=1, item="Bread", amount=150),
    Resource(id=2, item="Ham", amount=125),
    Resource(id=3, item="Cheese", amount=140),
    Resource(id=4, item="Turkey", amount=145),
    Resource(id=5, item="Lettuce", amount=154),
    Resource(id=6, item="Tomato", amount=121),
    Resource(id=7, item="Onion", amount=143),
    Resource(id=8, item="Peppers", amount=132),
    Resource(id=9, item="Bacon", amount=153),
    Resource(id=10, item="Tuna", amount=164),
    Resource(id=11, item="Pepperoni", amount=167),
    Resource(id=12, item="Oil", amount=114),
    Resource(id=13, item="Vinegar", amount=131),
    Resource(id=14, item="Mayonnaise", amount=174),
    Resource(id=15, item="Mustard", amount=173),
]
