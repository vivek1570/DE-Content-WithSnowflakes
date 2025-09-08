import pandas as pd
import random
from datetime import datetime, timedelta

start_time = datetime(2025, 9, 1, 9, 0, 0)
customers = ["Alice","Bob","Charlie","David","Emma","Frank","Grace","Hannah","Ivy","Jack","Zara"]

orders = []
for i in range(1, 101):
    ts = start_time + timedelta(minutes=i*5)
    cust = random.choice(customers)
    amt = random.randint(50, 500)
    orders.append([i, ts, cust, amt])

df = pd.DataFrame(orders, columns=["order_id","timestamp","customer","amount"])
df.to_csv("batch_orders.csv", index=False)
print("batch_orders.csv created")
