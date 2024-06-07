import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    POSTGRES_USER = os.environ["POSTGRES_USER"]
    POSTGREST_PASSWORD = os.environ["POSTGRES_PASSWORD"]
    POSTGRES_DB = os.environ["POSTGRES_DB"]
    DB_HOST = os.environ.get("DB_HOST", "postgres")
    DB_PORT = os.environ.get("DB_HOST", "5432")
    DB_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGREST_PASSWORD}@{DB_HOST}:{DB_PORT}/{POSTGRES_DB}"
    # AUTH
    SECRET_KEY = os.environ.get("SECRET_KEY")
    ALGORITHM = os.environ.get("AGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRES_MINUTES = 30


settings = Settings()
