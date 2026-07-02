from fastapi import FastAPI
from ..database.sql.config.sql_database import Base, engine
from ..database.sql.models.model import Facility

app = FastAPI()
Base.metadata.create_all(bind=engine)
