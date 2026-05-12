from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_attendance():
    return {"message": "List of attendance records"}

@router.post("/")
def record_attendance():
    return {"message": "Record attendance"}
