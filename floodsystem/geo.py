# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine, Unit
from .utils import sorted_by_key  # noqa
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

