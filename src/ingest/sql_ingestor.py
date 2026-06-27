from ..database.SQL.services.internal_services import insert_in_batch_service


def ingest_sql_db(sql_batch: list[dict]):
    insert_in_batch_service(sql_batch)
