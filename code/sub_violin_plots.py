import pandas as pd
from hires_analysis import violin_plots

data_day_1 = pd.read_csv("C:\\Users\\Dorian\\HIRES-2025-NYC-Subway-Air-Quality-Project\\data\\1379_2025-7-14.csv")
data_day_2 = pd.read_csv("C:\\Users\\Dorian\\HIRES-2025-NYC-Subway-Air-Quality-Project\\data\\1379_2025-7-15.csv")
data_day_3 = pd.read_csv("C:\\Users\\Dorian\\HIRES-2025-NYC-Subway-Air-Quality-Project\\data\\1379_2025-7-16.csv")
data_day_4 = pd.read_csv("C:\\Users\\Dorian\\HIRES-2025-NYC-Subway-Air-Quality-Project\\data\\1379_2025-7-24.csv")


day_1 = {
    "st_125" : ("13:47:02", '13:59:47'),
    "st_42_portauthority" : ("14:21:45", "14:34:36"),
    "barclayCenter" : ("15:09:36", "15:20:06")
}

day_2 = {
    "st_125_2" : ("13:01:17", "13:33:56" ),
    "st_42_bryantpark" : ("13:49:03", "14:22:04"),
    "st_74" : ("14:50:19", "15:23:05"),
    "courtsquare" : ("15:31:27", "15:52:04"),
    "fulton" : ("16:12:29", "16:22:27")
    }

day_3 = {
    "st_137" : ("13:32:38", "13:52:25"),
    "st_225" : ("14:10:31", "18:20:30"),
    "st_242" : ("18:28:43", "18:36:34")
    }

day_4 = {
    'st_72' : ("14:45:40", "15:10:00"),
    'st_86' : ("15:13:42", "15:32:23"),
    'st_96' : ("15:36:19", "15:53:12")
    }

days = [day_1, day_2, day_3, day_4]

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


all_pm25_day_1, all_time_day_1 = get_all_pm25(data_day_1, day_1) # csv, dict
all_pm25_day_2, all_time_day_2 = get_all_pm25(data_day_2, day_2)
all_pm25_day_3, all_time_day_3 = get_all_pm25(data_day_3, day_3)
all_pm25_day_4, all_time_day_4 = get_all_pm25(data_day_4, day_4)

all_pm25 = [all_pm25_day_1, all_pm25_day_2, all_pm25_day_3, all_pm25_day_4]

i = 0

violin_plots(all_pm25, i, days)