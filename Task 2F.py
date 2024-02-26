from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_highest_rel_level
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

    #get the stations you want to plot
    returned_list = stations_highest_rel_level_return_stations(stations, 5)


#for each of the stations, plot using the created function
    for i in returned_list:
        plot_water_level_with_fit(i, p=4, dt=2)


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()