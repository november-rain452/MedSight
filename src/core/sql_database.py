from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from .config import MYSQL_DATABASE_URL

# engine
engine = create_engine(MYSQL_DATABASE_URL, echo=True)

# factory
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()  # <-- Automatically roll back on errors
        raise
    finally:
        db.close()
