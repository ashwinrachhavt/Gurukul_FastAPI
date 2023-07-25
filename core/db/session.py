from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core import settings

engine = create_engine(settings.POSTGRES_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
