import requests
from .settings import settings


class Config:
    loaded_cloud = False  # Ngăn load lại nếu không bật AUTO_REFRESH

    def load_from_cloud(self):
        """Load config từ Cloud Config Server nếu có."""
        if not settings.CLOUD_CONFIG_URL:
            return

        if self.loaded_cloud and not settings.AUTO_REFRESH:
            return

        try:
            r = requests.get(settings.CLOUD_CONFIG_URL, timeout=3)
            if r.status_code == 200:
                sources = r.json().get("propertySources", [])
                for src in sources:
                    for k, v in src.get("source", {}).items():
                        setattr(settings, k, v)
                self.loaded_cloud = True
        except Exception as ex:
            print(f"Cloud config not loaded: {ex}")

    @property
    def DB_DSN(self) -> str:
        self.load_from_cloud()
        return f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_SERVICE}"

    @property
    def DB_CONFIG(self) -> dict:
        self.load_from_cloud()
        return {
            "user": settings.DB_USER,
            "password": settings.DB_PASS,
            "dsn": self.DB_DSN
        }


config = Config()
