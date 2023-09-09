# Import Meteostat library and dependencies
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily

# Set time period
start = datetime(2018, 1, 1)
end = datetime(2018, 12, 31)

# Create Point for Vancouver, BC
location = Point(39.995837624559755, -75.1358451695366, 70)

# Get daily data for 2018
data = Daily(location, start, end)
data = data.fetch()

print(data[["tavg", "prcp"]])