# Import libraries
import requests
import pandas as pd
from sqlalchemy import create_engine # function from SQLAlchemy used to create a connection to SQL databases.

# DB Connection
DB_URI = "postgresql://airflow:airflow@postgres:5432/airflow"

# Extract
def extract_data():
    url = "https://api.coingecko.com/api/v3/coins/markets" # CoinGecko API endpoint -> /coins/markets returns cryptocurrency market data
    params = {
        "vs_currency": "usd", # base currency for prices (will be returned in USD)
        "order": "market_cap_desc", # sort cryptocurrencies by descending market capitalization
        "per_page": 5, # only the top 5 coins are returned
        "page": 1
    }

    response = requests.get(url, params=params) # sends an HTTP GET request to the API
    if response.status_code != 200: # 200 = successful request
        raise Exception(f"Error API: {response.status_code}") # if the API fails (exmaple: 404 or 500), an exception is raised
    return response.json() # converts the JSON response into python data structures (lists/dictionaries).

# Transform
def transform_data(data): # converts JSON data into a pandas DataFrame (structured table)
    df = pd.DataFrame(data)

    df = df[[ # just for the required columns
        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "total_volume"
    ]]
    
    df = df.rename(columns={ # rename to improve readability
        "id": "coin_id",
        "current_price": "price"
    })

    return df

# Load
def load_data(df):
    engine = create_engine(DB_URI) # creates a connection object for PostgreSQL
    # engine = bridge between Python and SQL
    df.to_sql("crypto_prices", engine, if_exists="append", index=False) # saves the DataFrame into PostgreSQL
    # if_exists = "append" -> inserts new rows without deleting existing data
    # index = False -> prevents pandas index from being stored as a SQL column

# Pipeline
def run_pipeline():
    print("Extrayendo datos...")
    data = extract_data()
    print("Transformando datos...")
    df = transform_data(data)
    print(df) 
    print("Guardando en DB...")
    load_data(df) # loads data into PostgreSQL
    print("Pipeline terminado")
    
if __name__ == "__main__": # entry point
    run_pipeline()
