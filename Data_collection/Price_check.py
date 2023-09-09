import pandas as pd

filepath = "Files/Produce_location_prices.csv"
df = pd.read_csv(filepath)

mask = df["region"].isin(["Northeast"])
rows = df[mask]
print(rows[["commodity", "region", "wtd avg price"]])