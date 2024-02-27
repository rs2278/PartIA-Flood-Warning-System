from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np
from matplotlib import dates
import matplotlib.pyplot as plt 
from datetime import timedelta
from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key

def stations_highest_rel_level_return_stations(stations, N):
    list_relative_water_level=[]
    stations = build_station_list()
    for station in stations:
        if station.relative_water_level() == None:
            pass
        else:
            list_relative_water_level.append(station,station.relative_water_level())
    sorted_relative_water_level = sorted_by_key(list_relative_water_level, 1, reverse=True)
    stations_sorted = [i[0] for i in sorted_relative_water_level]
    return stations_sorted

def run():
    # Initialization of variables that are needed afterwards
    stations = build_station_list()
    update_water_levels(stations)

    #get list of stations you want to plot (top 5 highest relative water levels)
    returned_list_stations = stations_highest_rel_level_return_stations(stations, 5)
    #for each list, plot
    for i in returned_list_stations:
        plot_water_levels(i)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()