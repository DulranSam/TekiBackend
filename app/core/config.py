from pydantic import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "am-backend-auth-secret" # replace or load from env
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str = "sqlite:///./test.db"

    class Config:
        env_file = ".env"

settings = Settings()

