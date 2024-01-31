# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT



from haversine import haversine, Unit
from floodsystem.utils import sorted_by_key  # noqa
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river



stations = build_station_list()

def rivers_with_station(stations):
    list_of_rivers=[]
    for station in stations:
        if (station.river in list_of_rivers):
            pass
        else:
            list_of_rivers.append(station.river)
    return list_of_rivers

def stations_by_river(stations):
    stations_dic = dict()
    for river in rivers_with_station(stations):
        stations_dic[river] = []
    
    for station in stations:
        stations_dic[station.river].append(station)
    return stations_dic


#main
list1 = rivers_with_station(stations)
number = len(list1)
selected_list = list1[0:10]
selected_list.sort()
print(f"{number} stations. first 10 - {selected_list}")

dict1 = stations_by_river(stations)
AireStation = []
CamStation = []
ThamesStation = []
for station in dict1["River Aire"]:
    AireStation.append(station.name)

for station in dict1["River Cam"]:
    CamStation.append(station.name)

for station in dict1["River Thames"]:
    ThamesStation.append(station.name)

print(f"River Aire : {AireStation}")
print(f"River Cam : {CamStation}")
print(f"River Thames : {ThamesStation}")
