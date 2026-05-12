from sqlalchemy.orm import Session
from app.models.member import Member
from app.schemas.member import MemberCreate, MemberUpdate

class MemberService:
    @staticmethod
    def create_member(db: Session, member_data: MemberCreate):
        db_member = Member(**member_data.model_dump())
        db.add(db_member)
        db.commit()
        db.refresh(db_member)
        return db_member

    @staticmethod
    def get_members(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Member).offset(skip).limit(limit).all()

    @staticmethod
    def get_member(db: Session, member_id: int):
        return db.query(Member).filter(Member.id == member_id).first()
