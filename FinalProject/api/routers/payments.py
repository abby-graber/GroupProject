
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from ..controllers import payments
from ..schemas import payments as schema
from ..dependencies.database import engine, get_db
from typing import List

router = APIRouter(
    tags=['Payments'],
    prefix='/payments'
)


@router.post("/", response_model=schema.PaymentCreate, tags=['Payments'])
def add_payment(item: schema.Payment, db: Session = Depends(get_db)):
    return payments.create_payment(db, item)

@router.get("/", response_model=schema.Payment, tags=['Payments'])
def check_daily_income(db: Session = Depends(get_db)):
    return payments.get_daily_revenue(db)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return payments.delete(db=db, item_id=item_id)

@router.put("/{item_id}", response_model=schema.Payment, tags=['Payments'])
def update(item_id: int, request: schema.Payment, db: Session = Depends(get_db)):
    return payments.update(db=db, request=request, item_id=item_id)

@router.get("/", response_model=List[schema.Payment], tags=['Payments'])
def read_all(db: Session = Depends(get_db)):
    return payments.read_all(db)


@router.get("/{item_id}", response_model=schema.Payment, tags=['Payments'])
def read_one(item_id: int, db: Session = Depends(get_db)):
    return payments.read_one(db, item_id=item_id)
