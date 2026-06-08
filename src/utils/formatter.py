def format_chroma_retrieval_output(output):
    docs = output["documents"][0]
    metas = output["metadatas"][0]
    distances = output["distances"][0]
    for i in range(len(docs)):

        print(f"\nResult no: {i+1}")
        print(f"Text : {docs[i]}")
        print(f"Metadata : {metas[i]}")
        print(f"Distance : {distances[i]}")
