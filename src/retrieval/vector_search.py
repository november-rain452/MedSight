from ..database.vectors.vector_store import query_documents

TYPE_SET = {"procedure", "equipment", "capability"}

FIELD_MAP = {
    "organization_type": "level facility ",
    "city": ", ",
    "country": "",
    "facility_type": "a type of ",
    "procedure": "consisting of procedures like ",
    "equipment": "has equipments such as ",
    "capability": "with capabitilies such as ",
}


# call the vector db with the query
def retrieve_vectors(
    parsed_query: dict[str, str], top_k: int = 7, threshold: float = 0.8
) -> list[list]:

    query_types = {t for t in TYPE_SET if t in parsed_query}

    query = create_query(parsed_query, query_types)

    query_results = []

    for qtype in query_types:
        result = query_documents(query, 7, qtype, 0.8)
        query_results.append(result)

    return query_results


# create a natural language vector query based on given query parameters
def create_query(parsed_query: dict, query_types: set) -> str:

    if "organization_type" in parsed_query:
        org_type = (
            f"{parsed_query['organization_type']} {FIELD_MAP['organization_type']}"
        )

    if "city" in parsed_query:
        city = f"{parsed_query['city']}{FIELD_MAP['city']}"

    if "country" in parsed_query:
        country = f"{parsed_query['country']}"

    if "facility_type" in parsed_query:
        facility_type = f"{FIELD_MAP['facility_type']} {parsed_query['facility_type']}"

    if "procedure" in query_types:
        procedure = f"{FIELD_MAP['procedure']}{parsed_query['procedure']}"

    if "equipment" in query_types:
        equipment = f"{FIELD_MAP['equipment']}{parsed_query['equipment']}"

    if "capability" in query_types:
        capability = f"{FIELD_MAP['capability']}{parsed_query['capability']}"

    query = f"{org_type} in {city}{country} which is {facility_type} {capability} {equipment} and {procedure}"
    return query
