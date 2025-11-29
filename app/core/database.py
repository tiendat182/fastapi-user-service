# app/core/database.py
import oracledb
from .config import settings

def get_connection():
    return oracledb.connect(
        user=settings.DB_USER,
        password=settings.DB_PASS,
        dsn=settings.DB_DSN
    )
