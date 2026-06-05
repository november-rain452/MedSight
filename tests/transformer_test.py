import pandas as pd
from src.utils import transformer
from src.ingest.processors import facility_to_documents

df = pd.read_csv("databricks/Virtue Foundation Ghana v0.3 - Sheet1.csv")

row = df.iloc[0].to_dict()

facility = transformer.transform_row(row)
documents = facility_to_documents(facility)

print(documents)
