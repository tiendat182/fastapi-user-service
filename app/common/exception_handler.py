# app/common/exception_handler.py
from fastapi import Request
from fastapi.responses import JSONResponse

from app.common.exceptions import DatabaseException
from app.common.response import error_response
from app.common.logger import logger
from pydantic import ValidationError

async def global_exception_handler(request: Request, exc: Exception):
    """
    Bắt tất cả exception chưa được xử lý
    """
    logger.error("Unhandled error: %s", str(exc))
    return JSONResponse(
        status_code=500,
        content=error_response("Internal server error")
    )

async def validation_exception_handler(request: Request, exc: ValidationError):
    """
    Bắt validation error từ Pydantic
    """
    logger.warning("Validation error: %s", exc.errors())
    return JSONResponse(
        status_code=422,
        content=error_response("Validation error")
    )

# Bắt DatabaseException
async def db_exception_handler(request: Request, exc: DatabaseException):
    logger.error("Database error: %s", exc.message)
    return JSONResponse(
        status_code=exc.code,
        content=error_response(exc.message, exc.code)
    )
