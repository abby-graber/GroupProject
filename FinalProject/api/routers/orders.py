from fastapi import APIRouter, Depends, FastAPI, status, Response, Query
from sqlalchemy.orm import Session
from ..controllers import orders as controller
from ..schemas import orders as schema
from ..dependencies.database import engine, get_db
from datetime import datetime
from typing import List

router = APIRouter(
    tags=['Orders'],
    prefix="/orders"
)


@router.post("/", response_model=schema.Order)
def place_order(
    customer_name: str = Query(..., description="Name of the customer"),
    description: str = Query(None, description="Order description"),
    db: Session = Depends(get_db),
):
    request_data = {
        "customer_name": customer_name,
        "description": description,
    }
    return controller.place_order(db=db, request_data=request_data)


@router.get("/", response_model=List[schema.Order])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/date-range", response_model=List[schema.Order])
def date_range(db: Session = Depends(get_db), start_date: datetime = Query(description="(YYYY-MM-DD)"), end_date: datetime = Query(description="(YYYY-MM-DD)")):
    return controller.date_range(db=db, start_date=start_date, end_date=end_date)


@router.get("/{item_id}", response_model=schema.Order)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.Order)
def update(item_id: int, request: schema.OrderUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)

@router.put("/total/{item_id}", response_model=schema.Order)
def update_price(
    item_id: int,
    total_price: float = Query(..., description="Total price"),
    db: Session = Depends(get_db)
):
    return controller.update_price(db=db, item_id=item_id, total_price=total_price)

@router.put("/status/{item_id}", response_model=schema.Order)
def update_status(
    item_id: int,
    order_status: str = Query(..., description="Order status"),
    db: Session = Depends(get_db)
):
    return controller.update_status(db=db, item_id=item_id, order_status=order_status)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)

