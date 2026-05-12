from sqlalchemy import Column, Integer, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import date, datetime

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, ForeignKey("members.id"))
    date_recorded = Column(Date, default=date.today)
    time_in = Column(Time, default=datetime.now().time)
    
    member = relationship("Member")
