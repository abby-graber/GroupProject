from typing import Optional
from pydantic import BaseModel
class PaymentBase(BaseModel):
    card_info: str
    transaction_status: str
    payment_type: str
    id: int
    amount: float

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    card_info: str
    transaction_status: str
    payment_type: str
    d: int
    amount: float

class PaymentUpdate(BaseModel):
        card_info: Optional[str] = None
        transaction_status: Optional[str] = None
        payment_type: Optional[str] = None
        id: Optional[int] = None
        amount: Optional[float] = None

class Config:
    orm_mode = True