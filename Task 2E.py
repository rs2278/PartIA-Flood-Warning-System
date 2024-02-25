import numpy as np
from matplotlib import dates
import matplotlib.pyplot as plt 
from datetime import timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.stationdata import update_water_levels
from floodsystem.plot import plot_water_levels

def stations_highest_rel_level(stations, N):
    list_relative_water_level=[]
    for station in stations:
        if MonitoringStation.relative_water_level(station) == None:
            pass
        else:
            value = MonitoringStation.relative_water_level(station)
            new_tuple = (station.name, value)
            list_relative_water_level.append(new_tuple)
    sorted_relative_water_level = sorted(list_relative_water_level, key=lambda x: x[1], reverse=True)
    N_highest_relative_water_level = sorted_relative_water_level[:N]
    return N_highest_relative_water_level


def run():
    # Initialization of variables that are needed afterwards
    stations = build_station_list()
    update_water_levels(stations)

    #get list of stations you want to plot (top 5 highest relative water levels)
    returned_list = stations_highest_rel_level(stations, 10)
    #for each list, plot
    for i in returned_list:
        plot_water_levels(i)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()