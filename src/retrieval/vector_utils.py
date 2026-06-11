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
