import pandas as pd

# โหลดข้อมูล
df = pd.read_csv("data/fmcg_sales_data.csv")

# สร้าง revenue
df["revenue"] = df["unit_price"] * df["quantity"]

# แปลง date
df["date"] = pd.to_datetime(df["date"])

# สร้าง customer_id (เพราะ dataset ไม่มี)
df["customer_id"] = df.index + 1

# วันที่ล่าสุดใน dataset
snapshot_date = df["date"].max()

# --- คำนวณ RFM ---
rfm = df.groupby("customer_id").agg({
    "date": lambda x: (snapshot_date - x.max()).days,
    "order_id": "count",
    "revenue": "sum"
})

rfm.columns = ["Recency", "Frequency", "Monetary"]

print("\n=== RFM Table ===")
print(rfm)

# --- แบ่ง Score ---
rfm["R_score"] = pd.qcut(rfm["Recency"], 3, labels=[3,2,1])
rfm["F_score"] = pd.qcut(rfm["Frequency"].rank(method="first"), 3, labels=[1,2,3])
rfm["M_score"] = pd.qcut(rfm["Monetary"], 3, labels=[1,2,3])

rfm["RFM_Score"] = rfm["R_score"].astype(str) + rfm["F_score"].astype(str) + rfm["M_score"].astype(str)

# --- Segmentation ---
def segment(row):
    if row["RFM_Score"] == "333":
        return "VIP"
    elif row["R_score"] == 3:
        return "Loyal"
    elif row["R_score"] == 1:
        return "At Risk"
    else:
        return "Normal"

rfm["Segment"] = rfm.apply(segment, axis=1)

print("\n=== Customer Segments ===")
print(rfm[["Recency", "Frequency", "Monetary", "Segment"]])
