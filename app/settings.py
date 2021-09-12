from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite:///database.db"


settings = Settings()