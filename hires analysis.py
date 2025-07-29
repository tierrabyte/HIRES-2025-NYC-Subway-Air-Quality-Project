import pandas as pd
import matplotlib.pyplot as plt

filename = "C:\\Users\\Angy\\Documents\\iaq_analysis\\hires_project\\1379_2025-7-14.csv"


    
def identify_pollutant():
    data = pd.read_csv(filename)
    col = data['PM2.5'].dropna()
    time = data['Time'].dropna()
    """
    plt.plot(time, col, 'r-o', label='PM2.5')
    plt.xlabel('Time')
    plt.ylabel('Concentration')
    plt.show()
    """
    
    #day 1
    st_125 = ("13:47:02", '13:59:47')
    st_42_portauthority = ("14:21:45" , "14:34:36")
    barclayCenter = ("15:09:36", "15:20:06")
    #day 2
    st_42_bryantpark  = ()
    st_74 = ()
    courtsquare = ()
    fulton = ()
    #day 3
    st_137 = ()
    st_225 = ()
    st_242 = ()


    

    #print(st_125[0])
    startIndex =time[time == st_125[0]].index.values[0]
    endIndex = time[time == st_125[1]].index.values[0]

    subcolumn = col[startIndex: endIndex]
    subtime = time[startIndex: endIndex]

    print(startIndex)
    print(endIndex)

    plt.plot(subtime,subcolumn, 'r-o', label = "PM2.5")
    plt.xticks(fontsize=10, rotation=45)
    plt.xlabel("Time")
    plt.ylabel("Concentration")
    plt.grid(True)
    plt.show()

identify_pollutant()