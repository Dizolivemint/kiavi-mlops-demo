import pandas as pd
from sklearn.linear_model import LinearRegression
import mlflow

def train():
    df = pd.read_csv("data/properties.csv")
    X = df[["sqft", "year_built"]]
    y = df["price"]
    
    model = LinearRegression()
    model.fit(X, y)

    mlflow.start_run()
    mlflow.log_param("features", ["sqft", "year_built"])
    mlflow.sklearn.log_model(model, "model")
    mlflow.end_run()

if __name__ == "__main__":
    train()
