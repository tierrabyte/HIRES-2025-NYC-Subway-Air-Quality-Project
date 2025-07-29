import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

filename = "1379_2025-7-14 (1).csv"
data = pd.read_csv(filename)


def identify_PM25(data):
    col = data['PM2.5'].dropna()
    time = data['Time'].dropna()
    """
    plt.plot(time, col, 'r-o', label='PM2.5')
    plt.xlabel('Time')
    plt.ylabel('Concentration')
    plt.show()
    """

    # day 1
    st_125 = ("13:47:02", '13:59:47')
    st_42_portauthority = ("14:21:45", "14:34:36")
    barclayCenter = ("15:09:36", "15:20:06")
    # day 2
    st_42_bryantpark = ()
    st_74 = ()
    courtsquare = ()
    fulton = ()
    # day 3
    st_137 = ()
    st_225 = ()
    st_242 = ()

    # print(st_125[0])
    startIndex = time[time == st_125[0]].index.values[0]
    endIndex = time[time == st_125[1]].index.values[0]

    subcolumn = col[startIndex: endIndex]
    subtime = time[startIndex: endIndex]

    print(startIndex)
    print(endIndex)

    plt.plot(subtime, subcolumn, 'r-o', label="PM2.5")
    plt.xticks(fontsize=10, rotation=45)
    plt.xlabel("Time")
    plt.ylabel("Concentration")
    plt.grid(True)
    plt.show()


def identify_carbonDioxide():
    data = pd.read_csv(filename)
    col = data['C02'].dropna()
    time = data['Time'].dropna()

    # day 1
    st_125 = ("13:47:02", '13:59:47', "14:21:45", "14:34:36", "15:09:36", "15:20:06")

    st_42_portauthority = ("14:21:45", "14:34:36")
    barclayCenter = ("15:09:36", "15:20:06")

    startIndex = time[time == st_125[0]].index.values[0]
    endIndex = time[time == st_125[1]].index.values[0]

    subcolumn = col[startIndex: endIndex]
    subtime = time[startIndex: endIndex]

    print(startIndex)
    print(endIndex)

    plt.plot(subtime, subcolumn, 'r-o', label="CO2")
    plt.xticks(fontsize=10, rotation=45)
    plt.xlabel("Time")
    plt.ylabel("Concentration")
    plt.grid(True)
    plt.show()


def identify_PM10():
    data = pd.read_csv(filename)
    col = data['PM10'].dropna()
    time = data['Time'].dropna()

    # day 1
    st_125 = ("13:47:02", '13:59:47', "14:21:45", "14:34:36", "15:09:36", "15:20:06")
    st_42_portauthority = ("14:21:45", "14:34:36")
    barclayCenter = ("15:09:36", "15:20:06")

    startIndex = time[time == st_125[0]].index.values[0]
    endIndex = time[time == st_125[1]].index.values[0]

    subcolumn = col[startIndex: endIndex]
    subtime = time[startIndex: endIndex]

    print(startIndex)
    print(endIndex)

    plt.plot(subtime, subcolumn, 'r-o', label="PM1")
    plt.xticks(fontsize=10, rotation=45)
    plt.xlabel("Time")
    plt.ylabel("Concentration")
    plt.grid(True)
    plt.show()


def identify_PM1():
    data = pd.read_csv(filename)
    col = data['PM1'].dropna()
    time = data['Time'].dropna()
    """
        plt.plot(time, col, 'r-o', label='PM1')
        plt.xlabel('Time')
        plt.ylabel('Concentration')
        plt.show()
        """

    # day 1
    st_125 = ("13:47:02", '13:59:47', "14:21:45", "14:34:36", "15:09:36", "15:20:06")

    st_42_portauthority = ("14:21:45", "14:34:36")
    barclayCenter = ("15:09:36", "15:20:06")
    # day 2
    st_42_bryantpark = ()
    st_74 = ()
    courtsquare = ()
    fulton = ()
    # day 3
    st_137 = ()
    st_225 = ()
    st_242 = ()

    startIndex = time[time == st_125[0]].index.values[0]
    endIndex = time[time == st_125[1]].index.values[0]

    subcolumn = col[startIndex: endIndex]
    subtime = time[startIndex: endIndex]

    print(startIndex)
    print(endIndex)

    plt.plot(subtime, subcolumn, 'r-o', label="PM1")
    plt.xticks(fontsize=10, rotation=45)
    plt.xlabel("Time")
    plt.ylabel("Concentration")
    plt.grid(True)
    plt.show()


