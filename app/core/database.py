import oracledb
from app.core.config import config, settings

pool = None  # khởi tạo rỗng trước

def init_db():
    global pool
    if pool is None:  # tránh tạo nhiều lần
        pool = oracledb.create_pool(
            user=settings.DB_USER,
            password=settings.DB_PASS,
            dsn=config.DB_DSN,
            min=1, max=5, increment=1
        )
    return pool

def get_connection():
    if pool is None:
        init_db()
    return pool.acquire()
