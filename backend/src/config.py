"""Config file for fastapi settings"""

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    """General config"""

    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8080


settings = Config()
