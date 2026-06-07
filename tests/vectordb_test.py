import pandas as pd
from src.database.vectors.vector_store import add_documents
from src.utils.transformer import transform_row
from src.ingest.processors import facility_to_documents
from src.database.vectors.vector_store_config import collection

df = pd.read_csv("databricks/Virtue Foundation Ghana v0.3 - Sheet1.csv")
for i in range(2):
    row = df.iloc[i].to_dict()
    facility = transform_row(row)
    document = facility_to_documents(facility)
    add_documents(document)

result = collection.query(query_texts="chartered bank", n_results=2)
print(result)
