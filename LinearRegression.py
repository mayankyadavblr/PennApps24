import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

raw_data = pd.read_csv('Files/Crop_recommendation.csv')

print(raw_data.info())
sns.pairplot(raw_data)

x = raw_data[["temperature", "humidity", "ph", "rainfall"]]
y = raw_data["label"]