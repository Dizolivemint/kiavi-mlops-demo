import pandas as pd
import duckdb

def save_features(df, db_path="features.db"):
    con = duckdb.connect(db_path)
    con.execute("CREATE TABLE IF NOT EXISTS features AS SELECT * FROM df")
    con.close()

def load_features(db_path="features.db"):
    con = duckdb.connect(db_path)
    df = con.execute("SELECT * FROM features").fetchdf()
    con.close()
    return df
