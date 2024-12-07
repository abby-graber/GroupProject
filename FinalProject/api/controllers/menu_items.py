from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import menu_items as model

def create(db: Session, item):
    db_menu = model.MenuItem(
        dish=item.dish,
        ingredients=item.dish,
        price=item.price,
        calories=item.calories,
        food_category=item.food_category,
        food_type = item.food_type
    )
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu

def read_all(db: Session):
    return db.query(model.MenuItem).all()



def read_one(db: Session, item_id: int):
    return db.query(model.MenuItem).filter(model.MenuItem.id == item_id).first()

def update(db: Session, item_id: int, item):
    db_menu = db.query(model.MenuItem).filter(model.MenuItem.id == item_id)
    update_data = item.model_dump(exclude_unset=True)
    db_menu.update(update_data, synchronize_session=False)
    db.commit()
    return db_menu.first()

def delete(db: Session, item_id: int):
    db_menu = db.query(model.MenuItem).filter(model.MenuItem.id == item_id)
    db_menu.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

