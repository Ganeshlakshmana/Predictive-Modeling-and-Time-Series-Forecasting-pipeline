from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression

from preprocessing import preprocess_data
from feature_engineering import prepare_regression_features
from evaluation import evaluate_regression

def run_regression_pipeline():
    # 1. Load and preprocess data
    df = preprocess_data(store_id=1)

    # 2. Feature engineering
    X, y = prepare_regression_features(df)

    # 3. Train-test split (no shuffle issues here)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 4. Train baseline regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 5. Predictions
    y_pred = model.predict(X_test)

    # 6. Evaluation
    metrics = evaluate_regression(y_test, y_pred)

    print("Regression Performance:")
    for k, v in metrics.items():
        print(f"{k}: {v:.2f}")

    # 7. Cross-validation (model stability)
    cv_scores = cross_val_score(
        model, X, y, cv=5, scoring="neg_mean_absolute_error"
    )

    print(f"\nCross-Validation MAE: {-cv_scores.mean():.2f}")

if __name__ == "__main__":
    run_regression_pipeline()
