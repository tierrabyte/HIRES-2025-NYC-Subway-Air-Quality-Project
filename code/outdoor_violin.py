import pandas as pd
from hires_analysis import violin_plots

# Day 1 Data
st_125 = pd.read_csv('C:/Users/Dorian/HIRES-2025-NYC-Subway-Air-Quality-Project/data/PurpleAir/st-125_7-14_82929.csv')
st_42_portauthority = pd.read_csv('C:/Users/Dorian/HIRES-2025-NYC-Subway-Air-Quality-Project/data/PurpleAir/portauth_07-14_29183.csv')
barclayCenter = pd.read_csv('C:/Users/Dorian/HIRES-2025-NYC-Subway-Air-Quality-Project/data/PurpleAir/barclay_7-14_143784.csv')

# Day 2 Data
st_125_2 = pd.read_csv('C:/Users/Dorian/HIRES-2025-NYC-Subway-Air-Quality-Project/data/PurpleAir/st-125_7-15_82929.csv')
st_42_bryantpark = pd.read_csv('C:/Users/Dorian/HIRES-2025-NYC-Subway-Air-Quality-Project/data/PurpleAir/bryantpark_07-15_29183.csv')
st_74 = pd.read_csv('C:/Users/Dorian/HIRES-2025-NYC-Subway-Air-Quality-Project/data/PurpleAir/st-74_7-15_128551.csv')
courtsquare = pd.read_csv('C:/Users/Dorian/HIRES-2025-NYC-Subway-Air-Quality-Project/data/PurpleAir/st-74_7-15_128551.csv')
fulton = pd.read_csv('C:/Users/Dorian/HIRES-2025-NYC-Subway-Air-Quality-Project/data/PurpleAir/fulton_7-15_143784.csv')

# Day 3 Data
st_137 = pd.read_csv('C:/Users/Dorian/HIRES-2025-NYC-Subway-Air-Quality-Project/data/PurpleAir/st-137_7-16_188651.csv')
st_225 = pd.read_csv('C:/Users/Dorian/HIRES-2025-NYC-Subway-Air-Quality-Project/data/PurpleAir/st-225_7-16_140062.csv')
st_242 = pd.read_csv('C:/Users/Dorian/HIRES-2025-NYC-Subway-Air-Quality-Project/data/PurpleAir/st-242_7-16_188617.csv')

# Day 4 Data
st_72 = pd.read_csv('C:/Users/Dorian/HIRES-2025-NYC-Subway-Air-Quality-Project/data/PurpleAir/st-72_7-24_82031.csv')
st_86 = pd.read_csv('C:/Users/Dorian/HIRES-2025-NYC-Subway-Air-Quality-Project/data/PurpleAir/st-86_7-24_257889.csv')
st_96 = pd.read_csv('C:/Users/Dorian/HIRES-2025-NYC-Subway-Air-Quality-Project/data/PurpleAir/st-96_7-24_43527.csv')

# Day -> DataFrames
data_day_1 = {"st_125": st_125, "portauthority_42": st_42_portauthority, "barclaycenter": barclayCenter}
data_day_2 = {"st_125_15": st_125_2, "bryantpark_42": st_42_bryantpark, "broadway_roosevelt_74th": st_74, "courtSquare": courtsquare, "fultonstreet": fulton}
data_day_3 = {"st_137": st_137, "st_225": st_225, "st_242": st_242}
data_day_4 = {"st_72": st_72, "st_86": st_86, "st_96": st_96}

# Time windows
day_1 = {
    "st_125" : ("2025-07-14T13:46:32-04:00", '2025-07-14T13:58:32-04:00'),
    "portauthority_42" : ("2025-07-14T14:20:12-04:00", "2025-07-14T14:34:12-04:00"),
    "barclaycenter" : ("2025-07-14T15:08:46-04:00", "2025-07-14T15:20:46-04:00"),
}


day_2 = {
    "st_125_15" : ("2025-07-15T13:00:45-04:00", "2025-07-15T13:32:45-04:00" ),
    "bryantpark_42" : ("2025-07-15T13:58:23-04:00", "2025-07-15T14:22:23-04:00"),
    "broadway_roosevelt_74th" : ("2025-07-15T14:49:35-04:00", "2025-07-15T15:23:36-04:00"),
    "courtSquare" : ("2025-07-15T15:30:57-04:00", "2025-07-15T15:52:57-04:00"),
    "fultonstreet" : ("2025-07-15T16:12:21-04:00", "2025-07-15T16:22:21-04:00"),
}
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
days = [day_1, day_2, day_3, day_4]

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
pm25_day1 = get_all_pm25(data_day_1, day_1)
pm25_day2 = get_all_pm25(data_day_2, day_2)
pm25_day3 = get_all_pm25(data_day_3, day_3)
pm25_day4 = get_all_pm25(data_day_4, day_4)

all_pm25 = [pm25_day1, pm25_day2, pm25_day3, pm25_day4]
violin_plots(all_pm25, i=0, days=days)