import pandas as pd
from src.ingest import transformer
from src.retrieval.retrieval_utils import format_chroma_retrieval_output
from src.retrieval.vector_store import add_documents, count_docs, query_documents
from src.ingest.processors import facility_to_documents
from src.database.vectors.vector_store_config import collection

# df = pd.read_csv("src/data/virtue foundation ghana.csv")
# for i in range(10):
#     row = df.iloc[i].to_dict()
#     facility = transformer.transform_row(row)
#     document = facility_to_documents(facility)
#     add_documents(document)

query = "HIV research"
output = query_documents(query, n_results=5, doc_type="capability", dist_threshold=0.8)
format_chroma_retrieval_output(output)
print(count_docs())
