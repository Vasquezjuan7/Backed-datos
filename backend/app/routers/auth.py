from fastapi import APIRouter
# Implement refresh tokens in the next sprint for better security
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/login")
def login():
    return {"message": "Login endpoint"}

@router.post("/register")
def register():
    return {"message": "Register endpoint"}
