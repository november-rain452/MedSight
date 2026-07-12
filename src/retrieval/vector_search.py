TYPE_ARRAY = ["procedure", "equipment", "capability"]


def retrieve_vectors(parsed_query: dict):

    query_types = []

    for types in TYPE_ARRAY:
        if types in parsed_query:
            query_types.append(types)

    query = f""
