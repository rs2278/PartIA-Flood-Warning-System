from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level


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