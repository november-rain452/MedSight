import pandas as pd
from src.retrieval.vector_store import add_documents, count_docs, query_documents
from src.utils import transformer, formatter
from src.ingest.processors import facility_to_documents
from src.database.vectors.vector_store_config import collection

df = pd.read_csv("databricks/Virtue Foundation Ghana v0.3 - Sheet1.csv")
# for i in range(2):
#     row = df.iloc[i].to_dict()
#     facility = transformer.transform_row(row)
#     document = facility_to_documents(facility)
#     add_documents(document)

query = "HIV outreach programs"
output = query_documents(query)
result = formatter.format_chroma_retrieval_output(output)
print(result)
