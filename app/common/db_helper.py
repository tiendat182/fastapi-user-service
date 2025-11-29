from contextlib import contextmanager
from app.core.database import get_connection
from app.common.exceptions import DatabaseException

def fetch_all(sql: str, model_class):
    """
    Thực thi SQL SELECT và convert kết quả thành list Pydantic/Entity object
    model_class: class User, Product, ...
    """
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            cursor.close()
        return [model_class.from_row(row) for row in rows]
    except Exception as e:
        raise DatabaseException(f"Failed to fetch data: {str(e)}")

def fetch_one(sql: str, model_class):
    """
    Thực thi SQL SELECT 1 bản ghi
    """
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            row = cursor.fetchone()
            cursor.close()
        if not row:
            return None
        return model_class.from_row(row)
    except Exception as e:
        raise DatabaseException(f"Failed to fetch data: {str(e)}")

def execute(sql: str, params: dict = None):
    """
    Thực thi INSERT/UPDATE/DELETE, trả về commit tự động
    """
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            conn.commit()
            cursor.close()
    except Exception as e:
        raise DatabaseException(f"Failed to execute SQL: {str(e)}")
