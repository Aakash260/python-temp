from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config.setting import settings

DATABASE_URL = settings.DATABASE_URL
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def connect_db():
    try:
        connection = engine.connect()
        print("Database connected successfully")
        connection.close()
    except Exception as e:
        print("Database connection failed:", e)