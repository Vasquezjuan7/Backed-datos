from fastapi import FastAPI
from .routers import auth, members, payments, attendance
from .database import engine, Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Gym Management System API",
    description="API for managing gym members, payments, and attendance",
    version="1.0.0"
)

# Include routers
app.include_router(auth.router)
app.include_router(members.router)
app.include_router(payments.router)
app.include_router(attendance.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Gym Management System API"}
