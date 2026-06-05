def facility_to_documents(facility: dict) -> list[dict]:
    """Creates a document out of facilities to store for RAG/Retrieval"""

    docs = []
    fid = facility["id"]
    name = facility.get("name", "Unknown Facility")

    if facility.get("procedure"):
        docs.append(
            {
                "text": f'{name} performs: {", ".join(facility["procedure"])}',
                "metadata": {"facility_id": fid, "type": "procedure"},
            }
        )

    if facility.get("equipment"):
        docs.append(
            {
                "text": f'{name} has {", ".join(facility["equipment"])} equipment',
                "metadata": {"facility_id": fid, "type": "equipment"},
            }
        )

    if facility.get("capability"):
        docs.append(
            {
                "text": f"{name}'s capabilities include : {', '.join(facility["capability"])}",
                "metadata": {"facility_id": fid, "type": "capability"},
            }
        )
