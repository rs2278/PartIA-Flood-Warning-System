# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine, Unit
from floodsystem.utils import sorted_by_key  # noqa
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
def stations_by_distance(stations,p):
    new_stations = []
    for i in range(len(stations)):
        d = haversine(p,stations[i].coord)
        my_tuple = (stations[i].name,stations[i].town,d)
        new_stations.append(my_tuple)
    
    return sorted_by_key(new_stations, 2, reverse=False)

def stations_within_radius(stations,center,r):
    stations_within = []
    for i in range(len(stations)):
        if haversine(center,stations[i].coord) < r:
            stations_within.append(stations[i].name)
    return sorted(stations_within)

# main
stations = build_station_list()
print(stations_within_radius(stations,(52.2053,0.1218),10))