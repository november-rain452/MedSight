from ..database.vectors.vector_store import query_documents
from ..core.logger import logger
from .models import VectorResult

TYPE_SET = {"procedure", "equipment", "capability"}

FIELD_MAP = {
    "organization_type": "facility level:",
    "city": ", ",
    "country": "",
    "facility_type": "a type of ",
    "procedure": "consisting of procedures like ",
    "equipment": "with equipment such as ",
    "capability": "with capabilities such as ",
}


# call the vector db with the query
def retrieve_vectors(
    parsed_query: dict[str, str], top_k: int = 7, threshold: float = 0.8
) -> list[VectorResult]:
    """
    Query the vector database for present query parameters

    Args:
        parsed_query: dictionary with keys like 'organization_type', 'city', etc.
        top_k: number of documents to retrieve per type.
        threshold: similarity threshold for filtering.

    Returns:
        List of results per type (each result is whatever query_documents returns).
    """

    query_types = {t for t in TYPE_SET if t in parsed_query}

    query = create_query(parsed_query, query_types)

    query_results = []

    if query_types:
        for qtype in query_types:
            try:
                query_res = query_documents(query, top_k, qtype, threshold)
                result = format_vectordb_output(query_res)

            except Exception as e:
                logger.error(f"Vector query failed for type {qtype}: {e}")
                result = []

            query_results.append(result)
    else:
        try:
            query_res = query_documents(query, top_k, None, threshold)
            result = format_vectordb_output(query_res)
            query_results.append(result)
        except Exception as e:
            logger.error(f"Vector query failed: {e}")
            result = []

    return [item for res in query_results for item in res]


# create a natural language vector query based on given query parameters
def create_query(parsed_query: dict, query_types: set) -> str:
    """
    Construct a natural language query from given parameters
    """

    parts = []

    if "organization_type" in parsed_query:
        parts.append(
            f"{FIELD_MAP['organization_type']} {parsed_query['organization_type']}"
        )

    # fusing location
    location_parts = []
    if "city" in parsed_query:
        location_parts.append(f"{parsed_query['city']}")

    if "country" in parsed_query:
        location_parts.append(f"{parsed_query['country']}")
    if location_parts:
        parts.append(("in " + ", ".join(location_parts)))

    if "facility_type" in parsed_query:
        parts.append("{FIELD_MAP['facility_type']} {parsed_query['facility_type']}")

    if "procedure" in query_types:
        parts.append(f"{FIELD_MAP['procedure']}{parsed_query['procedure']}")

    if "equipment" in query_types:
        parts.append(f"{FIELD_MAP['equipment']}{parsed_query['equipment']}")

    if "capability" in query_types:
        parts.append(f"{FIELD_MAP['capability']}{parsed_query['capability']}")

    query = " ".join(parts)
    return query


# formatting vectorDB output
def format_vectordb_output(output: dict[str, list]) -> list[VectorResult]:
    docs = output["documents"]
    metas = output["metadatas"]
    dists = output["distances"]

    results = []

    for i in range(len(docs)):
        vec_result_obj = VectorResult(
            facility_id=metas[i]["facility_id"],
            content=docs[i],
            metadata=metas[i],
            distance=dists[i],
        )
        results.append(vec_result_obj)

    return results
