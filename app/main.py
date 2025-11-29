from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from app.common.exception_handler import global_exception_handler, validation_exception_handler, db_exception_handler
from app.common.exceptions import DatabaseException
from app.api.user_api import router as UserRouter

app = FastAPI(title="FastAPI User Service")

app.include_router(UserRouter, prefix="/users", tags=["Users"])

# Global exception
app.add_exception_handler(Exception, global_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(DatabaseException, db_exception_handler)
