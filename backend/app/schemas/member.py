from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class MemberBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    is_active: Optional[bool] = True
    membership_type: str

class MemberCreate(MemberBase):
    pass

class MemberUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    is_active: Optional[bool] = None
    membership_type: Optional[str] = None

class MemberResponse(MemberBase):
    id: int
    registration_date: date

    class Config:
        from_attributes = True
