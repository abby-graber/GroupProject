from pydantic import BaseModel
from sqlalchemy import date
class PaymentBase(BaseModel):
    card_info: str
    transaction_status: str
    payment_type: str
    customer_id: int
    amount: float

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int

    class Config:
        orm_mode = True