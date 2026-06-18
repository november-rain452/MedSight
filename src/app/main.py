from fastapi import FastAPI
from ..core.sql_database import Base, engine
from ..database.SQL.models.model import Facility, Freeform

app = FastAPI()
Base.metadata.create_all(bind=engine)
