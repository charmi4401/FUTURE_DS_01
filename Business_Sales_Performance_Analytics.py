import pandas as pd 
 
# Load dataset 
df = pd.read_csv("Sample_Superstore.csv", encoding="latin1") 
 
# ---------------- DATA CLEANING ---------------- 
 
# Remove row with missing Row ID 
df = df.dropna(subset=["Row ID"]) 
 
# Convert dates 
df["Order Date"] = pd.to_datetime(df["Order Date"], format="mixed") 
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="mixed") 
 
# Convert Row ID to integer 
df["Row ID"] = df["Row ID"].astype(int) 
 
# Save cleaned dataset 
df.to_csv("Sample_Superstore_Cleaned.csv", index=False) 
 
 
# ---------------- OVERALL PERFORMANCE ---------------- 
 
total_sales = df["Sales"].sum() 
total_profit = df["Profit"].sum() 
total_quantity = df["Quantity"].sum() 
total_orders = df["Order ID"].nunique() 
 
profit_margin = (total_profit / total_sales) * 100 
 
 
# ---------------- SALES TREND ---------------- 
 
df["Year"] = df["Order Date"].dt.year 
df["Month"] = df["Order Date"].dt.month 
 
yearly_sales = df.groupby("Year")["Sales"].sum() 
yearly_profit = df.groupby("Year")["Profit"].sum() 
monthly_sales = df.groupby("Month")["Sales"].sum() 
 
highest_month = monthly_sales.idxmax() 
lowest_month = monthly_sales.idxmin() 
 
 
# ---------------- TOP PRODUCTS ---------------- 
 
top_products = ( 
    df.groupby("Product Name")["Sales"] 
    .sum() 
    .sort_values(ascending=False) 
    .head(10) 
) 
 
 
# ---------------- CATEGORY PERFORMANCE ---------------- 
 
category_performance = ( 
    df.groupby("Category")[["Sales", "Profit"]] 
    .sum() 
    .sort_values("Sales", ascending=False) 
) 
 
 
# ---------------- REGION PERFORMANCE ---------------- 
 
region_performance = ( 
    df.groupby("Region")[["Sales", "Profit"]] 
    .sum() 
    .sort_values("Sales", ascending=False) 
) 
 
 
# ---------------- SUB-CATEGORY PERFORMANCE ---------------- 
 
subcategory_performance = ( 
    df.groupby("Sub-Category")[["Sales", "Profit"]] 
    .sum() 
    .sort_values("Sales", ascending=False) 
) 
 
 
# ---------------- DISCOUNT ANALYSIS ---------------- 
 
discount_analysis = ( 
    df.groupby("Discount")["Profit"] 
    .agg(["sum", "mean", "count"]) 
) 
 
 
# ---------------- LOSS-MAKING SUB-CATEGORIES ---------------- 
 
loss_making = subcategory_performance[ 
    subcategory_performance["Profit"] < 0 
] 
 
 
# ---------------- LOSS SUB-CATEGORY DISCOUNT ANALYSIS ---------------- 
 
loss_subcategories = ["Tables", "Bookcases", "Supplies"] 
 
loss_discount_analysis = ( 
    df[df["Sub-Category"].isin(loss_subcategories)] 
    .groupby("Sub-Category") 
    .agg({ 
        "Sales": "sum", 
        "Profit": "sum", 
        "Discount": "mean" 
    }) 
    .sort_values("Profit") 
) 
 
 
# ---------------- TOP SUB-CATEGORIES BY PROFIT ---------------- 
 
top_profit_subcategories = ( 
    df.groupby("Sub-Category")["Profit"] 
    .sum() 
    .sort_values(ascending=False) 
    .head(10) 
) 
 
 
# ---------------- CATEGORY PROFIT MARGIN ---------------- 
 
category_margin = ( 
    df.groupby("Category")[["Sales", "Profit"]] 
    .sum() 
) 
 
category_margin["Profit Margin (%)"] = ( 
    category_margin["Profit"] / category_margin["Sales"] 
) * 100 
 
 
# ---------------- FINAL RESULTS ---------------- 

print("BUSINESS SALES PERFORMANCE")
print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Quantity:", total_quantity)
print("Total Orders:", total_orders)
print("Profit Margin:", round(profit_margin, 2), "%")

print("\nTOP 10 PRODUCTS")
print(top_products.round(2))

print("\nCATEGORY PERFORMANCE")
print(category_performance.round(2))

print("\nREGION PERFORMANCE")
print(region_performance.round(2))

print("\nLOSS-MAKING SUB-CATEGORIES")
print(loss_making.round(2))

print("\nCATEGORY PROFIT MARGIN")
print(category_margin.round(2))