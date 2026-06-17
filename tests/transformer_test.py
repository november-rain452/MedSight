import pandas as pd
from src.ingest import transformer
from src.ingest.processors import facility_to_documents

df = pd.read_csv("src/data/virtue foundation ghana.csv")

row = df.iloc[0].to_dict()

facility = transformer.transform_row(row)
documents = facility_to_documents(facility)

print(documents)
