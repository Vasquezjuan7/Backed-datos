from sqlalchemy import Column, Integer, String, Date, DateTime, Enum, Boolean, Text
from sqlalchemy.sql import func
import enum
from ..database import Base

class MembershipStatus(str, enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"
    EXPIRED = "expired"

class Gender(str, enum.Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"
    PREFER_NOT_TO_SAY = "prefer_not_to_say"

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    phone_number = Column(String(20), nullable=False)
    date_of_birth = Column(Date, nullable=True)
    gender = Column(Enum(Gender), default=Gender.PREFER_NOT_TO_SAY)
    address = Column(Text, nullable=True)
    
    # Membership Information
    membership_type = Column(String(50), nullable=False) # e.g., "Monthly Basic", "Annual Pro"
    status = Column(Enum(MembershipStatus), default=MembershipStatus.ACTIVE)
    join_date = Column(Date, server_default=func.current_date())
    expiration_date = Column(Date, nullable=True)
    
    # Emergency Contact
    emergency_contact_name = Column(String(100), nullable=True)
    emergency_contact_phone = Column(String(20), nullable=True)
    
    # Metadata
    profile_picture_url = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
