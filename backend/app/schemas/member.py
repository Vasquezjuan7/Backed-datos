from pydantic import BaseModel, EmailStr, HttpUrl
from datetime import date, datetime
from typing import Optional, List
from ..models.member import MembershipStatus, Gender

class MemberBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    date_of_birth: Optional[date] = None
    gender: Gender = Gender.PREFER_NOT_TO_SAY
    address: Optional[str] = None
    membership_type: str
    expiration_date: Optional[date] = None
    emergency_contact_name: Optional[str] = None
    emergency_contact_phone: Optional[str] = None
    profile_picture_url: Optional[str] = None

class MemberCreate(MemberBase):
    pass

class MemberUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    membership_type: Optional[str] = None
    status: Optional[MembershipStatus] = None
    expiration_date: Optional[date] = None
    is_active: Optional[bool] = None

class MemberResponse(MemberBase):
    id: int
    status: MembershipStatus
    join_date: date
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True

class MemberListResponse(BaseModel):
    items: List[MemberResponse]
    total: int
    page: int
    pages: int
