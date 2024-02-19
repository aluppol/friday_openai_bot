from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TELEGRAM_API_KEY: str
    WEBHOOK_URL: str

    class Config:
        env_file = ".env"


settings = Settings()
