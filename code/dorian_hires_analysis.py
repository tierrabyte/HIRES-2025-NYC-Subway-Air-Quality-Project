import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import numpy

file_7_14 = "C:\\Users\\Dorian\\project\\spatial_gradients\\1379_2025-7-14.csv"
file_7_15 = "C:\\Users\\Dorian\\project\\spatial_gradients\\1379_2025-7-15.csv"
file_7_16 = "C:\\Users\\Dorian\\project\\spatial_gradients\\1379_2025-7-16.csv"

    
def identify_pollutant():
    data = pd.read_csv(file_7_14)
    pm2 = data['PM2.5'].dropna()
    co = data['CO'].dropna()
    pm1 = data['PM1'].dropna()
    time = data['Time'].dropna()

    ref = pm1

    
    #day 1
    st_125_7_14 = ("13:47:02", "13:59:47")
    st_42_portauthority_7_14 = ("14:21:45" , "14:34:36")
    barclayCenter_7_14 = ("15:09:36", "15:20:06")

    #day 2
    st_125_bryantpark_7_15 = ("13:01:21", "13:33:56")
    st_42_bryantpark_7_15 = ("13:49:07", "14:22:00")
    st_74_7_15 = ("14:50:19", "15:23:40")
    courtsquare_7_15 = ("15:31:27", "15:52:07")
    fulton_7_15 = ("16:12:29", "16:22:27")

    #day 3
    st_137_7_16 = ("13:32:38", "13:52:25")
    st_225_7_16 = ("14:10:30", "14:20:00")
    st_242_7_16 = ("14:28:52", "14:38:52")
    


    startIndex = time[time == st_125_7_14[0]].index.values[0]
    endIndex = time[time == st_125_7_14[1]].index.values[0]

    # Find mean
    mean = ref[startIndex: endIndex].mean()
    print(mean)
    


    for t in time:
        dt.datetime.strptime(t, "%H:%M:%S")
        if st_125_7_14[0] <= t <= st_125_7_14[1]:
            print(t)


    

    subcolumn = pm1[startIndex: endIndex,]
    subtime = time[startIndex: endIndex]
    
    print(startIndex)
    print(endIndex)

    
    plt.plot(subtime, subcolumn, 'r-o', label = "PM2.5")
    plt.xticks(fontsize=10, rotation=45)
    plt.xlabel("Time")
    plt.ylabel("Concentration")
    plt.grid(True)
    #plt.show()
    

identify_pollutant()