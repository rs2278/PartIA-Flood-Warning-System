import numpy as np
from matplotlib import dates
import matplotlib.pyplot as plt 
from datetime import timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels

def plot_water_levels(station, dates=None, levels=None, dt=10, dotesting = False):

   # Creating lists for dates and levels
    dates_self = dates
    levels_self = levels

    # Fetching dates and levels for specific station    
    # rough test to see if data is link as expected
    if station.measure_id[0:4] != "http":
        pass
    else:
        dates_self, levels_self = fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))

    # Plot
    plt.plot(dates_self, levels_self)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(f"Station {station.name}")

    # Plot of typical minimum and typical maximum, adding legend for clarity
    plt.plot(dates_self, [station.typical_range[0]] * len(dates_self), label="Min")
    plt.plot(dates_self, [station.typical_range[1]] * len(dates_self), label="Max")
    plt.legend()

    # Display plot
    plt.tight_layout()

    plt.show()

    #for testing purposes, if dotest = True, return lists of values used in plotting function
    if dotesting == True:
        return dates_self, levels_self
    else:
        pass


#from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
#from floodsystem.flood import stations_highest_rel_level

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