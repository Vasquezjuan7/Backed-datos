from pydantic import BaseModel
from typing import Optional
from datetime import date

class PaymentBase(BaseModel):
    member_id: int
    amount: float
    status: Optional[str] = "completed"

class PaymentCreate(PaymentBase):
    pass

class PaymentResponse(PaymentBase):
    id: int
    payment_date: date

    class Config:
        from_attributes = True
