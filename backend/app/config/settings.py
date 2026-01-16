from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str

    snowflake_account: str
    snowflake_user: str
    snowflake_password: str
    snowflake_warehouse: str
    snowflake_database: str
    snowflake_schema: str
    snowflake_role: str

    class Config:
        env_file = ".env"

settings = Settings()
