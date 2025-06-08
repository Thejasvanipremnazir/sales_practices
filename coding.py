import pandas as pd

data = {
    "Month": ["Jan", "Jan", "Feb", "Feb", "Mar", "Mar"],
    "Region": ["South", "North", "South", "North", "South", "North"],
    "Sales": [25000, 30000, 50000, 31000, 70000, 45000],
    "Profit": [4500, 2500, 7000, 6000, 5000, 3000],
    "Product": ["Mobile", "Laptop", "Mobile", "Laptop", "Laptop", "Laptop"]
}

df = pd.DataFrame(data)
df.to_csv("sales.csv", index=False)
print(" Dataset saved as 'sales.csv'")

print("Total Sales:", df["Sales"].sum())     # 176000
print("Total Profit:", df["Profit"].sum())   # 17000

print("\nGroup by Region - Sales:")
print(df.groupby("Region")["Sales"].sum())

print("\nGroup by Month - Sales and Profit:")
print(df.groupby("Month")[["Sales", "Profit"]].sum())

print("\nFilter: Only Laptop Sales")
print(df[df["Product"] == "Laptop"])
