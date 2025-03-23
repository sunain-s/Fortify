# init_db.py
from databases.database import engine
from databases.models import Base

Base.metadata.create_all(bind=engine)
print("Database tables created successfully.")
