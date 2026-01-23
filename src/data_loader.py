import pandas as pd

def load_walmart_data(path: str) -> pd.DataFrame:
    """
    Loads Walmart sales dataset and parses date column.
    """
    df = pd.read_csv(path)
    df["Date"] = pd.to_datetime(df["Date"])
    return df
