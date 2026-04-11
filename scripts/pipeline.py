import requests
import pandas as pd
from sqlalchemy import create_engine

# 🔌 conexión DB
DB_URI = "postgresql://airflow:airflow@postgres:5432/airflow"


# 🔹 EXTRACT
def extract_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 5,
        "page": 1
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(f"Error API: {response.status_code}")

    return response.json()


# 🔹 TRANSFORM
def transform_data(data):
    df = pd.DataFrame(data)

    df = df[[
        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "total_volume"
    ]]

    df = df.rename(columns={
        "id": "coin_id",
        "current_price": "price"
    })

    return df


# 🔹 LOAD
def load_data(df):
    engine = create_engine(DB_URI)

    df.to_sql("crypto_prices", engine, if_exists="append", index=False)


# 🔥 PIPELINE
def run_pipeline():
    print("🚀 Extrayendo datos...")
    data = extract_data()

    print("🔄 Transformando datos...")
    df = transform_data(data)

    print(df)  # 👈 para que veas la tabla

    print("💾 Guardando en DB...")
    load_data(df)

    print("✅ Pipeline terminado")


if __name__ == "__main__":
    run_pipeline()
