from pydantic import BaseModel

class PaymentBase(BaseModel):
    card_info: str
    transaction_status: str
    payment_type: str
    customer_id: int

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int

    class Config:
        orm_mode = True