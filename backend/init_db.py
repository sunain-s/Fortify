from databases.models import Base
from databases.database import engine

# Create all tables in the database
Base.metadata.create_all(bind=engine)

print("Database initialized successfully.")
