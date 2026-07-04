from fastapi import APIRouter
from .endpoints.ingest_router import router as ingest_router

api_router = APIRouter()
api_router.include_router(ingest_router)
