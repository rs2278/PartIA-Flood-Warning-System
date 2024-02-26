from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold



# Consider only stations with consistent typical low/high data



def run():
    stations = build_station_list()

        # Update latest level data for all stations
    update_water_levels(stations)

    final_list = stations_level_over_threshold(stations,0.8)
    print(final_list)


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()




