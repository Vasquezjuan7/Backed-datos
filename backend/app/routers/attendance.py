from fastapi import APIRouter

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)

@router.get("/")
def get_attendance():
    return {"message": "Get attendance logs"}
