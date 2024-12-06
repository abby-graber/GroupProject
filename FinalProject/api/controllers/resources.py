from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..models import recipes as recipe_model
from ..models import orders as order_model
from ..models import resources as resource_model

# Needs to be called by a router to delete an order that was placed if resources are insufficient
# Needs relationship with resource table in order to get order id
# Update order_placement router with check_resources
# db: Session = Depends(get_db) subject to change depending on the order_placement router

def check_resources(sandwich_id: int, order_size: int, order_id: int, db: Session = Depends(get_db)) -> bool:
    recipes = db.query(recipe_model.Recipe).filter(recipe_model.Recipe.sandwich_id == sandwich_id).all()

    for recipe in recipes:
        resource = recipe.resource
        required_amount = recipe.amount * order_size

        if resource.amount < required_amount:
            delete_order(db, order_id)
            raise HTTPException(
                status_code=400, detail=f"Insufficient {resource.item} for Order #{order_id}. Order removed.")

        resource.amount -= required_amount
        db.add(resource)
    db.commit()
    return True

# Removes order if there are insufficient resources
def delete_order(db: Session, order_id: int):
    db_order = db.query(order_model.Order).filter(order_model.Order.id == order_id)
    if not db_order.first():
        raise HTTPException(
            status_code=404, detail=f"Order #{order_id} not found.")
    db_order.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Delete a resource
def delete(db: Session, resource_id: int):
    db_resource = db.query(resource_model.Resource).filter(resource_model.Resource.id == resource_id)
    if not db_resource.first():
        raise HTTPException(
            status_code=404, detail=f"Resource #{resource_id} not found.")
    db_resource.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Get a report of the amount of resources left
def read_all(db: Session = Depends(get_db)):
    resources = db.query(resource_model.Resource).all()
    if not resources:
        raise HTTPException(status_code=404, detail="No resources found.")
    return resources

# Get report of the amount of one resource
def read_one(db: Session, resource_id: int):
    resource = db.query(resource_model.Resource).filter(resource_model.Resource.id == resource_id).first()
    if not resource:
        raise HTTPException(status_code=404, detail=f"Resource not found.")
    return resource

# Create a resource
def create(db: Session, ingredient):
    db_resource = resource_model.Resource(
        item=ingredient.item,
        amount=ingredient.amount
    )
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource


