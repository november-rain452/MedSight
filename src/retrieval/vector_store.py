from ..database.vectors.vector_store_config import collection

# add hashid instead of loop numbers
import hashlib


def add_documents(documents):
    batch_doc = []
    batch_metas = []
    batch_ids = []
    for doc in documents:
        hash = hashlib.md5(doc["text"].encode("utf-8")).hexdigest()[:8]

        batch_doc.append(doc["text"]),
        batch_metas.append(doc["metadata"]),
        batch_ids.append(
            f"{doc['metadata']['facility_id']}_{doc['metadata']['type']}_{hash}"
        ),
    if batch_ids:
        collection.upsert(
            ids=batch_ids,
            documents=batch_doc,
            metadatas=batch_metas,
        )


def query_documents(query, n_results=5, doc_type=None):
    where_filter = None
    if doc_type:
        where_filter = {"type": doc_type}
    results = collection.query(
        query_texts=query, n_results=n_results, where=where_filter
    )
    return results


def count_docs():
    return collection.count()
