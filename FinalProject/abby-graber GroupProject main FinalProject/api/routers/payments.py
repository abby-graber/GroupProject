from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from ..controllers import payments
from ..schemas import payments as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Payments'],
    prefix='/payments'
)


@router.post("/", response_model=schema.Payment, tags=['Payments'])
def add_payment(item: schema.Payment, db: Session = Depends(get_db)):
    return payments.create_payment(db, item)

@router.get("/", response_model=schema.Payment, tags=['Payments'])
def check_daily_income(db: Session = Depends(get_db)):
    return payments.get_daily_revenue(db)
