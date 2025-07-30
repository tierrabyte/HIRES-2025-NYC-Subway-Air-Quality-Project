import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


file_7_14 = "C:\\Users\\Dorian\\HIRES-2025-NYC-Subway-Air-Quality-Project\\data\\1379_2025-7-14.csv"
file_7_15 = "C:\\Users\\Dorian\\HIRES-2025-NYC-Subway-Air-Quality-Project\\data\\1379_2025-7-15.csv"
file_7_16 = "C:\\Users\\Dorian\\HIRES-2025-NYC-Subway-Air-Quality-Project\\data\\1379_2025-7-16.csv"
file_7_24 = "C:\\Users\\Dorian\\HIRES-2025-NYC-Subway-Air-Quality-Project\\data\\1379_2025-7-24.csv"


day_1 = pd.read_csv(file_7_14)
day_2 = pd.read_csv(file_7_15)
day_3 = pd.read_csv(file_7_16)
day_4 = pd.read_csv(file_7_24)

data = day_1
pm10_day_1 = day_1['PM10'].dropna()
pm2_day_1 = day_1['PM2.5'].dropna()
pm1_day_1 = day_1['PM1'].dropna()
co_day_1 = day_1['CO'].dropna()
time_day_1 = day_1['Time'].dropna()

pm10_day_2 = day_2['PM10'].dropna()
pm2_day_2 = day_2['PM2.5'].dropna()
pm1_day_2 = day_2['PM1'].dropna()
co_day_2 = day_2['CO'].dropna()
time_day_2 = day_2['Time'].dropna()

pm10_day_3 = day_3['PM10'].dropna()
pm2_day_3 = day_3['PM2.5'].dropna()
pm1_day_3 = day_3['PM1'].dropna()
co_day_3 = day_3['CO'].dropna()
time_day_3 = day_3['Time'].dropna()

pm10_day_4 = day_4['PM10'].dropna()
pm2_day_4 = day_4['PM2.5'].dropna()
pm1_day_4 = day_4['PM1'].dropna()
co_day_4 = day_4['CO'].dropna()
time_day_4 = day_4['Time'].dropna()


#day 1
st_125_7_14 = ("13:47:02", "13:59:47")
st_42_portauthority_7_14 = ("14:21:45" , "14:34:36")
barclayCenter_7_14 = ("15:09:36", "15:20:06")

#day 2
st_125_bryantpark_7_15 = ("13:01:17", "13:33:56")
st_42_bryantpark_7_15 = ("13:49:03", "14:22:04")
st_74_7_15 = ("14:50:19", "15:23:05")
courtsquare_7_15 = ("15:31:27", "15:52:04")
fulton_7_15 = ("16:12:29", "16:22:27")

#day 3
st_137_7_16 = ("13:32:38", "13:52:25")
st_225_7_16 = ("14:10:31", "18:20:30")
st_242_7_16 = ("18:28:43", "18:36:34")

#day 4
st_72_7_24 = ("14:45:40", "15:10:00")
st_86_7_24 = ("15:13:42", "15:32:23")
st_96_7_24 = ("15:36:19", "15:53:12")

def find_mean_day_1(street):
    time = time_day_1
    startIndex = time[time == street[0]].index.values[0]
    endIndex = time[time == street[1]].index.values[0]
    ref = pm2_day_1
    mean = float(ref[startIndex:endIndex].mean().round(2))
    print("Day 1:", mean)
    
    plt.violinplot(ref[startIndex:endIndex])
    plt.show()
    
    return mean

def find_mean_day_2(street):
    time = time_day_2
    startIndex = time[time == street[0]].index.values[0]
    endIndex = time[time == street[1]].index.values[0]
    ref = pm2_day_2
    mean = float(ref[startIndex:endIndex].mean().round(2))
    print("Day 2:", mean)
    
    plt.violinplot(ref[startIndex:endIndex])
    plt.show()
    
    return mean

def find_mean_day_3(street):
    time = time_day_3
    startIndex = time[time == street[0]].index.values[0]
    endIndex = time[time == street[1]].index.values[0]
    ref = pm2_day_3
    mean = float(ref[startIndex:endIndex].mean().round(2))
    print("Day 3:", mean)
    
    plt.violinplot(ref[startIndex:endIndex])
    plt.show()
    
    return mean

def find_mean_day_4(street):
    time = time_day_4
    startIndex = time[time == street[0]].index.values[0]
    endIndex = time[time == street[1]].index.values[0]
    ref = pm2_day_4
    mean = float(ref[startIndex:endIndex].mean().round(2))
    print("Day 4:", mean)
    
    plt.violinplot(ref[startIndex:endIndex])
    plt.show()
    
    return mean

mean_data = {"125th st 7/14": find_mean_day_1(st_125_7_14),
             "42nd st Port Authority 7/14": find_mean_day_1(st_42_portauthority_7_14),
             "Barclay Center 7/14": find_mean_day_1(barclayCenter_7_14),
             "125th st Bryant Park 7/15": find_mean_day_2(st_125_bryantpark_7_15),
             "42nd st Bryant Park 7/15": find_mean_day_2(st_42_bryantpark_7_15),
             "74th st 7/15": find_mean_day_2(st_74_7_15),
             "Court Square 7/15": find_mean_day_2(courtsquare_7_15),
             "Fulton 7/15": find_mean_day_2(fulton_7_15),
             "137th st 7/16": find_mean_day_3(st_137_7_16),
             "225th st 7/16": find_mean_day_3(st_225_7_16),
             "242nd st 7/16": find_mean_day_3(st_242_7_16),
             "72nd st 7/24": find_mean_day_4(st_72_7_24),
             "86th st 7/24": find_mean_day_4(st_86_7_24),
             "96th st 7/24": find_mean_day_4(st_96_7_24)}



print(mean_data)


