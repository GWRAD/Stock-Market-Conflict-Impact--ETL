# 📊 Stock Market Conflict Impact Pipeline

This project tracks and visualizes how major global conflicts influence stock prices of key companies across the **Banking**, **Defense**, and **Energy** sectors.

We use **Apache Airflow** (via Docker) to schedule a daily pipeline that fetches stock data using Yahoo Finance and extracts relevant slices around specific events. The data is then visualized in **Power BI**.

---

## 🚀 Technologies Used

| Tool / Tech       | Purpose                                        |
|-------------------|------------------------------------------------|
| Python            | Data collection and transformation logic       |
| yfinance          | API for pulling stock data from Yahoo Finance |
| Pandas            | Compute moving averages, volatility, returns   |
| Apache Airflow    | DAG orchestration for daily runs               |
| Docker            | Containerized Airflow setup                    |
| Power BI          | Dashboard visualization                        |

---

## ✅ Steps to Run This Project

# 1. Clone the Repository

```bash
git clone https://github.com/GWRAD/Stock-Market-Conflict-Impact--ETL.git
cd stock-conflict-airflow-pipeline

# 2. Setup Apache Airflow Using Docker
Make sure you have Docker Desktop installed.
curl -LfO https://airflow.apache.org/docs/apache-airflow/2.8.2/docker-compose.yaml
mkdir -p dags logs plugins
echo "AIRFLOW_UID=50000" > .env

Start Airflow:
docker compose up airflow-init
docker compose up


