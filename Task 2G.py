from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation, inconsistent_latest_level_stations


# percentage >= 3 : severe
# percentage 2-3 and increasing : high
# percentage 2-3 and decreasing, or 1-2 and increasing : moderate
# else : low

stations = build_station_list()
update_water_levels(stations)
severe = ["towns with severe risk of flooding:"]
high = ["towns with high risk of flooding:"]
moderate = ["towns with moderate risk of flooding:"]
low = ["towns with low risk of flooding:"]
inconsistent_stations = inconsistent_latest_level_stations(stations)


for station in stations:
    
    if station.name not in inconsistent_stations:
        if station.town == None:
            pass
        else:


            if MonitoringStation.relative_water_level(station) >= 3:
                severe.append(station.town)
            elif MonitoringStation.relative_water_level(station) >= 2: 
                    high.append(station.town)
            elif MonitoringStation.relative_water_level(station) >= 1: 
                moderate.append(station.town)
            else:
                low.append(station.town)

print(severe)
print(high)
print(moderate)
print(low)

