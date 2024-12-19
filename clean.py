import pandas as pd

def clean_data(data):
    """Clean raw sales data."""
    # Drop duplicates
    data = data.drop_duplicates()

    # Handle missing values
    data.fillna({"sales": 0, "category": "Unknown"}, inplace=True)

    # Convert date to datetime
    data['date'] = pd.to_datetime(data['date'])

    print("Data successfully cleaned.")
    return data
