from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from app.common.exception_handler import (
    global_exception_handler,
    validation_exception_handler,
    db_exception_handler
)
from app.common.exceptions import DatabaseException
from app.api.user_api import router as UserRouter

app = FastAPI(title="FastAPI User Service")

# include routers
app.include_router(UserRouter, prefix="/users", tags=["Users"])

# Global exception handlers
app.add_exception_handler(Exception, global_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(DatabaseException, db_exception_handler)

# uvicorn run
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",  # module:app
        host="0.0.0.0",
        port=8000,
        reload=True,      # auto reload khi thay đổi code
    )
