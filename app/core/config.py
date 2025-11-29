from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings
    """

    # App settings
    APP_NAME: str = "Enana Image Generation API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # Server settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # Log settings
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # Image generation settings
    DEFAULT_IMAGE_SCALE: float = 1.0
    MAX_IMAGE_WIDTH: int = 4096
    MAX_IMAGE_HEIGHT: int = 4096

    # Security settings
    API_TOKEN: str = (
        "default_token"  # Default token, should be set via environment variable
    )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


# Create settings instance
settings = Settings()
