import pandas as pd
import matplotlib.pyplot as plt
import sub_violin_plots as svp
from hires_analysis import stations


file_7_14 = "C:\\Users\\Dorian\\HIRES-2025-NYC-Subway-Air-Quality-Project\\data\\1379_2025-7-14.csv"
file_7_15 = "C:\\Users\\Dorian\\HIRES-2025-NYC-Subway-Air-Quality-Project\\data\\1379_2025-7-15.csv"
file_7_16 = "C:\\Users\\Dorian\\HIRES-2025-NYC-Subway-Air-Quality-Project\\data\\1379_2025-7-16.csv"
file_7_24 = "C:\\Users\\Dorian\\HIRES-2025-NYC-Subway-Air-Quality-Project\\data\\1379_2025-7-24.csv"


day_1 = pd.read_csv(file_7_14)
day_2 = pd.read_csv(file_7_15)
day_3 = pd.read_csv(file_7_16)
day_4 = pd.read_csv(file_7_24)

data = day_1
pm2_day_1 = day_1['PM2.5'].dropna()
time_day_1 = day_1['Time'].dropna()

pm2_day_2 = day_2['PM2.5'].dropna()
time_day_2 = day_2['Time'].dropna()

pm2_day_3 = day_3['PM2.5'].dropna()
time_day_3 = day_3['Time'].dropna()

pm2_day_4 = day_4['PM2.5'].dropna()
time_day_4 = day_4['Time'].dropna()

def find_mean_day_1(street):
    time = time_day_1
    startIndex = time[time == street[0]].index.values[0]
    endIndex = time[time == street[1]].index.values[0]
    ref = pm2_day_1
    mean = float(ref[startIndex:endIndex].mean().round(2))
    print("Day 1:", mean)
    
    plt.violinplot(ref[startIndex:endIndex])
    
    return mean

def find_mean_day_2(street):
    time = time_day_2
    startIndex = time[time == street[0]].index.values[0]
    endIndex = time[time == street[1]].index.values[0]
    ref = pm2_day_2
    mean = float(ref[startIndex:endIndex].mean().round(2))
    print("Day 2:", mean)
    
    plt.violinplot(ref[startIndex:endIndex])
    
    return mean

def find_mean_day_3(street):
    time = time_day_3
    startIndex = time[time == street[0]].index.values[0]
    endIndex = time[time == street[1]].index.values[0]
    ref = pm2_day_3
    mean = float(ref[startIndex:endIndex].mean().round(2))
    print("Day 3:", mean)
    
    plt.violinplot(ref[startIndex:endIndex])
    
    return mean

def find_mean_day_4(street):
    time = time_day_4
    startIndex = time[time == street[0]].index.values[0]
    endIndex = time[time == street[1]].index.values[0]
    ref = pm2_day_4
    mean = float(ref[startIndex:endIndex].mean().round(2))
    print("Day 4:", mean)
    
    plt.violinplot(ref[startIndex:endIndex])
    
    return mean



mean_data = {"125th st 7/14": find_mean_day_1(stations['st_125']),
             "42nd st Port Authority 7/14": find_mean_day_1(stations['st_42_portauthority']),
             "Barclay Center 7/14": find_mean_day_1(stations['barclayCenter']),
             "125th st Bryant Park 7/15": find_mean_day_2(stations['st_125_2']),
             "42nd st Bryant Park 7/15": find_mean_day_2(stations['st_42_bryantpark']),
             "74th st 7/15": find_mean_day_2(stations['st_74']),
             "Court Square 7/15": find_mean_day_2(stations['courtsquare']),
             "Fulton 7/15": find_mean_day_2(stations['fulton']),
             "137th st 7/16": find_mean_day_3(stations['st_137']),
             "225th st 7/16": find_mean_day_3(stations['st_225']),
             "242nd st 7/16": find_mean_day_3(stations['st_242']),
             "72nd st 7/24": find_mean_day_4(stations['st_72']),
             "86th st 7/24": find_mean_day_4(stations['st_86']),
             "96th st 7/24": find_mean_day_4(stations['st_96'])}
