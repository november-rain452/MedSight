def format_chroma_retrieval_output(output):
    docs = output["documents"]
    metas = output["metadatas"]
    distances = output["distances"]
    if not docs:
        print("No relevant results found.")
        return None
    for i in range(len(docs)):

        print(f"\nResult no: {i+1}")
        print(f"Text : {docs[i]}")
        print(f"Metadata : {metas[i]}")
        print(f"Distance : {distances[i]}")


def extract_keyword(query):
    return [word.lower() for word in query.split() if len(word) >= 3]


def if_keyword_exists(doc, query_keywords):
    doc_lower = doc.lower()
    return any(keyword in doc_lower for keyword in query_keywords)
