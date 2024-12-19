import pandas as pd
import matplotlib.pyplot as plt

def analyze_data(data):
    """Analyze the data and generate insights."""
    # Aggregated monthly sales
    monthly_sales = data.groupby(['year', 'month'])['sales'].sum().reset_index()

    # Plot sales trends
    plt.figure(figsize=(10, 5))
    plt.plot(monthly_sales['month'], monthly_sales['sales'], marker='o')
    plt.title('Monthly Sales Trends')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.grid()
    plt.show()

    print("Analysis complete.")
