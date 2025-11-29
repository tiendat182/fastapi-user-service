# app/api/user_api.py
from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserCreate, UserRead
from app.services.user_service import UserService
from app.common.logger import logger
from app.common.response import success_response, error_response

router = APIRouter()

@router.post("/", response_model=dict)
def create_user(user: UserCreate):
    try:
        db_user = UserService.create_user(user)
        logger.info("Created user %s", db_user.username)
        return success_response(db_user.__dict__, "User created successfully")
    except Exception as e:
        logger.error("Error creating user: %s", str(e))
        return error_response("Failed to create user", 500)

@router.get("/", response_model=dict)
def list_users():
    try:
        users = UserService.get_users()
        data = [u.__dict__ for u in users]
        return success_response(data, "Users fetched successfully")
    except Exception as e:
        logger.error("Error fetching users: %s", str(e))
        return error_response("Failed to fetch users", 500)

@router.get("/{user_id}", response_model=dict)
def get_user(user_id: int):
    db_user = UserService.get_user_by_id(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
