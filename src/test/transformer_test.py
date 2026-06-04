import pandas as pd
from core.transform import transform_row

df = pd.read_csv("your_file.csv")

row = df.iloc[0].to_dict()

facility = transform_row(row)

print(facility)
