import matplotlib.pyplot as plt
import datetime
from datetime import timedelta
from floodsystem.stationdata import build_station_list, update_water_levels

def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.title(station.name)
    plt.tight_layout()
    plt.show()

# main
dates = [datetime(2024, 2, 15) - timedelta(days=i) for i in range(10)]
levels = [0.2, 0.7, 0.95, 0.92, 1.02, 0.91, 0.64, 0.78, 0.85, 1.1]

stations = build_station_list()

# Sorting stations based on current relative water level
sorted_stations = sorted(stations, key=lambda station: max(levels), reverse=True)[:5]

for station in sorted_stations:
    plot_water_levels(station, dates, levels)