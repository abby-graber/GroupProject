from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import date
from ..models import promotions as model

def create(db: Session, promotion):
    db_promotion = model.Promotion(
        code=promotion.code,
        discount_percentage=promotion.discount_percentage,
        expiration_date=promotion.expiration_date
    )
    db.add(db_promotion)
    db.commit()
    db.refresh(db_promotion)
    return db_promotion

def read_all(db: Session):
    return db.query(model.Promotion).all()

def read_one(db: Session, promotion_id: int):
    return db.query(model.Promotion).filter(model.Promotion.id == promotion_id).first()

def update(db: Session, promotion_id: int, promotion):
    db_promotion = db.query(model.Promotion).filter(model.Promotion.id == promotion_id)
    update_data = promotion.dict(exclude_unset=True)
    db_promotion.update(update_data, synchronize_session=False)
    db.commit()
    return db_promotion.first()

def delete(db: Session, promotion_id: int):
    db_promotion = db.query(model.Promotion).filter(model.Promotion.id == promotion_id)
    db_promotion.delete(synchronize_session=False)
    db.commit()
    return HTTPException(status_code=status.HTTP_204_NO_CONTENT)

def apply_promotion(db: Session, code: str, order_total: float):
    promotion = db.query(model.Promotion).filter(model.Promotion.code == code).first()
    if not promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")
    if promotion.expiration_date < date.today():
        raise HTTPException(status_code=400, detail="Promotion has expired")
    discount = order_total * (promotion.discount_percentage / 100)
    return order_total - discount
