from .vector_store_config import collection
from .retrieval_utils import extract_keyword, if_keyword_exists

# add hashid instead of loop numbers
import hashlib


# insert/upserting
def add_documents(documents):
    batch_doc = []
    batch_metas = []
    batch_ids = []
    for doc in documents:
        doc_hash = hashlib.md5(doc["text"].encode("utf-8")).hexdigest()[:8]

        batch_doc.append(doc["text"]),
        batch_metas.append(doc["metadata"]),
        batch_ids.append(
            f"{doc['metadata']['facility_id']}_{doc['metadata']['type']}_{doc_hash}"
        ),
    if batch_ids:
        collection.upsert(
            ids=batch_ids,
            documents=batch_doc,
            metadatas=batch_metas,
        )


def add_documents_in_batch(doc_batch: list[list[dict]]):
    BATCH_SIZE = 500
    batch_doc = []
    batch_metas = []
    batch_ids = []

    for doc_list in doc_batch:
        for doc in doc_list:
            doc_hash = hashlib.md5(doc["text"].encode("utf-8")).hexdigest()[:8]

            batch_doc.append(doc["text"])
            batch_metas.append(doc["metadata"])
            batch_ids.append(
                f"{doc['metadata']['facility_id']}_{doc['metadata']['type']}_{doc_hash}"
            )
            if len(batch_ids) >= BATCH_SIZE:
                collection.upsert(
                    ids=batch_ids,
                    documents=batch_doc,
                    metadatas=batch_metas,
                )
                batch_ids.clear()
                batch_doc.clear()
                batch_metas.clear()
    if batch_ids:
        collection.upsert(
            ids=batch_ids,
            documents=batch_doc,
            metadatas=batch_metas,
        )


# querying
def query_documents(query, n_results=5, doc_type=None, dist_threshold=0.8):
    where_filter = None
    if doc_type:
        where_filter = {"type": doc_type}
    results = collection.query(
        query_texts=query, n_results=n_results, where=where_filter
    )

    extracted_keywords = extract_keyword(query)

    filtered = {"documents": [], "metadatas": [], "distances": []}

    docs = results["documents"][0]
    metas = results["metadatas"][0]
    dists = results["distances"][0]

    for doc, meta, dist in zip(docs, metas, dists):
        if dist <= dist_threshold and if_keyword_exists(doc, extracted_keywords):
            filtered["documents"].append(doc)
            filtered["metadatas"].append(meta)
            filtered["distances"].append(dist)

    return filtered


# collection utils
def count_docs():
    return collection.count()


def delete_all_chroma_docs_when_seed():
    batch_size = 1000
    while True:
        batch = collection.get(limit=batch_size)["ids"]
        if not batch:
            break
        collection.delete(ids=batch)
