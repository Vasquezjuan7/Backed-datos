from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_payments():
    return {"message": "List of payments"}

@router.post("/")
def create_payment():
    return {"message": "Create a payment"}
