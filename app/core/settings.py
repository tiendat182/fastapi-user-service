from pydantic_settings import BaseSettings
import os

mode = os.getenv("ENV_MODE", "dev")  # default dev

class Settings(BaseSettings):
    # App
    APP_NAME: str = "fastapi-user-service"
    APP_PORT: int = 8000

    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int
    DB_SERVICE: str

    # Cloud Config
    CLOUD_CONFIG_URL: str | None = None
    AUTO_REFRESH: bool = False

    class Config:
        env_file = f".env.{mode}"
        env_file_encoding = "utf-8"
        extra = "allow"

settings = Settings()
