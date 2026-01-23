from data_loader import load_walmart_data

DATA_PATH = "data/raw/walmart_sales.csv"

def preprocess_data(store_id: int = 1):
    """
    Cleans and prepares Walmart data for modeling.
    """
    df = load_walmart_data(DATA_PATH)

    # Filter single store
    df = df[df["Store"] == store_id]

    # Sort by date (important for time-series)
    df = df.sort_values("Date")

    # Handle missing values in markdown columns
    markdown_cols = [
        "MarkDown1", "MarkDown2", "MarkDown3", "MarkDown4", "MarkDown5"
    ]
    df[markdown_cols] = df[markdown_cols].fillna(0)

    return df


if __name__ == "__main__":
    df = preprocess_data()
    print(df.isnull().sum())
    print(df.head())
