from ..database.vectors.vector_store_config import collection

# add hashid instead of loop numbers
import hashlib


def add_documents(documents):
    for _, doc in enumerate(documents):
        hash = hashlib.md5(doc["text"].encode("utf-8")).hexdigest()[:8]
        collection.add(
            documents=[doc["text"]],
            metadatas=[doc["metadata"]],
            ids=[f"{doc['metadata']['facility_id']}_{doc['metadata']['type']}_{hash}"],
        )


def query_documents(query, n_results=5):
    results = collection.query(query_texts=query, n_results=n_results)
    return results


def count_docs():
    return collection.count()
