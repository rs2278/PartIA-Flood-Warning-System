# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""

class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):
        """Create a monitoring station."""

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d



    def typical_range_consistent(self):
        # check whether self.typical_range is empty or the first element is higher than the second
        consistentFlag = True
        if self.typical_range == None:
            consistentFlag = False
        elif self.typical_range[0] > self.typical_range[1]:
            consistentFlag = False
        return consistentFlag
    
    def latest_level_consistent(self):
        consistentFlag = True
        if self.typical_range == None:
            consistentFlag = False
        elif self.typical_range[0] > self.typical_range[1]:
            consistentFlag = False
        elif self.latest_level == None:
            consistentFlag = False
        return consistentFlag

    
    def relative_water_level(self):

        # returns the latest water level as a fraction of the typical range
        if self.typical_range == None:
            return None
        elif self.typical_range[0] > self.typical_range[1]:
            return None
        elif self.latest_level == None:
            return None
        else:
            fraction = (self.latest_level - self.typical_range[0]) / (self.typical_range[1] - self.typical_range[0])
            return fraction

def inconsistent_typical_range_stations(stations):

        # generate a list of station consistent flag for every station
        consisFlagList = dict()
        for station in stations:
            flagNow = MonitoringStation.typical_range_consistent(station)
            consisFlagList[station.name] = flagNow
        
        # returns a list of stations that have inconsistent data
        inconsistentStations = []
        for key, value in consisFlagList.items():
            if value == False:
                inconsistentStations.append(key)

        return inconsistentStations
    
def inconsistent_latest_level_stations(stations):
        consisFlagList = dict()
        for station in stations:
            flagNow = MonitoringStation.latest_level_consistent(station)
            consisFlagList[station.name] = flagNow
        
        # returns a list of stations that have inconsistent data
        inconsistentStations = []
        for key, value in consisFlagList.items():
            if value == False:
                inconsistentStations.append(key)

        return inconsistentStations

    