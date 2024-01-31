from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit
from floodsystem.utils import sorted_by_key  # noqa
def stations_by_distance(stations,p):
    new_stations = []
    for i in range(len(stations)):
        d = haversine(p,stations[i].coord)
        my_tuple = (stations[i].name,stations[i].town,d)
        new_stations.append(my_tuple)
    
    return sorted_by_key(new_stations, 2, reverse=False)
stations = build_station_list()
#print(stations)
print(stations_by_distance(stations,(52.2053,0.1218))[:10])
print(stations_by_distance(stations,(52.2053,0.1218))[-10:])