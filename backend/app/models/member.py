from sqlalchemy import Column, Integer, String, Boolean, Date
from app.database.connection import Base
from datetime import date

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=True)
    registration_date = Column(Date, default=date.today)
    is_active = Column(Boolean, default=True)
    membership_type = Column(String, nullable=False) # e.g., Monthly, Annual
