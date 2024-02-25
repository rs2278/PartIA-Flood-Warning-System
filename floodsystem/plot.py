import numpy as np
from matplotlib import dates
import matplotlib.pyplot as plt 
from datetime import timedelta
from datafetcher import fetch_measure_levels

def plot_water_levels(station, dates=None, levels=None, dt=10, dotesting = False):
    dates_self = dates
    levels_self = levels
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

