from hires_analysis_functions import (
    plot_all_stations_all_days,
    violin_plot_all_days,
    timeseries_plot_all_stations_per_day,
    combined_timeseries_all_days,
    combined_violin_all_days
)

# Run batch plotting for all stations and dates

base_path = "C://Users//Angy//Documents//iaq_analysis//HIRES-2025-NYC-Subway-Air-Quality-Project//data//"
plot_all_stations_all_days(station_time_stamps, station_to_csv_mapping, base_path)

violin_plot_all_days(station_time_stamps, station_to_csv_mapping, base_path)

timeseries_plot_all_stations_per_day(station_time_stamps, station_to_csv_mapping, base_path)

#combined_timeseries_all_days(station_time_stamps, station_to_csv_mapping, base_path)   ifnore since hard to visualize when condensed into one plot

combined_violin_all_days(station_time_stamps, station_to_csv_mapping, base_path)