from ..database.vectors.vector_store import add_documents_in_batch


def ingest_vector_db(vector_batch):
    add_documents_in_batch(vector_batch)
