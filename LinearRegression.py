import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

raw_data = pd.read_csv('Files/Crop_recommendation.csv')

print(raw_data.info())
sns.pairplot(raw_data)

x = raw_data[["temperature", "humidity", "ph", "rainfall"]]
le = LabelEncoder()
y = raw_data["label"]
y = le.fit_transform(raw_data['label'])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)

model = LinearRegression()
model.fit(x_train, y_train)
print(model.coef_)