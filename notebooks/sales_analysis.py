import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/fmcg_sales_data.csv")

df["revenue"] = df["unit_price"] * df["quantity"]
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M").astype(str)

os.makedirs("dashboard", exist_ok=True)

print("=== FMCG Sales Analytics ===")

total_revenue = df["revenue"].sum()
print("\nTotal Revenue:")
print(total_revenue)

product_revenue = df.groupby("product_name")["revenue"].sum().sort_values(ascending=False)
print("\nRevenue by Product:")
print(product_revenue)

region_revenue = df.groupby("region")["revenue"].sum().sort_values(ascending=False)
print("\nRevenue by Region:")
print(region_revenue)

monthly_revenue = df.groupby("month")["revenue"].sum()
print("\nRevenue by Month:")
print(monthly_revenue)

promotion_revenue = df.groupby("promotion")["revenue"].sum()
print("\nRevenue by Promotion:")
print(promotion_revenue)

# Chart 1: Revenue by Product
plt.figure(figsize=(8, 5))
product_revenue.plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("dashboard/revenue_by_product.png")
plt.close()

# Chart 2: Revenue by Region
plt.figure(figsize=(8, 5))
region_revenue.plot(kind="bar")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("dashboard/revenue_by_region.png")
plt.close()

# Chart 3: Revenue by Month
plt.figure(figsize=(8, 5))
monthly_revenue.plot(kind="line", marker="o")
plt.title("Revenue by Month")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("dashboard/revenue_by_month.png")
plt.close()

top_product = product_revenue.idxmax()
top_region = region_revenue.idxmax()

print("\nBusiness Insights:")
print(f"1. The top-performing product is {top_product}.")
print(f"2. The best-performing region is {top_region}.")
print("3. Promotion impact should be analyzed further to improve campaign strategy.")

print("\nCharts saved to dashboard folder.")
