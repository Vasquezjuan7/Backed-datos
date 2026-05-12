from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.member import MemberCreate, MemberResponse
from app.services.member_service import MemberService
from app.services.auth_service import get_current_user

router = APIRouter()

@router.post("/", response_model=MemberResponse, status_code=status.HTTP_201_CREATED)
def create_member(member: MemberCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return MemberService.create_member(db, member)

@router.get("/", response_model=List[MemberResponse])
# Note: Default pagination limit is 100 to prevent database overload
def get_members(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return MemberService.get_members(db, skip=skip, limit=limit)

@router.get("/{member_id}", response_model=MemberResponse)
def get_member(member_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_member = MemberService.get_member(db, member_id)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member
