import pandas as pd

filepath = "Files/Produce_location_prices.csv"
df = pd.read_csv(filepath)

mask = df["commodity"].isin(["Carrots"])
rows = df[mask]
print(rows[["commodity", "region", "wtd avg price"]])