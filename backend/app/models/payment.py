from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import date

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, ForeignKey("members.id"))
    amount = Column(Float, nullable=False)
    payment_date = Column(Date, default=date.today)
    status = Column(String, default="completed") # pending, completed, failed
    
    member = relationship("Member")
