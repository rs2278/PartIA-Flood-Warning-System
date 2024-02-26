from .stationdata import build_station_list, update_water_levels
from .station import MonitoringStation
from .station import inconsistent_latest_level_stations



# Consider only stations with consistent typical low/high data
def stations_level_over_threshold(stations, tol):
    inconsistent_stations = inconsistent_latest_level_stations(stations)
    latest_over_tol = []
    for station in stations:
        if station.name not in inconsistent_stations and MonitoringStation.relative_water_level(station) > tol:
            value = MonitoringStation.relative_water_level(station)
            new_tuple = (station.name, value)
            latest_over_tol.append(new_tuple)
    sorted_latest_over_tol = sorted(latest_over_tol, key=lambda x: x[1], reverse=True)

    
    return sorted_latest_over_tol

# returns a list of the N stations (objects) at which the water level, relative to the typical range, is highest.
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