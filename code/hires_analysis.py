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


