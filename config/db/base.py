from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from config.settings import DATABASES

# PostgreSQL connection string
POSTGRES_USER = DATABASES['default']['DATABASE_USER']
POSTGRES_PASSWORD = DATABASES['default']['DATABASE_PASSWORD']
POSTGRES_DB = DATABASES['default']['DATABASE_NAME']
POSTGRES_HOST = DATABASES['default']['DATABASE_HOST']
POSTGRES_PORT = DATABASES['default']['DATABASE_PORT']

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
