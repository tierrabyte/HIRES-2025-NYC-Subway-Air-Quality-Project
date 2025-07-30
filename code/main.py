import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

filename = "1379_2025-7-14 (1).csv"
july14_data = pd.read_csv(filename)

filename2 = "1379_2025-7-15.csv"
july15_data = pd.read_csv(filename2)

filename3 = "1379_2025-7-16.csv"
july16_data = pd.read_csv(filename3)

filename4 = "1379_2025-7-24.csv"
july24_data = pd.read_csv(filename4)


stations = {
    "st_125" : ("13:47:02", '13:59:47'),
    "st_42_portauthority" : ("14:21:45", "14:34:36"),
    "barclayCenter" : ("15:09:36", "15:20:06"),
    # day 2
    "st_125_2" : ("13:01:17", "13:33:56" ),
    "st_42_bryantpark" : ("13:49:03", "14:22:04"),
    "st_74" : ("14:50:19", "15:23:05"),
    "courtsquare" : ("15:31:27", "15:52:04"),
    "fulton" : ("16:12:29", "16:22:27"),
    # day 3
    "st_137" : ("13:32:38", "13:52:25"),
    "st_225" : ("14:10:31", "18:20:30"),
    "st_242" : ("18:28:43", "18:36:34"),
}



def get_pm25(data, station):
    pm25 = data["PM2.5"]
    time = data["Time"]

    startindex = time[time == station[0]]
    endindex = time[time == station[1]]

    sub_pm25 = pm25[startindex : endindex]
    sub_time = time[startindex : endindex]

    return sub_pm25, sub_time



def get_carbonDioxide(data, station):
    carbon = data["C02"]
    time = data["Time"]

    startindex = time[time == station[0]]
    endindex = time[time == station[1]]

    sub_carbon = carbon[startindex : endindex]
    sub_time = time[startindex : endindex]

    return sub_carbon, sub_time


def get_pm10(data, station):
    pm10 = data["PM10"]
    time = data["Time"]

    startindex = time[time == station[0]]
    endindex = time[time == station[1]]

    sub_pm10 = pm10[startindex : endindex]
    sub_time = time[startindex : endindex]

    return sub_pm10, sub_time

def get_pm1(data, station):
    pm1 = data["PM1"]
    time = data["Time"]

    startindex = time[time == station[0]]
    endindex = time[time == station[1]]

    sub_pm1 = pm1[startindex : endindex]
    sub_time = time[startindex : endindex]

    return sub_pm1, sub_time

def get_relhum(data, station):
    relhum = data["RELHUM"]
    time = data["Time"]

    startindex = time[time == station[0]]
    endindex = time[time == station[1]]

    sub_relhum = relhum[startindex : endindex]
    sub_time = time[startindex : endindex]

    return sub_relhum, sub_time

def get_pressure(data, station):
    pressure = data["PRES(HPA)"]
    time = data["Time"]

    startindex = time[time == station[0]]
    endindex = time[time == station[1]]

    sub_pressure = pressure[startindex : endindex]
    sub_time = time[startindex : endindex]

    return sub_pressure, sub_time

def calculate_heat_index(data):
    temp_c = data['TEMP©'].dropna()
    rh = data['RELHUM'].dropna()

    temp_f = (temp_c * 9 / 5) + 32

    # Constants
    c1 = -42.379;
    c2 = 2.04901523;
    c3 = 10.14333127
    c4 = -0.22475541;
    c5 = -6.83783e-3;
    c6 = -5.481717e-2
    c7 = 1.22874e-3;
    c8 = 8.5282e-4;
    c9 = -1.99e-6

    # Base formula
    hi = (c1 + c2 * temp_f + c3 * rh + c4 * temp_f * rh +
          c5 * temp_f ** 2 + c6 * rh ** 2 + c7 * temp_f ** 2 * rh +
          c8 * temp_f * rh ** 2 + c9 * temp_f ** 2 * rh ** 2)

    # Adjustment: Low humidity and high temp
    mask1 = (rh < 13) & (temp_f >= 80) & (temp_f <= 112)
    hi[mask1] -= ((13 - rh[mask1]) / 4) * np.sqrt((17 - np.abs(temp_f[mask1] - 95)) / 17)

    # Adjustment: High humidity and moderate temp
    mask2 = (rh > 85) & (temp_f >= 80) & (temp_f <= 87)
    hi[mask2] += ((rh[mask2] - 85) / 10) * ((87 - temp_f[mask2]) / 5)

    # For values below 80°F, use simpler formula
    mask3 = hi < 80
    hi[mask3] = 0.5 * (temp_f[mask3] + 61 + ((temp_f[mask3] - 68) * 1.2) + (rh[mask3] * 0.094))

    return hi

