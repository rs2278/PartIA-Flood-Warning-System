from station import MonitoringStation


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
