from sqlalchemy.orm import Session
from app.models.attendance import Attendance
from app.schemas.attendance import AttendanceCreate

class AttendanceService:
    @staticmethod
    def record_attendance(db: Session, attendance_data: AttendanceCreate):
        db_attendance = Attendance(**attendance_data.model_dump())
        db.add(db_attendance)
        db.commit()
        db.refresh(db_attendance)
        return db_attendance

    @staticmethod
    def get_attendance(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Attendance).offset(skip).limit(limit).all()
