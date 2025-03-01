import os
from dotenv import load_dotenv  # For loading .env file
from sqlalchemy.engine import create_engine
from sqlalchemy.sql import text  # Import text() to execute raw SQL queries

# Load environment variables from a .env file
load_dotenv()

# Read values from environment variables
DB_USER = os.getenv("DB_USER", "root")  # Default to "root" if not set
DB_PASSWORD = os.getenv("DB_PASSWORD", "root")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "car_rental")

class Config:
    # MySQL connection string (without database for initial check)
    DB_URI_WITHOUT_DB = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/"

    # MySQL connection string (with database)
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Create database if it doesn't exist
    engine = create_engine(DB_URI_WITHOUT_DB)
    with engine.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))  # Use text() here
        conn.execute(text("COMMIT"))  # Ensure changes are saved
