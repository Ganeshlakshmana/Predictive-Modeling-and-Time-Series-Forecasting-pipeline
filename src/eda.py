from data_loader import load_walmart_data
from data_validation import validate_data

DATA_PATH = "data/raw/walmart_sales.csv"

df = load_walmart_data(DATA_PATH)
validate_data(df)

print("Dataset shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nMissing values:")
print(df.isnull().sum())

print("\nSample rows:")
print(df.head())
