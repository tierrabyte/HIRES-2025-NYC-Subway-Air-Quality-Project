import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("data//1379_2025-7-14.csv")

stations = {
    "st_125" : ("13:47:02", '13:59:47'),
    "st_42_portauthority" : ("14:21:45", "14:34:36"),
    "barclayCenter" : ("15:09:36", "15:20:06")
}




def get_pm25(data, station):
    pm25 = data['PM2.5'].dropna()
    time = data['Time'].dropna()

    startIndex = time[time == station[0]].index.values[0]
    endIndex = time[time == station[1]].index.values[0]

    sub_pm25 = pm25[startIndex : endIndex + 1]
    sub_time = time[startIndex : endIndex + 1]

    return sub_pm25, sub_time

def get_all_pm25(data, stations):
    all_pm25 = [] 
    all_time = []  

    for station_name, (start_time, end_time) in stations.items():
        pm25, time = get_pm25(data, (start_time, end_time))

        if len(pm25) > 0:  
            all_pm25.append(pm25.values) 
            all_time.append(time.values)

    return all_pm25, all_time



all_pm25, all_time = get_all_pm25(data, stations)
print(all_pm25)
print(all_time)



plt.figure(figsize=(10, 6))
plt.violinplot(all_pm25, showmeans=True, showmedians=True)
plt.xticks(
    ticks=range(1, len(stations) + 1),
    labels=list(stations.keys()),
    rotation=45
)
plt.title("PM2.5 Distribution per Station")
plt.ylabel("PM2.5 (µg/m³)")
plt.tight_layout()
plt.show()