def plot_tempandheat1():


    fig, ax = plt.subplots()

    for station_name, (start_time, end_time) in stations.items():

        station_data = july14_data[(july14_data['Time'] >= start_time) & (july14_data['Time'] <= end_time)]

        if station_data.empty:
            print(f"No data for {station_name} in given time range")
            continue

        time = station_data['Time']
        temp = (station_data['TEMP©'] * 9 /5 ) + 32
        heatIndex = calculate_heat_index(station_data)


        ax.plot(time, temp, label=f'{station_name} Temp ')
        ax.plot(time, heatIndex, linestyle='--', label=f'{station_name} Heat Index')

    ax.set_title('Temperature and Heat Index at Subway Stations')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_tempandheat2():
    fig, ax = plt.subplots()

    for station_name, (start_time, end_time) in stations.items():

        station_data = july15_data[(july15_data['Time'] >= start_time) & (july15_data['Time'] <= end_time)]

        if station_data.empty:
            print(f"No data for {station_name} in given time range")
            continue

        time = station_data['Time']
        temp = (station_data['TEMP©'] * 9 / 5) + 32
        heatIndex = calculate_heat_index(station_data)

        ax.plot(time, temp, label=f'{station_name} Temp ')
        ax.plot(time, heatIndex, linestyle='--', label=f'{station_name} Heat Index')

    ax.set_title('Temperature and Heat Index at Subway Stations')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_tempandheat3():


    fig, ax = plt.subplots()

    for station_name, (start_time, end_time) in stations.items():

        station_data = july16_data[(july16_data['Time'] >= start_time) & (july16_data['Time'] <= end_time)]

        if station_data.empty:
            print(f"No data for {station_name} in given time range")
            continue

        time = station_data['Time']
        temp = (station_data['TEMP©'] * 9 / 5) + 32
        heatIndex = calculate_heat_index(station_data)

        ax.plot(time, temp, label=f'{station_name} Temp ')
        ax.plot(time, heatIndex, linestyle='--', label=f'{station_name} Heat Index')

    ax.set_title('Temperature and Heat Index at Subway Stations')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_tempandheat4():
    stations = {
        "st_72_7_24" : ("14:45:40", "15:10:00"),
        "st_86_7_24" : ("15:13:42", "15:32:23"),
        "st_96_7_24" : ("15:36:19", "15:53:12")
    }

    fig, ax = plt.subplots()

    for station_name, (start_time, end_time) in stations.items():

        station_data = july24_data[(july24_data['Time'] >= start_time) & (july24_data['Time'] <= end_time)]

        if station_data.empty:
            print(f"No data for {station_name} in given time range")
            continue

        time = station_data['Time']
        temp = (station_data['TEMP©'] * 9 / 5) + 32
        heatIndex = calculate_heat_index(station_data)

        ax.plot(time, temp, label=f'{station_name} Temp ')
        ax.plot(time, heatIndex, linestyle='--', label=f'{station_name} Heat Index')

    ax.set_title('Temperature and Heat Index at Subway Stations')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_pm25_by_station(data):
    plt.figure(figsize=(10,6))

    st_125_start, st_125_end = "13:47:02", "13:59:47"
    data_125 = data[(data['Time'] >= st_125_start) & (data['Time'] <= st_125_end)]
    if not data_125.empty:
        plt.plot(data_125['Time'], data_125['PM2.5'], label='125th St')


    st_42_start, st_42_end = "14:21:45", "14:34:36"
    data_42 = data[(data['Time'] >= st_42_start) & (data['Time'] <= st_42_end)]
    if not data_42.empty:
        plt.plot(data_42['Time'], data_42['PM2.5'], label='42nd St Port Authority')


    barclay_start, barclay_end = "15:09:36", "15:20:06"
    data_barclay = data[(data['Time'] >= barclay_start) & (data['Time'] <= barclay_end)]
    if not data_barclay.empty:
        plt.plot(data_barclay['Time'], data_barclay['PM2.5'], label='Barclay Center')


    plt.title('PM2.5 Levels at Subway Stations')
    plt.xlabel('Time')
    plt.ylabel('PM2.5 (µg/m³)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_carbonDixiode(data):
        plt.figure(figsize=(10, 6))

        st_125_start, st_125_end = "13:47:02", "13:59:47"
        data_125 = data[(data['Time'] >= st_125_start) & (data['Time'] <= st_125_end)]
        if not data_125.empty:
            plt.plot(data_125['Time'], data_125['C02'], label='125th St')

        st_42_start, st_42_end = "14:21:45", "14:34:36"
        data_42 = data[(data['Time'] >= st_42_start) & (data['Time'] <= st_42_end)]
        if not data_42.empty:
            plt.plot(data_42['Time'], data_42['C02'], label='42nd St Port Authority')

        barclay_start, barclay_end = "15:09:36", "15:20:06"
        data_barclay = data[(data['Time'] >= barclay_start) & (data['Time'] <= barclay_end)]
        if not data_barclay.empty:
            plt.plot(data_barclay['Time'], data_barclay['C02'], label='Barclay Center')

        plt.title('C02 levels')
        plt.xlabel('Time')
        plt.ylabel('C02')
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()

