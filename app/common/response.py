# app/common/response.py
from typing import Any, Dict

def success_response(data: Any, message: str = "Success") -> Dict:
    return {
        "status": "success",
        "message": message,
        "data": data
    }

def error_response(message: str = "Error", code: int = 400) -> Dict:
    return {
        "status": "error",
        "message": message,
        "code": code,
        "data": None
    }
