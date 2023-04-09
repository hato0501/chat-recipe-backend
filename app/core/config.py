from pydantic import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Recipe Chat App"
    BACKEND_CORS_ORIGINS: list[str] = ["*"]
    OPENAI_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()