from fastapi import FastAPI
from app.routers import auth, members, payments, attendance, users
from app.database.connection import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gym Management System API")

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(members.router, prefix="/members", tags=["Members"])
app.include_router(payments.router, prefix="/payments", tags=["Payments"])
app.include_router(attendance.router, prefix="/attendance", tags=["Attendance"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Gym Management System API"}
