import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    data = pd.read_csv("data/raw/IRIS.csv")
    return data
