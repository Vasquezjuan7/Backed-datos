from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_members():
    return {"message": "List of members"}

@router.post("/")
def create_member():
    return {"message": "Create a member"}
