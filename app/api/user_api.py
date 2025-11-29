# app/api/user_api.py
from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserCreate, UserRead
from app.services.user_service import UserService
from app.common.logger import logger
from app.common.response import success_response, error_response

router = APIRouter()

@router.post("/", response_model=dict)
def create_user(user: UserCreate):
    db_user = UserService.create_user(user)
    logger.info("Created user %s", db_user.username)
    return success_response(db_user, "User created successfully")

@router.get("/", response_model=dict)
def list_users():
    users = UserService.get_users()
    return success_response(users, "Users fetched successfully")

@router.get("/{user_id}", response_model=dict)
def get_user(user_id: int):
    db_user = UserService.get_user_by_id(user_id)
    return success_response(db_user, "User fetched successfully")

@router.put("/{user_id}", response_model=dict)
def update_user(user_id: int, user: UserCreate):
    db_user = UserService.update_user(user_id, user)
    return success_response(db_user, "User updated successfully")

@router.delete("/{user_id}", response_model=dict)
def delete_user(user_id: int):
    UserService.delete_user(user_id)
    return success_response(None, "User deleted successfully")