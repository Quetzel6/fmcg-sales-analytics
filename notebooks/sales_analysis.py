import pandas as pd

df = pd.read_csv("data/fmcg_sales_data.csv")

df["revenue"] = df["unit_price"] * df["quantity"]
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M")

print("=== FMCG Sales Analytics ===")

print("\nTotal Revenue:")
print(df["revenue"].sum())

print("\nRevenue by Product:")
print(df.groupby("product_name")["revenue"].sum().sort_values(ascending=False))

print("\nRevenue by Region:")
print(df.groupby("region")["revenue"].sum().sort_values(ascending=False))

print("\nRevenue by Month:")
print(df.groupby("month")["revenue"].sum())

print("\nRevenue by Promotion:")
print(df.groupby("promotion")["revenue"].sum())

top_product = df.groupby("product_name")["revenue"].sum().idxmax()
top_region = df.groupby("region")["revenue"].sum().idxmax()

print("\nBusiness Insights:")
print(f"1. The top-performing product is {top_product}.")
print(f"2. The best-performing region is {top_region}.")
print("3. Promotion impact should be analyzed further to improve campaign strategy.")
