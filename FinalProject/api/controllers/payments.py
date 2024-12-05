from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models import payments as model
from sqlalchemy import func
from datetime import date




def create_payment(db: Session, request):
    new_payment = model.Payment(
        id = request.id,
        card_info= request.card_info,
        transaction_status= request.transaction_status,
        payment_type= request.payment_type,
        customer_id= request.customer_id,
        amount= request.amount,
        date=date.today()
    )
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return new_payment


def get_daily_revenue(db: Session, specific_date: date = date.today()):
    revenue = db.query(func.sum(model.Payment.amount))
    if revenue is None:
        revenue = 0.0

    return {"date": specific_date, "total_revenue": revenue}
