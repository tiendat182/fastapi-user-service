# app/common/logger.py
import logging
from logging.handlers import RotatingFileHandler
import sys

# Tạo logger
logger = logging.getLogger("user_service")
logger.setLevel(logging.INFO)  # có thể DEBUG khi dev

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
console_handler.setFormatter(console_formatter)

# File handler (log xoay vòng)
file_handler = RotatingFileHandler("logs/app.log", maxBytes=5*1024*1024, backupCount=5)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(console_formatter)

# Thêm handler vào logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
