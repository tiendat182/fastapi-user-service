import oracledb
from contextlib import contextmanager
from app.core.config import settings, config  # nơi bạn để DB_USER, DB_PASS, DB_DSN

cfg = config.DB_CONFIG
pool = oracledb.create_pool(
    user=cfg["user"],
    password=cfg["password"],
    dsn=cfg["dsn"],
    min=2,
    max=5,
    increment=1
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
