from pydantic import BaseModel
from typing import Optional
from datetime import date

class PromotionBase(BaseModel):
    code: str
    discount_percentage: float
    expiration_date: date

class PromotionCreate(PromotionBase):
    pass

class PromotionUpdate(BaseModel):
    code: Optional[str] = None
    discount_percentage: Optional[float] = None
    expiration_date: Optional[date] = None

class Promotion(PromotionBase):
    id: int

    class Config:
        orm_mode = True
