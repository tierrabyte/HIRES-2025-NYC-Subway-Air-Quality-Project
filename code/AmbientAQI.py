import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#day 1
filename = "PurpleAir_7-14/portauth_07-14_29183.csv"
portauthority_42 = pd.read_csv(filename)     #change soon

filename2 = "PurpleAir_7-14/st-125_7-14_82929.csv"
st_125 = pd.read_csv(filename2)

filename3 = "PurpleAir_7-14/barclay_7-14_143784.csv"
barclaycenter = pd.read_csv(filename3)

#day 2
filename4 = "PurpleAir_7-15/bryantpark_07-15_29183.csv"
bryantpark_42 = pd.read_csv(filename4)

filename5 = "PurpleAir_7-15/"
st_125_15 = pd.read_csv(filename5)

filename6 = "PurpleAir_7-15/128551 2025-07-15 2025-07-16 0-Minute Average.csv"
broadway_roosevelt_74th = pd.read_csv(filename6)

filename7 = "PurpleAir_7-15/143784 2025-07-15 2025-07-16 0-Minute Average.csv"
fultonstreet = pd.read_csv(filename7)

filename8 = "PurpleAir_7-15/147789 2025-07-15 2025-07-16 0-Minute Average.csv"
courtSquare = pd.read_csv(filename8)

day1 = {
    "st_125" : ("2025-07-14T13:46:32-04:00", '2025-07-14T13:58:32-04:00'),
    "portauthority_42" : ("2025-07-14T14:20:12-04:00", "2025-07-14T14:34:12-04:00"),
    "barclaycenter" : ("2025-07-14T15:08:46-04:00", "2025-07-14T15:20:46-04:00"),
}


day2 = {
    "st_125_15" : ("2025-07-15T13:00:45-04:00", "2025-07-15T13:32:45-04:00" ),
    "bryantpark_42" : ("2025-07-15T13:58:23-04:00", "2025-07-15T14:22:23-04:00"),
    "broadway_roosevelt_74th" : ("2025-07-15T14:49:35-04:00", "2025-07-15T15:23:36-04:00"),
    "courtSquare" : ("2025-07-15T15:30:57-04:00", "2025-07-15T15:52:57-04:00"),
    "fultonstreet" : ("2025-07-15T16:12:21-04:00", "2025-07-15T16:22:21-04:00"),
}

def get_pm25(data, station):
    pm25 = data["pm2.5_atm"]
    time = data["time_stamp"]

    startindex = time[time == station[0]].index.values[0]
    endindex = time[time == station[1]].index.values[0]

    sub_pm25 = pm25[startindex : endindex]
    sub_time = time[startindex : endindex]

    return sub_pm25, sub_time

def get_all_pm25(stations):
    all_pm25 = []
    all_time = []

    for station_name, time_range in stations.items():
        try:
            data = globals()[station_name]
            pm25, time = get_pm25(data, time_range)

            if len(pm25) > 0:
                all_pm25.append(pm25.values)
                all_time.append(time.values)
        except KeyError:
            print(f"Data for {station_name} not found, skipping.")
        except IndexError:
            print(f"Time range not found in {station_name}, skipping.")

    return all_pm25, all_time



def plot_pm25_by_day(stations):
    plt.figure(figsize=(12, 6))

    for station_name, time_range in stations.items():
        try:
            data = globals()[station_name]
            pm25_vals, time_vals = get_pm25(data, time_range)

            plt.plot(time_vals, pm25_vals, label=station_name)
        except KeyError:
            print(f"Data for {station_name} not found, skipping.")
        except IndexError:
            print(f"Time range not found in {station_name}, skipping.")

    plt.title("PM2.5 Levels by Station")
    plt.xlabel("Time")
    plt.ylabel("PM2.5")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()





