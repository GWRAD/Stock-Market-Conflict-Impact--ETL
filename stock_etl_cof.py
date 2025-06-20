from datetime import datetime, timedelta
import os
import yfinance as yf
import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator

# ------------------------
# Define tickers and events
# ------------------------
# COF - Capital One Financial Corp. (Banking, Credit Cards)
# JPM - JPMorgan Chase & Co. (Global Investment Banking)
# XOM - Exxon Mobil Corporation (Oil & Gas/Energy)
# LMT - Lockheed Martin Corporation (Defense & Aerospace)
# Bank of America
# Citigroup
# Wells Fargo
# Boeing (Defense & Aerospace)
# Northrop Grumman
# Raytheon Technologies
# Chevron
# BP
# TotalEnergies



tickers = {
    'COF': 'Banking',
    'JPM': 'Banking',
    'BAC': 'Banking',
    'C': 'Banking',
    'WFC': 'Banking',

    'LMT': 'Defense',
    'BA': 'Defense',
    'NOC': 'Defense',
    'RTX': 'Defense',

    'XOM': 'Energy',
    'CVX': 'Energy',
    'BP': 'Energy',
    'TTE': 'Energy'
}


event_dates = {
    
    "Iran_Israel_War_2025": "2025-06-05",
    "India_Pakistan_Sinddor_2025": "2025-05-12",
    "Israel_Gaza_Escalation_2025_06_18": "2025-06-18"
}

# ------------------------
# Save event window data
# ------------------------
def save_event_windows(df, ticker, event_dates):
    event_folder = "/opt/airflow/dags/event_windows"
    os.makedirs(event_folder, exist_ok=True)

    for event_name, event_str in event_dates.items():
        event_dt = datetime.strptime(event_str, "%Y-%m-%d")
        mask = (df['Date'] >= event_dt - timedelta(days=5)) & (df['Date'] <= event_dt + timedelta(days=5))
        event_df = df.loc[mask].copy()

        if not event_df.empty:
            filename = f"{event_folder}/{ticker}_{event_name}.csv"
            event_df.to_csv(filename, index=False)

# ------------------------
# Main ETL Function
# ------------------------
def fetch_transform_save():
    for ticker in tickers:
        df = yf.download(ticker, start="2024-01-01", end="2025-12-31", interval="1d")
        df.reset_index(inplace=True)
        df['MA20'] = df['Close'].rolling(window=20).mean()
        df['MA50'] = df['Close'].rolling(window=50).mean()
        df['Volatility_5D'] = df['Close'].rolling(5).std()
        df['Return_3D'] = df['Close'].pct_change(3)
        df['Ticker'] = ticker

        # Save full data
        df.to_csv(f"/opt/airflow/dags/{ticker}_data.csv", index=False)

        # Save windowed data for each event
        save_event_windows(df, ticker, event_dates)

# ------------------------
# Airflow DAG Setup
# ------------------------
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='stock_etl_cof',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=['stocks', 'events', 'volatility']
) as dag:

    etl_task = PythonOperator(
        task_id='fetch_transform_save',
        python_callable=fetch_transform_save
    )
