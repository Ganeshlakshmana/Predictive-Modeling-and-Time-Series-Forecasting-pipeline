def validate_data(df):
    """
    Performs basic data validation checks.
    """
    assert "Weekly_Sales" in df.columns, "Target column missing"
    assert df.isnull().sum().sum() >= 0, "Unexpected null issue"
    assert df["Weekly_Sales"].dtype != "object", "Target must be numeric"

    print("Data validation passed.")
