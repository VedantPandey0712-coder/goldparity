from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "postgresql+psycopg://goldparity:goldparity@localhost:5432/goldparity"
    cors_origins: list[str] = ["http://localhost:3000"]


settings = Settings()
