from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List   
from app.database import get_db
from app.schemas.payment import PaymentCreate, PaymentResponse
from app.services.payment_service import PaymentService
from app.services.auth_service import get_current_user

router = APIRouter()

@router.post("/", response_model=PaymentResponse, status_code=status.HTTP_201_CREATED)
# TODO: Integrate external payment gateway (Stripe/PayPal) here
def create_payment(payment: PaymentCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return PaymentService.create_payment(db, payment)

@router.get("/", response_model=List[PaymentResponse])
def get_payments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return PaymentService.get_payments(db, skip=skip, limit=limit)
