import pandas as pd
from utils.transformer import transform_row

df = pd.read_csv("your_file.csv")

row = df.iloc[0].to_dict()

facility = transform_row(row)

print(facility)
