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
    temp = (data['TEMP©'].dropna() * 9 / 5) + 32  #fix header in csv and adjust header reference

    heatindex = #initial equation
    condition1 = (rh<13) & (temp <= 80) & (temp >= 112) #first logic condition
    heatindex += #adjustment eq for first logic condition
    #repeat for second logic condition

    heatindex = np.where() #use this function to apply simplified equation, try it work it out yourself first! 

    '''

    heatindex = 42.379 + 2.04901523 * temp + 10.14333127 * relative_humidity - .22475541 * temp * relative_humidity - (
                0.00683783 * temp * temp) - .05481717 * relative_humidity * relative_humidity + .00122874 * temp * temp * relative_humidity + .00085282 * temp * relative_humidity * relative_humidity - .00000199 * temp * temp * relative_humidity * relative_humidity
    if relative_humidity.any() < 13 and (80 <= temp.any() <= 112):
        heatindex = heatindex - ((13 - relative_humidity) / 4) * math.sqrt((17 - abs(temp - 95)) / 17)
    elif relative_humidity.any() > 85 & ( 80 <= temp.any() <= 87):
        heatindex = heatindex + ((relative_humidity - 85) / 10) * ((87 - temp) / 5)

    if heatindex.any() < 80:
        heatindex = 0.5 * (temp + 61.0 + ((temp - 68.0) * 1.2) + (relative_humidity * 0.094))
    '''
    return heatindex


def plot_tempandheat():
    temp = data['TEMP©']
    time = data['Time']
    heatIndex = calculate_heatIndex(data)

    #print length of all three dataframes so make sure theyre the same length ^ 

    fig, ax = plt.subplots()
    ax.plot(time,temp)
    ax.plot(time, heatIndex)
    ax.set_title('Temperature & Heat Index')

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


plot_tempandheat()
