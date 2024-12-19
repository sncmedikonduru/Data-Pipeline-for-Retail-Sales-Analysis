import pandas as pd

def feature_engineering(data):
    """Add new features."""
    # Create a 'year' and 'month' column
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month

    # Calculate daily sales
    data['daily_sales'] = data.groupby('date')['sales'].transform('sum')

    print("Feature engineering completed.")
    return data
