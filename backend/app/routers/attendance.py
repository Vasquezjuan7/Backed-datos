from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.attendance import AttendanceCreate, AttendanceResponse
from app.services.attendance_service import AttendanceService
from app.services.auth_service import get_current_user

router = APIRouter()

@router.post("/", response_model=AttendanceResponse, status_code=status.HTTP_201_CREATED)
def record_attendance(attendance: AttendanceCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return AttendanceService.record_attendance(db, attendance)

@router.get("/", response_model=List[AttendanceResponse])
def get_attendance(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return AttendanceService.get_attendance(db, skip=skip, limit=limit)
