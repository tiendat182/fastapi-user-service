# app/schemas/user_schema.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: str
    fullname: Optional[str] = None

class UserRead(BaseModel):
    id: int
    username: str
    email: str
    fullname: Optional[str] = None
    created_at: datetime
    class Config:
        from_attributes = True

