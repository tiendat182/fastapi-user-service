from typing import List

from app.common.exceptions import DatabaseException
from app.core.database import get_connection
from app.models.user import User
from app.schemas.user_schema import UserCreate
from app.common.db_helper import fetch_all, fetch_one, execute

class UserService:

    @staticmethod
    def create_user(user: UserCreate) -> User:
        sql = """
        INSERT INTO USERS (USERNAME, EMAIL, FULLNAME)
        VALUES (:username, :email, :fullname)
        """
        execute(sql, {"username": user.username, "email": user.email, "fullname": user.fullname})
        # Trả về object vừa tạo (có thể select lại nếu cần id)
        return user

    @staticmethod
    def get_users():
        sql = "SELECT ID, USERNAME, EMAIL, FULLNAME, CREATED_AT FROM USERS"
        return fetch_all(sql, User)

    @staticmethod
    def get_user_by_id(user_id: int):
        sql = f"SELECT ID, USERNAME, EMAIL, FULLNAME, CREATED_AT FROM USERS WHERE ID={user_id}"
        user = fetch_one(sql, User)
        if not user:
            raise DatabaseException(f"User {user_id} not found")
        return user

    @staticmethod
    def update_user(user_id: int, user: UserCreate) -> User:
        """
        Cập nhật user theo ID
        """
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE USERS SET USERNAME=:username, EMAIL=:email, FULLNAME=:fullname
                WHERE ID=:id
                """,
                {"username": user.username, "email": user.email, "fullname": user.fullname, "id": user_id}
            )
            conn.commit()
            cursor.close()
        return User(id=user_id, username=user.username, email=user.email, fullname=user.fullname)

    @staticmethod
    def delete_user(user_id: int):
        """
        Xóa user theo ID
        """
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM USERS WHERE ID=:id", {"id": user_id})
            conn.commit()
            cursor.close()
