# app/core/config.py
from decouple import config
import requests

class Settings:
    APP_NAME: str = config("APP_NAME", default="fastapi-user-service")
    APP_PORT: int = config("APP_PORT", default=8000, cast=int)
    DB_USER: str = config("DB_USER")
    DB_PASS: str = config("DB_PASS")
    DB_DSN: str = config("DB_DSN")
    CLOUD_CONFIG_URL: str = config("CLOUD_CONFIG_URL", default=None)
    AUTO_REFRESH: bool = config("AUTO_REFRESH", default=False, cast=bool)

    def load_from_cloud(self):
        if self.CLOUD_CONFIG_URL:
            r = requests.get(self.CLOUD_CONFIG_URL)
            if r.status_code == 200:
                cloud_conf = r.json().get("propertySources", [])
                for src in cloud_conf:
                    for k, v in src["source"].items():
                        setattr(self, k, v)

settings = Settings()
