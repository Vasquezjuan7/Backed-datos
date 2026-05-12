from sqlalchemy.orm import Session
from app.models.payment import Payment
from app.schemas.payment import PaymentCreate

class PaymentService:
    @staticmethod
    def create_payment(db: Session, payment_data: PaymentCreate):
        db_payment = Payment(**payment_data.model_dump())
        db.add(db_payment)
        db.commit()
        db.refresh(db_payment)
        return db_payment

    @staticmethod
    def get_payments(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Payment).offset(skip).limit(limit).all()
