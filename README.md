# End-to-End Crypto Data Pipeline (Airflow + Docker + PostgreSQL)

## 📌 Overview

This project implements an end-to-end data engineering pipeline that ingests, processes, and stores real-time cryptocurrency market data.

The pipeline extracts data from the CoinGecko API, transforms it using Python, and loads it into a PostgreSQL database. Workflow orchestration is managed using Apache Airflow, and the entire system runs in a containerized environment using Docker.

This project simulates a production-style ETL workflow with automated scheduling and scalable infrastructure.

---

## 📌 Architecture

CoinGecko API → Python (ETL) → PostgreSQL → Airflow → BI Tools

---

## ⚙️ Tech Stack

* Python (pandas, requests, SQLAlchemy)
* Apache Airflow (DAGs, scheduling)
* PostgreSQL
* Docker & Docker Compose
* Power BI (optional)

---

## 🔄 Pipeline Workflow

### 1. Data Ingestion (Extract)

* Fetches real-time cryptocurrency data from CoinGecko API
* Retrieves metrics such as price, market cap, and volume

### 2. Data Transformation (Transform)

* Converts JSON data into a pandas DataFrame
* Selects relevant columns and renames fields for consistency

### 3. Data Storage (Load)

* Loads structured data into PostgreSQL
* Uses append strategy for incremental data storage

### 4. Workflow Orchestration

* Apache Airflow DAG schedules and executes the ETL process hourly
* Uses PythonOperator to trigger the pipeline functions

---

## 📁 Project Structure

airflow-crypto-pipeline/
│
├── dags/
│   └── crypto_dag.py
│
├── pipeline.py
├── docker-compose.yaml
├── requirements.txt
└── README.md

---

## 🧠 ETL Implementation

The ETL pipeline is implemented in a single Python module:

* extract_data() → retrieves API data
* transform_data() → processes and cleans data
* load_data() → stores data in PostgreSQL
* run_pipeline() → orchestrates the ETL steps

The Airflow DAG imports these functions and executes them as a scheduled workflow.

---

## ▶️ How to Run

### 1. Clone the repository

git clone <your-repo-url>
cd airflow-crypto-pipeline

### 2. Start services

docker compose up --build

### 3. Access Airflow

http://localhost:8080

* Username: airflow
* Password: airflow

### 4. Run the pipeline

* Enable DAG: crypto_pipeline
* Trigger manually or wait for scheduled run (@hourly)

---

## 📊 Output

* Data is stored in PostgreSQL table: crypto_prices
* Includes:

  * coin_id
  * symbol
  * name
  * price
  * market_cap
  * total_volume

---

## 🔑 Key Features

* Automated ETL pipeline using Apache Airflow
* Real-time data ingestion from CoinGecko API
* Data transformation using pandas
* PostgreSQL data storage
* Containerized architecture with Docker
* Scheduled execution (@hourly)

---

## 🚀 Future Improvements

* Refactor pipeline into modular components (extract / transform / load)
* Add data validation and logging
* Connect to Power BI for visualization
* Deploy to cloud (AWS/GCP)
* Add machine learning model for price prediction

---

## 🧠 What This Project Demonstrates

* ETL pipeline development
* API integration
* Workflow orchestration with Airflow
* Containerized data infrastructure
* Data readiness for analytics and BI

---

## 📬 Contact

Open to opportunities in Data Engineering, Data Science, and Analytics.