def identify_Relhum():
    data = pd.read_csv(filename)
    col = data['RELHUM'].dropna()
    time = data['Time'].dropna()

    # day 1
    st_125 = ("13:47:02", '13:59:47', "14:21:45", "14:34:36", "15:09:36", "15:20:06")

    st_42_portauthority = ("14:21:45", "14:34:36")
    barclayCenter = ("15:09:36", "15:20:06")
    # day 2
    st_42_bryantpark = ()
    st_74 = ()
    courtsquare = ()
    fulton = ()
    # day 3
    st_137 = ()
    st_225 = ()
    st_242 = ()

    startIndex = time[time == st_125[0]].index.values[0]
    endIndex = time[time == st_125[1]].index.values[0]

    subcolumn = col[startIndex: endIndex]
    subtime = time[startIndex: endIndex]

    print(startIndex)
    print(endIndex)

    plt.plot(subtime, subcolumn, 'r-o', label="Relative Humidity")
    plt.xticks(fontsize=10, rotation=45)
    plt.xlabel("Time")
    plt.ylabel("Relative Humidity")
    plt.grid(True)
    plt.show()


def identify_Pressure():
    data = pd.read_csv(filename)
    col = data['PRES(HPA)'].dropna()
    time = data['Time'].dropna()

    # day 1
    st_125 = ("13:47:02", '13:59:47', "14:21:45", "14:34:36", "15:09:36", "15:20:06")

    st_42_portauthority = ("14:21:45", "14:34:36")
    barclayCenter = ("15:09:36", "15:20:06")
    # day 2
    st_42_bryantpark = ()
    st_74 = ()
    courtsquare = ()
    fulton = ()
    # day 3
    st_137 = ()
    st_225 = ()
    st_242 = ()

    startIndex = time[time == st_125[0]].index.values[0]
    endIndex = time[time == st_125[1]].index.values[0]

    subcolumn = col[startIndex: endIndex]
    subtime = time[startIndex: endIndex]

    print(startIndex)
    print(endIndex)

    plt.plot(subtime, subcolumn, 'r-o', label="Pressure (HPA)")
    plt.xticks(fontsize=10, rotation=45)
    plt.xlabel("Time")
    plt.ylabel("Concentration")
    plt.grid(True)
    plt.show()


def calculate_heatIndex(data):

    relative_humidity = data['RELHUM'].dropna()
    temp = (data['TEMP©'].dropna() * 9 / 5) + 32

    # use because of the dropna
    relative_humidity = relative_humidity.loc[temp.index]
    temp = temp.loc[relative_humidity.index]


    heatindex = (42.379 + 2.04901523 * temp + 10.14333127 * relative_humidity
                 - 0.22475541 * temp * relative_humidity
                 - 0.00683783 * temp ** 2
                 - 0.05481717 * relative_humidity ** 2
                 + 0.00122874 * temp ** 2 * relative_humidity
                 + 0.00085282 * temp * relative_humidity ** 2
                 - 0.00000199 * temp ** 2 * relative_humidity ** 2)


    condition1 = (relative_humidity < 13) & (temp >= 80) & (temp <= 112)
    adjustment1 = ((13 - relative_humidity) / 4) * np.sqrt((17 - np.abs(temp - 95)) / 17)
    heatindex[condition1] -= adjustment1[condition1]


    condition2 = (relative_humidity > 85) & (temp >= 80) & (temp <= 87)
    adjustment2 = ((relative_humidity - 85) / 10) * ((87 - temp) / 5)
    heatindex[condition2] += adjustment2[condition2]


    simple_HI = 0.5 * (temp + 61.0 + ((temp - 68.0) * 1.2) + (relative_humidity * 0.094))
    heatindex = np.where(heatindex < 80, simple_HI, heatindex)


    return pd.Series(heatindex, index=temp.index)


def plot_tempandheat():

    stations = {
        '125th St': ("13:47:02", '13:59:47'),
        '42nd St Port Authority': ("14:21:45", "14:34:36"),
        'Barclay Center': ("15:09:36", "15:20:06")
    }

    fig, ax = plt.subplots()

    for station_name, (start_time, end_time) in stations.items():

        station_data = data[(data['Time'] >= start_time) & (data['Time'] <= end_time)]

        if station_data.empty:
            print(f"No data for {station_name} in given time range")
            continue

        time = station_data['Time']
        temp = (station_data['TEMP©'] * 9 /5 ) + 32
        heatIndex = calculate_heatIndex(station_data)


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


plot_tempandheat()