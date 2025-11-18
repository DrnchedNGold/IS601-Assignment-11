from app.models.calculation import Base
from app.models.user import User  # Ensure User table is registered
from app.database import engine

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Database tables created.")
