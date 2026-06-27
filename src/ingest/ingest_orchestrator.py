from .csv_loader import load_csv
from .sql_ingestor import ingest_sql_db
from .vector_ingestor import ingest_vector_db
from .transformer import transform_row
from .processors import facility_to_documents


def ingest_orchestrator_func():
    df = load_csv()
    sql_batch = []
    vector_batch = []

    for row in df.itertuples(index=False):
        transformed_facility = transform_row(row)
        rag_document = facility_to_documents(transformed_facility)
        sql_batch.append(transformed_facility)
        vector_batch.append(rag_document)

    ingest_sql_db(sql_batch)
    ingest_vector_db(vector_batch)
