import os
import pandas as pd
import sqlite3

print("=== Mini Data Pipeline Started ===")

os.makedirs("reports", exist_ok=True)

# Extract
df = pd.read_csv("data/fmcg_sales_data.csv")
print("1. Extract: Loaded CSV data")

# Transform
df["revenue"] = df["unit_price"] * df["quantity"]
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M").astype(str)
print("2. Transform: Added revenue and month columns")

# Load
conn = sqlite3.connect("sales.db")
df.to_sql("sales_data", conn, if_exists="replace", index=False)
print("3. Load: Saved cleaned data into SQLite database")

# Generate report
summary_query = """
SELECT 
    product_name,
    SUM(revenue) AS total_revenue,
    SUM(quantity) AS total_quantity
FROM sales_data
GROUP BY product_name
ORDER BY total_revenue DESC
"""

summary = pd.read_sql(summary_query, conn)
summary.to_csv("reports/product_sales_summary.csv", index=False)

print("4. Report: Generated product sales summary")
print("\n=== Product Sales Summary ===")
print(summary)

conn.close()

print("\n=== Mini Data Pipeline Finished ===")
