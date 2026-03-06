# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from motor.motor_asyncio import AsyncIOMotorClient

DATABASE_URL = "postgresql://bookuser:bookpass@localhost:5432/bookdb"


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


mongodb_url = "mongodb://admin:password@localhost:27017"

from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(mongodb_url)
db = client.fastapi


books_collection = db.books


async def mongo_db():
    return db