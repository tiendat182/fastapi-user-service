# app/models/user.py
from datetime import datetime

class User:
    def __init__(self, id, username, email, fullname, created_at):
        self.id = id
        self.username = username
        self.email = email
        self.fullname = fullname
        self.created_at = created_at

    @classmethod
    def from_row(cls, row):
        return cls(
            id=row[0],
            username=row[1],
            email=row[2],
            fullname=row[3],
            created_at=row[4]
        )
