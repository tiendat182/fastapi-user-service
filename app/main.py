from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.config import settings
from app.api.user_api import router as UserRouter

# Lifespan: quản lý startup + shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: load config, init resources
    settings.load_from_cloud()
    print(f"Service {settings.APP_NAME} starting on port {settings.APP_PORT}...")
    yield
    # Shutdown: release resources nếu cần
    print(f"Service {settings.APP_NAME} stopping...")

# Tạo app FastAPI với lifespan
app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)

# Include router CRUD User
app.include_router(UserRouter, prefix="/users", tags=["Users"])
