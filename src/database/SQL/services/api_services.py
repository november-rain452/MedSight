from ..config.sql_database import SessionLocal
from ..repository.api_repository import execute_statement_repository


def execute_statement_service(stmt):
    with SessionLocal() as db:
        facilities = execute_statement_repository(db, stmt)
        return facilities
