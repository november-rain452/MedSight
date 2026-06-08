from ..database.vectors.vector_store_config import collection


def add_documents(documents):
    for i, doc in enumerate(documents):
        collection.add(
            documents=[doc["text"]],
            metadatas=[doc["metadata"]],
            ids=[f"{doc['metadata']['facility_id']}_{doc['metadata']['type']}_{i}"],
        )


def query_documents(query, n_results=5):
    results = collection.query(query_texts=query, n_results=n_results)
    return results


def count_docs():
    return collection.count()
