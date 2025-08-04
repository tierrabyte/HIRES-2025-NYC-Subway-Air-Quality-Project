import pandas as pd
from hires_analysis import violin_plots

st_137 = pd.read_csv('C:/Users/Dorian/HIRES-2025-NYC-Subway-Air-Quality-Project/data/PurpleAir/188651 2025-07-16 2025-07-17 0-Minute Average.csv')
st_225 = pd.read_csv('C:/Users/Dorian/HIRES-2025-NYC-Subway-Air-Quality-Project/data/PurpleAir/140062 2025-07-16 2025-07-17 0-Minute Average.csv')
st_242 = pd.read_csv('C:/Users/Dorian/HIRES-2025-NYC-Subway-Air-Quality-Project/data/PurpleAir/188617 2025-07-16 2025-07-17 0-Minute Average.csv')

st_72 = pd.read_csv('C:/Users/Dorian/HIRES-2025-NYC-Subway-Air-Quality-Project/data/PurpleAir/82031 2025-07-24 2025-07-25 0-Minute Average.csv')
st_86 = pd.read_csv('C:/Users/Dorian/HIRES-2025-NYC-Subway-Air-Quality-Project/data/PurpleAir/257889 2025-07-24 2025-07-25 0-Minute Average.csv')
st_96 = pd.read_csv('C:/Users/Dorian/HIRES-2025-NYC-Subway-Air-Quality-Project/data/PurpleAir/43527 2025-07-24 2025-07-25 0-Minute Average.csv')


# Day -> DataFrames
data_day_3 = {"st_137": st_137, "st_225": st_225, "st_242": st_242}
data_day_4 = {"st_72": st_72, "st_86": st_86, "st_96": st_96}

# Time windows
day_3 = {
    "st_137": ("2025-07-16T13:33:24-04:00", "2025-07-16T13:53:23-04:00"), # 188651
    "st_225": ("2025-07-16T14:11:18-04:00", "2025-07-16T14:21:18-04:00"), # 140062
    "st_242": ("2025-07-16T14:29:13-04:00", "2025-07-16T14:37:13-04:00"), # 188617
}
day_4 = {
    "st_72": ("2025-07-24T14:44:28-04:00", "2025-07-24T15:10:28-04:00"), # 82031
    "st_86": ("2025-07-24T15:13:47-04:00", "2025-07-24T15:33:47-04:00"), # 257889
    "st_96": ("2025-07-24T15:37:01-04:00", "2025-07-24T15:53:01-04:00"), # 43527
}
days = [day_3, day_4]

# Functions
def get_pm25(data, station):
    data['time_stamp'] = pd.to_datetime(data['time_stamp'])
    start_time = pd.to_datetime(station[0])
    end_time = pd.to_datetime(station[1])
    sub_data = data[(data['time_stamp'] >= start_time) & (data['time_stamp'] <= end_time)]
    return sub_data['pm2.5_atm'].dropna(), sub_data['time_stamp'].dropna()

def get_all_pm25(data_dict, stations):
    all_pm25 = []
    for station_name, (start, end) in stations.items():
        data = data_dict[station_name]
        pm25, _ = get_pm25(data, (start, end))
        if len(pm25) > 0:
            all_pm25.append(pm25.values)
        else:
            print(f"[!] No data found for {station_name}")
    return all_pm25

# Run and plot
pm25_day3 = get_all_pm25(data_day_3, day_3)
pm25_day4 = get_all_pm25(data_day_4, day_4)

all_pm25 = [pm25_day3, pm25_day4]
violin_plots(all_pm25, i=0, days=days)