# app/services/user_service.py
from app.core.database import get_connection
from app.models.user import User
from app.schemas.user_schema import UserCreate
from typing import List

class UserService:

    @staticmethod
    def create_user(user: UserCreate) -> User:
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
        INSERT INTO USERS (USERNAME, EMAIL, FULLNAME) 
        VALUES (:username, :email, :fullname)
        RETURNING ID INTO :id
        """
        id_var = cursor.var(int)
        cursor.execute(sql, {
            "username": user.username,
            "email": user.email,
            "fullname": user.fullname,
            "id": id_var
        })
        conn.commit()
        cursor.close()
        conn.close()
        return User(id=id_var.getvalue()[0], username=user.username,
                    email=user.email, fullname=user.fullname, created_at=None)

    @staticmethod
    def get_users() -> List[User]:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT ID, USERNAME, EMAIL, FULLNAME, CREATED_AT FROM USERS")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [User.from_row(row) for row in rows]

    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT ID, USERNAME, EMAIL, FULLNAME, CREATED_AT FROM USERS WHERE ID=:id",
                       {"id": user_id})
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return User.from_row(row)
        return None
