import numpy as np
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

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
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()


    #for testing purposes if dotesting is True then return variables to be tested/asserted
    if dotesting == True:
        return x, y

