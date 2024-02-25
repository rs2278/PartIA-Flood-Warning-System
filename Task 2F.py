import numpy as np
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import numpy as np
from matplotlib import dates
import matplotlib.pyplot as plt 
from datetime import timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels

def polyfit(dates1, levels, p):
    x = dates.date2num(dates1)
    y = levels


    # Find coefficients of best-fit polynomial f(x) of degree p, with a change of base of d0
    p_coeff = np.polyfit(x - x[0], y, p)

    # Convert coefficient into a polynomial that can be evaluated,
    poly = np.poly1d(p_coeff)

    return poly, x[0]


def plot_water_level_with_fit(station, dates1=None, levels=None, p=4, dt=2, dotesting = False):
    # Creating empty lists for dates and levels
    dates_self = dates1
    levels_self = levels

    # Fetching dates and levels for specific station
    # rough test to check data is correct
    if station.measure_id[0:4] != "http":
        print('ERROR the measure ID is invalid')
        pass
    else:
        dates_self, levels_self = fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))

    #use polyfit and get fitted data
    poly, d0 = polyfit(dates_self, levels_self, p)
    x = dates.date2num(dates_self)
    y = poly(x - d0)

    #plot fitted and original data
    plt.plot(dates_self, y, label="Power Fit")
    plt.plot(dates_self, levels_self, label="Original")

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


    #for testing purposes if dotesting is True then return variables to be tested/asserted
    if dotesting == True:
        return x, y



def run():
    # Initialization of variables that are needed afterwards
    stations = build_station_list()
    update_water_levels(stations)

    #get the stations you want to plot
    returned_list = stations_highest_rel_level(stations, 5)


#for each of the stations, plot using the created function
    for i in returned_list:
        plot_water_level_with_fit(i, p=4, dt=2)


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()