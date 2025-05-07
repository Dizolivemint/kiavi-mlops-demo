
import pandas as pd
import numpy as np
import mlflow
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load data
df = pd.read_csv("data/properties.csv")

# Define different parameter sets dynamically
feature_sets = [
    ["sqft"],
    ["sqft", "year_built"],
    ["sqft", "zipcode"],
    ["sqft", "year_built", "zipcode"]
]

# Encode zipcode as numeric for simplicity
df["zipcode"] = df["zipcode"].astype("category").cat.codes

# Run multiple experiments
for features in feature_sets:
    X = df[features]
    y = df["price"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    
    mse = mean_squared_error(y_test, preds)
    r2 = r2_score(y_test, preds)

    with mlflow.start_run():
        mlflow.log_param("features_used", ", ".join(features))
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("r2_score", r2)
        mlflow.sklearn.log_model(model, "model")
        print(f"Logged run with features: {features} -> MSE: {mse:.2f}, R²: {r2:.2f}")
