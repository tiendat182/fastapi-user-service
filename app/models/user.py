from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: int
    username: str
    email: str | None = None
    fullname: str | None = None
    created_at: datetime | None = None

    @classmethod
    def from_row(cls, row):
        return cls(
            id=row[0],
            username=row[1],
            email=row[2],
            fullname=row[3],
            created_at=row[4]
        )
