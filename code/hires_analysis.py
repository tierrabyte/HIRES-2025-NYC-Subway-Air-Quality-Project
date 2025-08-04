import matplotlib.pyplot as plt

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


day1 = {
    "st_125" : ("2025-07-14T13:46:32-04:00", '2025-07-14T13:58:32-04:00'),
    "portauthority_42" : ("2025-07-14T14:20:12-04:00", "2025-07-14T14:34:12-04:00"),
    "barclaycenter" : ("2025-07-14T15:08:46-04:00", "2025-07-14T15:20:46-04:00"),
}


day2 = {
    "st_125_15" : ("2025-07-15T13:00:45-04:00", "2025-07-15T13:32:45-04:00" ),
    "bryantpark_42" : ("2025-07-15T13:58:23-04:00", "2025-07-15T14:22:23-04:00"),
    "broadway_roosevelt_74th" : ("2025-07-15T14:49:35-04:00", "2025-07-15T15:23:36-04:00"),
    "courtSquare" : ("2025-07-15T15:30:57-04:00", "2025-07-15T15:52:57-04:00"),
    "fultonstreet" : ("2025-07-15T16:12:21-04:00", "2025-07-15T16:22:21-04:00"),
}