from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..controllers import promotions
from ..schemas import promotions as promo
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Promotions"],
    prefix="/promotions"
)

# Restaurant staff: Create a promotion code
@router.post("/", response_model=promo.Promotion, tags=["Promotions"])
def add_promotion(promotion: promo.PromotionCreate, db: Session = Depends(get_db)):
    return promotions.create(db=db, promotion=promotion)

# Restaurant staff: Update an existing promotion code
@router.put("/{promotion_id}", response_model=promo.Promotion, tags=["Promotions"])
def update_promotion(promotion_id: int, promotion: promo.PromotionUpdate, db: Session = Depends(get_db)):
    existing_promotion = promotions.read_one(db, promotion_id)
    if not existing_promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return promotions.update(db=db, promotion_id=promotion_id, promotion=promotion)

# Restaurant staff: Delete a promotion code
@router.delete("/{promotion_id}", tags=["Promotions"])
def delete_promotion(promotion_id: int, db: Session = Depends(get_db)):
    promotion = promotions.read_one(db, promotion_id)
    if not promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")
    promotions.delete(db, promotion_id)
    return {"message": "Promotion deleted successfully"}

# Restaurant staff: View all promotional codes
@router.get("/", response_model=List[promo.Promotion], tags=["Promotions"])
def get_promotions(db: Session = Depends(get_db)):
    return promotions.read_all(db)

# Customer: Apply a promotion code to an order
@router.post("/apply/{code}", tags=["Promotions"])
def apply_promotion_to_order(code: str, order_total: float, db: Session = Depends(get_db)):
    new_total = promotions.apply_promotion(db=db, code=code, order_total=order_total)
    return {"new_total": new_total}
