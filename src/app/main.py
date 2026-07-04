from fastapi import FastAPI
from src.database.sql.config.sql_database import Base, engine
from ..database.sql.models.model import Facility
from .api.v1.router import api_router

app = FastAPI()
app.include_router(api_router)
Base.metadata.create_all(bind=engine)
