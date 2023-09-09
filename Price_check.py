import pandas as pd

filepath = "Files/Produce_location_prices.csv"
df = pd.read_csv(filepath)
print(len(df))