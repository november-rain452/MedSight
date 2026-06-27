import pandas as pd

DATA_PATH = "src/data/virtue foundation ghana.csv"


def load_csv():
    try:
        return pd.read_csv(DATA_PATH)
    except FileNotFoundError:
        print("File not found")
        return None
