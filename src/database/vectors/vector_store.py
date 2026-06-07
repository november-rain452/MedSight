from vector_store_config import collection


def add_documents(documents):
    for i, doc in enumerate(documents):
        collection.add(
            docs=[doc["text"]],
            metadatas=[doc["metadata"]],
            ids=[f"{doc['metadata']['facility_id']}_{doc['metadata'['type']]}_{i}"],
        )
