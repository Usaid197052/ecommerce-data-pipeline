import pandas as pd
import os

base_dir = os.path.dirname(os.path.dirname(__file__))
clean_path = os.path.join(base_dir, "data", "cleaned_ecommerce.csv")

df = pd.read_csv(clean_path)

total_revenue = df['total'].sum()
print("Total Revenue:", total_revenue)

revenue_per_product = df.groupby('product')['total'].sum()
print("\nRevenue per product:\n", revenue_per_product)

top_customers = df.groupby('customer_name')['total'].sum().sort_values(ascending=False).head(3)

print("\nTop 3 Customers:\n", top_customers)
