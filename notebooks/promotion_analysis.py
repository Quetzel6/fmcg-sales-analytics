import pandas as pd

print("=== Promotion Campaign Analysis ===")

# Load data
df = pd.read_csv("data/fmcg_sales_data.csv")

# Create revenue column
df["revenue"] = df["unit_price"] * df["quantity"]

# Revenue grouped by promotion
promo_summary = df.groupby("promotion")["revenue"].sum()

print("\nRevenue by Promotion:")
print(promo_summary)

# Average revenue
avg_revenue = df.groupby("promotion")["revenue"].mean()

print("\nAverage Revenue per Order:")
print(avg_revenue)

# Insight
print("\n=== Business Insight ===")

if promo_summary["Yes"] > promo_summary["No"]:
    print("Promotion campaigns generate higher revenue.")
else:
    print("Promotion campaigns do not significantly improve revenue.")

print("Marketing teams can use this insight to optimize future campaigns.")

# Export report
promo_report = pd.DataFrame({
    "total_revenue": promo_summary,
    "avg_revenue_per_order": avg_revenue
})

promo_report.to_csv("reports/promotion_campaign_report.csv")

print("\nReport exported to reports/promotion_campaign_report.csv")
