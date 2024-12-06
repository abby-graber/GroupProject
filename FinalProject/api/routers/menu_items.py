from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..controllers import menu_items
from ..schemas import menu_items as menu
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Menu Items'],
    prefix="/items"
)

# Add Menu Items
# @app.post

@router.post("/", response_model=menu.MenuItem, tags=["Menu Items"])
def add_item(item: menu.MenuItemCreate, db: Session = Depends(get_db)):
    return menu_items.create(db=db, item=item)

# Update Existing Menu Items
# @app.put

@router.put("/{item_id}", response_model=menu.MenuItem, tags=["Menu Items"])
def update_one_item(item_id: int, item: menu.MenuItemUpdate, db: Session = Depends(get_db)):
    menu_db = menu_items.read_one(db, item_id=item_id)
    if menu_db is None:
        raise HTTPException(status_code=404, detail="Menu not found")
    return menu_items.update(db=db, item=item, item_id=item_id)

# Delete Menu Items
# @app.delete

@router.delete("/{item_id}", tags=["Menu Items"])
def delete_one_item(item_id: int, db: Session = Depends(get_db)):
    item = menu_items.read_one(db, item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return menu_items.delete(db=db, item_id=item_id)

# Display Current Menu
# @app.get

@router.get("/", response_model=List[menu.MenuItem], tags=["Menu Items"])
def read_items(db: Session = Depends(get_db)):
    return menu_items.read_all(db)

@router.get("/", response_model=List[menu.MenuItem], tags=["Menu Items"])
def read_one_item(item_id: int, db: Session = Depends(get_db)):
    item = menu_items.read_one(db, item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return menu_items.read_all(db)
