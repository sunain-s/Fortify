from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import Depends

SQLALCHEMY_DATABASE_URL = "sqlite:///./fortify.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={}, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
