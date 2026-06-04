import pandas as pd
from src.utils import transformer

df = pd.read_csv("databricks/Virtue Foundation Ghana v0.3 - Sheet1.csv")

row = df.iloc[1].to_dict()

facility = transformer.transform_row(row)

print(facility)
