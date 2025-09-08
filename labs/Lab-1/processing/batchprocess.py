import pandas as pd

# Read batch file at once
batch_df = pd.read_csv("../generators/batch_orders.csv")

print("First 5 rows of batch data:")
print(batch_df.head())

# Simple analytics
print("\nBatch total revenue:", batch_df['amount'].sum())
print("Batch average order value:", batch_df['amount'].mean())
print("Orders per customer:")
print(batch_df['customer'].value_counts())
