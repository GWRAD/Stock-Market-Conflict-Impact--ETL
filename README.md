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

### 1. Clone the Repository

```bash
git clone https://github.com/GWRAD/Stock-Market-Conflict-Impact--ETL.git
cd stock-conflict-airflow-pipeline
```

---

### 2. Setup Apache Airflow Using Docker

Make sure you have Docker Desktop installed.

```bash
curl -LfO https://airflow.apache.org/docs/apache-airflow/2.8.2/docker-compose.yaml
mkdir -p dags logs plugins
echo "AIRFLOW_UID=50000" > .env
```

Start Airflow:

```bash
docker compose up airflow-init
docker compose up
```

---

### 3. Open Airflow UI

Once all containers are up, access the Airflow UI at:

[http://localhost:8080](http://localhost:8080)

- **Username**: `airflow`  
- **Password**: `airflow`

Enable the `stock_etl_cof` DAG from the dashboard to start the daily pipeline.
<img width="956" alt="image" src="https://github.com/user-attachments/assets/b9eb0bd7-f6cc-45d3-913c-16f1ff079107" />

---

### 4. Check Generated Files

After the DAG runs, check the `event_windows/` folder.  
You’ll find files like:

```
COF_Iran_Israel_War_2025.csv  
JPM_India_Pakistan_Sinddor_2025.csv  
```

These contain ±5-day stock price windows around each selected conflict.

---

### 5. Open Power BI Report

1. Open `PowerBI_Report.pbix`  
2. Make sure the folder path to `event_windows/` is set correctly  
3. Click `Home > Refresh` to load new data

---

## 🎯 Dashboard Insights

The Power BI report includes:

- 📌 **Conflict Timeline Slicer**
- 📌 **Sector Filter (Banking / Defense / Energy)**
- 📈 **Stock Price Trend During Conflict**
- 📊 **Latest Market Close vs Conflict Period Close**
- 🧮 **20-Day and 50-Day Moving Average Table**
- 💰 **Latest Closing Price Bar Chart**


<img width="718" alt="image" src="https://github.com/user-attachments/assets/379972c5-ca9c-4c2f-9a9d-55cd0f8d04b9" />
<img width="718" alt="image" src="https://github.com/user-attachments/assets/1bf50e95-4819-4d33-9088-f1934124f43e" />
<img width="721" alt="image" src="https://github.com/user-attachments/assets/26ce813a-32ff-4a35-88e9-61c3a70f9229" />



---

## ✅ Done!

You now have a live dashboard analyzing the impact of global conflicts on key sector stocks using:

- **Automated ETL with Airflow**  
- **Historical financial data from Yahoo Finance**  
- **Visual storytelling in Power BI**

---


