import oracledb
from contextlib import contextmanager
from app.core.config import settings  # nơi bạn để DB_USER, DB_PASSWORD, DB_DSN

# Nếu muốn pool connection, oracledb cũng hỗ trợ
pool = oracledb.create_pool(
    user=settings.DB_USER,
    password=settings.DB_PASSWORD,
    dsn=settings.DB_DSN,       # ví dụ "localhost:1521/XE"
    min=2,
    max=10,
    increment=1,
    encoding="UTF-8"
)

@contextmanager
def get_connection():
    """
    Context manager trả về connection Oracle DB.
    Sử dụng 'with get_connection() as conn:' sẽ tự động release.
    """
    conn = pool.acquire()  # lấy connection từ pool
    try:
        yield conn
    finally:
        pool.release(conn)  # trả connection về pool
