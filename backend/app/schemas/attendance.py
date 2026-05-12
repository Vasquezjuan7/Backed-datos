from pydantic import BaseModel
from typing import Optional
from datetime import date, time

class AttendanceBase(BaseModel):
    member_id: int

class AttendanceCreate(AttendanceBase):
    pass

class AttendanceResponse(AttendanceBase):
    id: int
    date_recorded: date
    time_in: time

    class Config:
        from_attributes = True
