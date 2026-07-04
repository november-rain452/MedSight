from .csv_loader import load_csv
from .sql_ingestor import ingest_sql_db
from .vector_ingestor import ingest_vector_db
from .transformer import transform_row, transform_row_to_facility
from .processors import facility_to_documents
from ..retrieval.vector_store import delete_all_chroma_docs_when_seed


def ingest_orchestrator_func():
    df = load_csv()
    sql_batch = []
    vector_batch = []

    for row in df.itertuples(index=False):
        transformed_facility = transform_row(row)
        rag_document = facility_to_documents(transformed_facility)
        sql_facility = transform_row_to_facility(transformed_facility)
        sql_batch.append(sql_facility)
        vector_batch.append(rag_document)
    try:
        ingest_vector_db(vector_batch)
        ingest_sql_db(sql_batch)
    except:
        delete_all_chroma_docs_when_seed()
        raise
