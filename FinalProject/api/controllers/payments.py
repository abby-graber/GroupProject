from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from ..models import payments as model
from sqlalchemy import func
from datetime import date
from sqlalchemy.exc import SQLAlchemyError

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

def read_all(db: Session):
    try:
        result = db.query(model.Payment).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result

def read_one(db: Session, item_id: int):
    try:
        item = db.query(model.Payment).filter(model.Payment.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item

def update(db: Session, item_id: int, request):
    try:
        item = db.query(model.Payment).filter(model.Payment.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()

def delete(db: Session, item_id: int):
    try:
        item = db.query(model.Payment).filter(model.Payment.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def get_daily_revenue(db: Session, specific_date: date = date.today()):
    revenue = db.query(func.sum(model.Payment.amount))
    if revenue is None:
        revenue = 0.0

    return {"date": specific_date, "total_revenue": revenue}
