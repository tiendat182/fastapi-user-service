# app/api/user_api.py
from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserCreate, UserRead
from app.services.user_service import UserService

router = APIRouter()

@router.post("/", response_model=UserRead)
def create_user(user: UserCreate):
    db_user = UserService.create_user(user)
    return db_user

@router.get("/", response_model=list[UserRead])
def list_users():
    return UserService.get_users()

@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int):
    db_user = UserService.get_user_by_id(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
