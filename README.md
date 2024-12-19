
# Data Pipeline for Retail Sales Analysis

This project implements a data pipeline for analyzing retail sales data. The pipeline performs data ingestion, cleaning, feature engineering, and analysis, generating insights through visualizations and summary statistics. It also supports orchestration using Airflow.

---

## Directory Structure

```
data_pipeline/
├── scripts/
│   ├── ingest.py               # Data ingestion script
│   ├── clean.py                # Data cleaning script
│   ├── feature_engineering.py  # Feature engineering script
│   ├── analyze.py              # Data analysis and visualization script
├── airflow_dag.py              # Airflow DAG to orchestrate the pipeline
```

---

## Requirements

### Python Libraries
Install the following Python libraries before running the pipeline:
- `pandas`
- `matplotlib`
- `apache-airflow` (if using Airflow)

You can install these libraries using pip:
```bash
pip install pandas matplotlib apache-airflow
```

---

## Pipeline Stages

### 1. Data Ingestion (`ingest.py`)
- Reads raw sales data from a CSV file.
- Returns a DataFrame for further processing.

### 2. Data Cleaning (`clean.py`)
- Drops duplicate records.
- Handles missing values by filling defaults (e.g., `sales = 0`, `category = "Unknown"`).
- Converts the `date` column to a datetime format.

### 3. Feature Engineering (`feature_engineering.py`)
- Extracts `year` and `month` from the `date` column.
- Computes `daily_sales` by aggregating sales per day.

### 4. Data Analysis (`analyze.py`)
- Aggregates monthly sales data.
- Generates a line plot showing sales trends.

### 5. Orchestration (`airflow_dag.py`)
- Automates the pipeline using Airflow.
- Defines tasks for each stage: ingestion, cleaning, feature engineering, and analysis.
- Provides a daily schedule for the pipeline.

---

## Input Data Format

The pipeline expects a CSV file in the following format:

```csv
date,store,category,sales
2023-01-01,Store_A,Electronics,500
2023-01-01,Store_B,Clothing,300
2023-01-02,Store_A,Clothing,450
2023-01-02,Store_B,Electronics,700
```

---

## Steps to Run the Pipeline

### Local Execution
Run each script in sequence for a manual pipeline execution:
```bash
python scripts/ingest.py
python scripts/clean.py
python scripts/feature_engineering.py
python scripts/analyze.py
```

### Airflow Execution
1. Start the Airflow web server and scheduler:
   ```bash
   airflow webserver
   airflow scheduler
   ```
2. Place the `airflow_dag.py` file in the `dags/` directory of your Airflow project.
3. Open the Airflow UI, locate the `retail_sales_analysis_pipeline` DAG, and trigger it.

---

## Outputs

- Cleaned data is saved as a DataFrame (or optionally to a CSV file if implemented).
- Visualizations such as monthly sales trends.

