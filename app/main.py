from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from app.common.exception_handler import (
    global_exception_handler,
    validation_exception_handler,
    db_exception_handler
)
from app.common.exceptions import DatabaseException
from app.core.database import init_db
from app.api.user_api import router as UserRouter


app = FastAPI(title="FastAPI User Service")

# ---------------- Register Routers ----------------
app.include_router(UserRouter, prefix="/users", tags=["Users"])

# ---------------- Register Global Exception ----------------
app.add_exception_handler(Exception, global_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(DatabaseException, db_exception_handler)


# ---------------- Startup Init Oracle Pool ----------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()         # 🔥 create pool only here
    print("🚀 App started & DB connected")
    yield
    print("🛑 App shutdown")


# ---------------- Run Uvicorn ----------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
