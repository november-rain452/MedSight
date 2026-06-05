def clean_text(text):
    return text.replace("  ", " ".strip())


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
        text = f"Facility : {name}. Capabilities include : {', '.join(facility["capability"])}"
        docs.append(
            {
                "text": clean_text(text),
                "metadata": {"facility_id": fid, "type": "capability"},
            }
        )

    if facility.get("description"):
        text = f"Facility : {name}. Description : {facility["description"]}"
        docs.append(
            {
                "text": clean_text(text),
                "metadata": {"facility_id": fid, "type": "description"},
            }
        )
    return docs
