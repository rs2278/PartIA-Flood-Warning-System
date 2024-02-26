from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np
from matplotlib import dates
import matplotlib.pyplot as plt 
from datetime import timedelta

class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):
        """Create a monitoring station."""

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None
    def relative_water_level(self):

        # returns the latest water level as a fraction of the typical range
        if self.typical_range == None:
            return None
        elif self.typical_range[0] > self.typical_range[1]:
            return None
        elif self.latest_level == None:
            return None
        else:
            fraction = (self.latest_level - self.typical_range[0]) / (self.typical_range[1] - self.typical_range[0])
        return fraction
    
    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d





def plot_water_levels(station, dates=None, levels=None, dt=10, dotesting = False):
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










def run():
    # Initialization of variables that are needed afterwards
    stations = build_station_list()
    update_water_levels(stations)

    #get list of stations you want to plot (top 5 highest relative water levels)
    returned_list = stations_highest_rel_level(stations, 5)
    #for each list, plot
    for i in returned_list:
        plot_water_levels(i)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()