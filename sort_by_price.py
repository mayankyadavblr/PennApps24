from RegionClassifier import *
import pandas as pd


def control(lat, long, commodities):
    filepath = "Files/Produce_location_prices.csv"
    df = pd.read_csv(filepath)
    
    region = get_region(lat, long)

    mask = df["region"].isin([region, "National"])
    rows = df[mask]

    mask = rows["commodity"].isin(commodities)
    rows = rows[mask]
    print(rows[["commodity", "region", "wtd avg price"]])

control(41.06104324059672, -81.51734366383978, ["Carrots", "orange", "watermelon"])