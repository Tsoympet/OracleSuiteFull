import os

class Settings:
    ENV: str = os.getenv("ENV", "dev")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://oracle:oracle@db:5432/oracle_suite")

settings = Settings()
