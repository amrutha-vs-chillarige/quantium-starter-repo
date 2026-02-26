import pandas as pd

# Load the three CSV files
df0 = pd.read_csv("data/daily_sales_data_0.csv")
df1 = pd.read_csv("data/daily_sales_data_1.csv")
df2 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine them
df = pd.concat([df0, df1, df2])

# Keep only pink morsel (case insensitive and safe)
df = df[df["product"].str.strip().str.lower() == "pink morsel"]

# Remove $ sign from price and convert to float
df["price"] = df["price"].replace('[\$,]', '', regex=True).astype(float)

# Create Sales column
df["Sales"] = df["price"] * df["quantity"]

# Keep required columns
final_df = df[["Sales", "date", "region"]]

# Rename columns
final_df = final_df.rename(columns={
    "date": "Date",
    "region": "Region"
})

# Save file
final_df.to_csv("formatted_sales_data.csv", index=False)

print("File created successfully!")