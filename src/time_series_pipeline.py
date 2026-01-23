from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

from preprocessing import preprocess_data
from feature_engineering import prepare_time_series_features

def run_time_series_pipeline():
    # 1. Load & preprocess data
    df = preprocess_data(store_id=1)

    # 2. Prepare time-series features
    df = prepare_time_series_features(df)

    # 3. Train-test split (time-based)
    forecast_horizon = 12  # last 12 weeks
    train = df.iloc[:-forecast_horizon]
    test = df.iloc[-forecast_horizon:]

    X_train = train[["time_index"]]
    y_train = train["Weekly_Sales"]

    X_test = test[["time_index"]]
    y_test = test["Weekly_Sales"]

    # 4. Train forecasting model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 5. Forecast
    predictions = model.predict(X_test)

    # 6. Evaluation
    mae = mean_absolute_error(y_test, predictions)

    print("Time-Series Forecasting Results")
    print("Actual Sales:", list(y_test.values))
    print("Predicted Sales:", list(predictions))
    print(f"Forecast MAE: {mae:.2f}")

if __name__ == "__main__":
    run_time_series_pipeline()
