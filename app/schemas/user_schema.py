# app/schemas/user_schema.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    fullname: Optional[str] = None

class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr
    fullname: Optional[str] = None
    created_at: datetime
    class Config:
        orm_mode = True
