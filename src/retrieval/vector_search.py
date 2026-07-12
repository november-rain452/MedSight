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


def retrieve_vectors(parsed_query: dict):

    query_types = set()

    for types in TYPE_SET:
        if types in parsed_query:
            query_types.append(types)

    query = f""
