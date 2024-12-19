import pandas as pd

def ingest_data(file_path):
    """Load raw sales data."""
    try:
        data = pd.read_csv(file_path)
        print("Data successfully ingested.")
        return data
    except Exception as e:
        print(f"Error ingesting data: {e}")
        raise
