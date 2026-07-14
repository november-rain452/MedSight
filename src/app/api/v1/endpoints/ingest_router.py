from fastapi import APIRouter, BackgroundTasks
from src.ingest.ingest_orchestrator import ingest_orchestrator_func
from src.core.logger import logger

router = APIRouter(prefix="/ingest", tags=["Ingest"])


@router.post("/seed-db", status_code=202)
def seed_ingest_endpoint(background_tasks: BackgroundTasks):
    """
    Triggers the database seeding process in the background.
    """
    background_tasks.add_task(ingest_orchestrator_func)
    logger.info("Database seeding started")

    return {
        "status": "accepted",
        "message": "Database seeding sequence initiated in the background.",
    }
