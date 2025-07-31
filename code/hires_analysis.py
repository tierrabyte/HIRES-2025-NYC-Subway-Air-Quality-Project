import matplotlib.pyplot as plt

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
    # day 4
    'st_72' : ("14:45:40", "15:10:00"),
    'st_86' : ("15:13:42", "15:32:23"),
    'st_96' : ("15:36:19", "15:53:12")
}

def violin_plots(all_pm25, i, days):
    for a in all_pm25:
        plt.figure(figsize=(10, 6))
        plt.violinplot(a, showmeans=True, showmedians=True)
        plt.xticks(
            ticks=range(1, len(a) + 1),
            labels=list(days[i].keys()),
            rotation=45
        )
        plt.title("PM2.5 Distribution per Station")
        plt.ylabel("PM2.5 (µg/m³)")
        plt.tight_layout()
        plt.show()
        
        i += 1