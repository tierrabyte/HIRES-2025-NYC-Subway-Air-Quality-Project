import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


def normalize_columns(df):
    # Clean column names first
    cleaned_cols = (
        df.columns.str.strip()
        .str.lower()
        .str.replace("©", "c", regex=False)
        .str.replace(" ", "", regex=False)
        .str.replace("_", "", regex=False)
    )
    df.columns = cleaned_cols

    # Map cleaned names to standard names
    COLUMN_STANDARDIZATION = {
        "time": "Time",
        "timestamp": "Datetime",      # handles outdoor
        "time_stamp": "Datetime",     # extra safeguard
        "datetime": "Datetime",
        "pm1": "PM 1.0",
        "pm1.0": "PM 1.0",
        "pm1.0atm": "PM 1.0",
        "pm10": "PM 10.0",
        "pm10.0": "PM 10.0",
        "pm10.0atm": "PM 10.0",
        "pm25": "PM 2.5",
        "pm2.5": "PM 2.5",
        "pm25atm": "PM 2.5",
        "pm2.5atm": "PM 2.5",
        "relhum": "Relative Humidity",
        "humidity": "Relative Humidity",
        "tempc": "Temperature",
        "temperature": "Temperature",
        "preshpa": "Pressure",
        "pressure": "Pressure",
        "date": "Date"
    }

    df.rename(columns={col: COLUMN_STANDARDIZATION.get(col, col) for col in df.columns}, inplace=True)
    df = df.loc[:, ~df.columns.duplicated()]
    return df

station_time_stamps = {
    "2025-07-14": {
        "st_125": {"indoor": ("13:47:02", "13:59:47"), "outdoor": ("2025-07-14T13:46:32-04:00", "2025-07-14T13:58:32-04:00")},
        "portauthority_42": {"indoor": ("14:21:45", "14:34:36"), "outdoor": ("2025-07-14T14:20:12-04:00", "2025-07-14T14:34:12-04:00")},
        "barclaycenter": {"indoor": ("15:09:36", "15:20:06"), "outdoor": ("2025-07-14T15:08:46-04:00", "2025-07-14T15:20:46-04:00")},
    },
    "2025-07-15": {
        "st_125": {"indoor": ("13:01:17", "13:33:56"), "outdoor": ("2025-07-15T13:00:45-04:00", "2025-07-15T13:32:45-04:00")},
        "bryantpark_42": {"indoor": ("13:49:03", "14:22:04"), "outdoor": ("2025-07-15T13:58:23-04:00", "2025-07-15T14:22:23-04:00")},
        "broadway_roosevelt_74th": {"indoor": ("14:50:19", "15:23:05"), "outdoor": ("2025-07-15T14:49:35-04:00", "2025-07-15T15:23:36-04:00")},
        "courtSquare": {"indoor": ("15:31:27", "15:52:04"), "outdoor": ("2025-07-15T15:30:57-04:00", "2025-07-15T15:52:57-04:00")},
        "fultonstreet": {"indoor": ("16:12:29", "16:22:27"), "outdoor": ("2025-07-15T16:12:21-04:00", "2025-07-15T16:22:21-04:00")},
    },
    "2025-07-16": {
        "st_137": {"indoor": ("13:32:38", "13:52:25"), "outdoor": ("2025-07-16T13:33:24-04:00", "2025-07-16T13:53:23-04:00")},
        "st_225": {"indoor": ("14:10:31", "14:20:30"), "outdoor": ("2025-07-16T14:11:18-04:00", "2025-07-16T14:21:18-04:00")},
        "st_242": {"indoor": ("14:28:43", "14:36:34"), "outdoor": ("2025-07-16T14:29:13-04:00", "2025-07-16T14:37:13-04:00")},
    },
    "2025-07-24": {
        "st_72": {"indoor": ("14:45:40", "15:10:00"), "outdoor": ("2025-07-24T14:44:28-04:00", "2025-07-24T15:10:28-04:00")},
        "st_86": {"indoor": ("15:13:42", "15:32:23"), "outdoor": ("2025-07-24T15:13:47-04:00", "2025-07-24T15:33:47-04:00")},
        "st_96": {"indoor": ("15:36:19", "15:53:12"), "outdoor": ("2025-07-24T15:37:01-04:00", "2025-07-24T15:53:01-04:00")},
    }
}

station_to_csv_mapping = {
     "2025-07-14": {
        "st_125": {"indoor": "1379_2025-7-14.csv", "outdoor": "st-125_7-14_82929.csv"},
        "portauthority_42": {"indoor": "1379_2025-7-14.csv", "outdoor": "portauth_07-14_29183.csv"},
        "barclaycenter": {"indoor": "1379_2025-7-14.csv", "outdoor": "barclay_7-14_143784.csv"},
    },
    "2025-07-15": {
        "st_125": {"indoor": "1379_2025-7-15.csv", "outdoor": "st-125_7-15_82929.csv "},
        "bryantpark_42": {"indoor": "1379_2025-7-15.csv", "outdoor": "bryantpark_07-15_29183.csv"},
        "broadway_roosevelt_74th": {"indoor": "1379_2025-7-15.csv", "outdoor": "st-74_7-15_128551.csv"},
        "courtSquare": {"indoor": "1379_2025-7-15.csv", "outdoor": "courtsq_7-15_147789.csv"},
        "fultonstreet": {"indoor": "1379_2025-7-15.csv", "outdoor": "fulton_7-15_143784.csv"},
    },
    "2025-07-16": {
        "st_137": {"indoor": "1379_2025-7-16.csv", "outdoor": "st-137_7-16_188651.csv "},
        "st_225": {"indoor": "1379_2025-7-16.csv", "outdoor": "st-225_7-16_140062.csv"},
        "st_242": {"indoor": "1379_2025-7-16.csv", "outdoor": "st-242_7-16_188617.csv"},
    },
    "2025-07-24": {
        "st_72": {"indoor": "1379_2025-7-24.csv", "outdoor": "st-72_7-24_82031.csv"},
        "st_86": {"indoor": "1379_2025-7-24.csv", "outdoor": "st-86_7-24_257889.csv"},
        "st_96": {"indoor": "1379_2025-7-24.csv", "outdoor": "st-96_7-24_43527.csv"},
    }

}

def load_and_prepare_csv(path, is_indoor=False):
    """
    Loads a CSV file, normalizes its columns, and prepares the Datetime column.
    For indoor files, ignores 'Time stamp' and combines 'Date' and 'Time'.
    For outdoor files, uses 'Datetime' column from 'time_stamp' mapping.
    """
    df = pd.read_csv(path)
    df = normalize_columns(df)

    if is_indoor:
        # Remove the 'Time stamp' column if it exists
        if "Time stamp" in df.columns:
            df.drop(columns=["Time stamp"], inplace=True, errors="ignore")
        
        # Find correct Date and Time columns
        date_col = next((c for c in df.columns if c.lower() == "date"), None)
        time_col = next((c for c in df.columns if c.lower() == "time"), None)

        if date_col and time_col:
            df = df.dropna(subset=[date_col, time_col])
            df["Datetime"] = pd.to_datetime(
                df[date_col].astype(str) + " " + df[time_col].astype(str),
                errors="coerce"
            )
            df = df.dropna(subset=["Datetime"])
        else:
            raise ValueError(f"Indoor file {path} missing 'Date' or 'Time'.")
    else:
        # Outdoor files use already mapped 'Datetime'
        datetime_col = next((c for c in df.columns if c.lower() == "datetime"), None)
        if datetime_col:
            df = df.dropna(subset=[datetime_col])
            df["Datetime"] = pd.to_datetime(df[datetime_col], errors="coerce")
            df = df.dropna(subset=["Datetime"])
        else:
            raise ValueError(f"Outdoor file {path} missing 'Datetime' column.")

    return df

#Plot functions
def plot_station_time_series(station, date, station_time_stamps, station_to_csv_mapping, base_path="C://Users//Angy//Documents//iaq_analysis//HIRES-2025-NYC-Subway-Air-Quality-Project//data//", output_dir="plots"):
    """
    Plot time series data for a specific station (indoor & outdoor) and save as PNG.
    Indoor times are shifted +4 hours to match outdoor local time.
    """
    os.makedirs(output_dir, exist_ok=True)

    indoor_file = station_to_csv_mapping[date][station]['indoor'].strip()
    outdoor_file = station_to_csv_mapping[date][station]['outdoor'].strip()

    indoor_df = load_and_prepare_csv(f"{base_path}{indoor_file}", is_indoor=True)
    outdoor_df = load_and_prepare_csv(f"{base_path}{outdoor_file}", is_indoor=False)

    # Shift indoor times
    indoor_df["Datetime"] = indoor_df["Datetime"] + pd.Timedelta(hours=4)

    # Get station time ranges
    indoor_start, indoor_end = station_time_stamps[date][station]["indoor"]
    outdoor_start, outdoor_end = station_time_stamps[date][station]["outdoor"]

    # Shift indoor filter times
    indoor_start_dt = pd.to_datetime(f"{date} {indoor_start}") + pd.Timedelta(hours=4)
    indoor_end_dt = pd.to_datetime(f"{date} {indoor_end}") + pd.Timedelta(hours=4)

    # Filter data
    indoor_filtered = indoor_df[(indoor_df["Datetime"] >= indoor_start_dt) &
                                (indoor_df["Datetime"] <= indoor_end_dt)]
    outdoor_filtered = outdoor_df[(outdoor_df["Datetime"] >= pd.to_datetime(outdoor_start)) &
                                  (outdoor_df["Datetime"] <= pd.to_datetime(outdoor_end))]

    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(indoor_filtered["Datetime"], indoor_filtered["PM 2.5"], label="Indoor PM 2.5")
    plt.plot(outdoor_filtered["Datetime"], outdoor_filtered["PM 2.5"], label="Outdoor PM 2.5")
    plt.title(f"{station} - {date}")
    plt.xlabel("Time")
    plt.ylabel("PM 2.5")
    plt.legend()

    file_path = os.path.join(output_dir, f"{date}_{station}_timeseries.png")
    plt.savefig(file_path, dpi=300)
    plt.close()


def violin_plot_station(station, date, station_time_stamps, station_to_csv_mapping, base_path="C://Users//Angy//Documents//iaq_analysis//HIRES-2025-NYC-Subway-Air-Quality-Project//data//", output_dir="plots"):
    """
    Make violin plots for indoor and outdoor PM 2.5 data of a specific station and save as PNG.
    Indoor times are shifted +4 hours to match outdoor local time.
    """
    os.makedirs(output_dir, exist_ok=True)

    indoor_file = station_to_csv_mapping[date][station]['indoor'].strip()
    outdoor_file = station_to_csv_mapping[date][station]['outdoor'].strip()

    indoor_df = load_and_prepare_csv(f"{base_path}{indoor_file}", is_indoor=True)
    outdoor_df = load_and_prepare_csv(f"{base_path}{outdoor_file}", is_indoor=False)

    # Shift indoor times
    indoor_df["Datetime"] = indoor_df["Datetime"] + pd.Timedelta(hours=4)

    # Get station time ranges
    indoor_start, indoor_end = station_time_stamps[date][station]["indoor"]
    outdoor_start, outdoor_end = station_time_stamps[date][station]["outdoor"]

    # Shift indoor filter times
    indoor_start_dt = pd.to_datetime(f"{date} {indoor_start}") + pd.Timedelta(hours=4)
    indoor_end_dt = pd.to_datetime(f"{date} {indoor_end}") + pd.Timedelta(hours=4)

    # Filter data
    indoor_filtered = indoor_df[(indoor_df["Datetime"] >= indoor_start_dt) &
                                (indoor_df["Datetime"] <= indoor_end_dt)]
    outdoor_filtered = outdoor_df[(outdoor_df["Datetime"] >= pd.to_datetime(outdoor_start)) &
                                  (outdoor_df["Datetime"] <= pd.to_datetime(outdoor_end))]

    # Label and combine
    indoor_filtered = indoor_filtered.copy()
    outdoor_filtered = outdoor_filtered.copy()
    indoor_filtered["Type"] = "Indoor"
    outdoor_filtered["Type"] = "Outdoor"

    combined_df = pd.concat([indoor_filtered[["PM 2.5", "Type"]], outdoor_filtered[["PM 2.5", "Type"]]])

    # Plot
    plt.figure(figsize=(8, 5))
    sns.violinplot(x="Type", y="PM 2.5", data=combined_df)
    plt.title(f"Violin Plot - {station} ({date})")

    file_path = os.path.join(output_dir, f"{date}_{station}_violin.png")
    plt.savefig(file_path, dpi=300)
    plt.close()


def plot_all_stations_all_days(station_time_stamps, station_to_csv_mapping, base_path="C://Users//Angy//Documents//iaq_analysis//HIRES-2025-NYC-Subway-Air-Quality-Project//data//", output_dir="plots"):
    """
    Loops through all dates and stations, saving time series and violin plots.
    """
    for date in station_time_stamps:
        for station in station_time_stamps[date]:
            try:
                print(f"Saving plots for {station} on {date}...")
                plot_station_time_series(station, date, station_time_stamps, station_to_csv_mapping, base_path, output_dir)
                violin_plot_station(station, date, station_time_stamps, station_to_csv_mapping, base_path, output_dir)
            except Exception as e:
                print(f"Error plotting {station} on {date}: {e}")



def violin_plot_all_days(station_time_stamps, station_to_csv_mapping, base_path="C://Users//Angy//Documents//iaq_analysis//HIRES-2025-NYC-Subway-Air-Quality-Project//data//", output_dir="plots"):
    """
    Creates a violin plot for all stations for each date in station_time_stamps.
    Indoor and outdoor data are side-by-side for each station.
    """
    os.makedirs(output_dir, exist_ok=True)

    for date in station_time_stamps:
        print(f"Processing violin plot for {date}...")
        all_data = []

        for station in station_time_stamps[date]:
            try:
                # Load indoor & outdoor data
                indoor_file = station_to_csv_mapping[date][station]['indoor'].strip()
                outdoor_file = station_to_csv_mapping[date][station]['outdoor'].strip()

                indoor_df = load_and_prepare_csv(f"{base_path}{indoor_file}", is_indoor=True)
                outdoor_df = load_and_prepare_csv(f"{base_path}{outdoor_file}", is_indoor=False)

                # Shift indoor time +4 hours
                indoor_df["Datetime"] = indoor_df["Datetime"] + pd.Timedelta(hours=4)

                # Time ranges
                indoor_start, indoor_end = station_time_stamps[date][station]["indoor"]
                outdoor_start, outdoor_end = station_time_stamps[date][station]["outdoor"]

                # Shift indoor filter times
                indoor_start_dt = pd.to_datetime(f"{date} {indoor_start}") + pd.Timedelta(hours=4)
                indoor_end_dt = pd.to_datetime(f"{date} {indoor_end}") + pd.Timedelta(hours=4)

                # Filter
                indoor_filtered = indoor_df[(indoor_df["Datetime"] >= indoor_start_dt) &
                                            (indoor_df["Datetime"] <= indoor_end_dt)]
                outdoor_filtered = outdoor_df[(outdoor_df["Datetime"] >= pd.to_datetime(outdoor_start)) &
                                              (outdoor_df["Datetime"] <= pd.to_datetime(outdoor_end))]

                # Label for plotting
                indoor_filtered = indoor_filtered.copy()
                outdoor_filtered = outdoor_filtered.copy()
                indoor_filtered["Station"] = f"{station} - Indoor"
                outdoor_filtered["Station"] = f"{station} - Outdoor"

                # Append
                all_data.append(indoor_filtered[["PM 2.5", "Station"]])
                all_data.append(outdoor_filtered[["PM 2.5", "Station"]])

            except Exception as e:
                print(f"Skipping {station} on {date}: {e}")

        # Only plot if we have data
        if all_data:
            combined_df = pd.concat(all_data)

            plt.figure(figsize=(14, 6))
            sns.violinplot(x="Station", y="PM 2.5", data=combined_df, palette="Set2")
            plt.title(f"PM 2.5 Violin Plot - All Stations ({date})")
            plt.xticks(rotation=45, ha="right")

            file_path = os.path.join(output_dir, f"{date}_all_stations_violin.png")
            plt.savefig(file_path, dpi=300, bbox_inches="tight")
            plt.close()
        else:
            print(f"No data available for {date}.")


def timeseries_plot_all_stations_per_day(station_time_stamps, station_to_csv_mapping, base_path="C://Users//Angy//Documents//iaq_analysis//HIRES-2025-NYC-Subway-Air-Quality-Project//data//", output_dir="plots"):
    """
    Creates a time series plot of all stations (indoor & outdoor) for each date.
    Saves one plot per day.
    """
    os.makedirs(output_dir, exist_ok=True)

    for date in station_time_stamps:
        print(f"Processing time series for {date}...")
        plt.figure(figsize=(14, 6))

        for station in station_time_stamps[date]:
            try:
                # Load indoor & outdoor data
                indoor_file = station_to_csv_mapping[date][station]['indoor'].strip()
                outdoor_file = station_to_csv_mapping[date][station]['outdoor'].strip()

                indoor_df = load_and_prepare_csv(f"{base_path}{indoor_file}", is_indoor=True)
                outdoor_df = load_and_prepare_csv(f"{base_path}{outdoor_file}", is_indoor=False)

                # Shift indoor time +4 hours
                indoor_df["Datetime"] = indoor_df["Datetime"] + pd.Timedelta(hours=4)

                # Time ranges
                indoor_start, indoor_end = station_time_stamps[date][station]["indoor"]
                outdoor_start, outdoor_end = station_time_stamps[date][station]["outdoor"]

                # Shift indoor filter times
                indoor_start_dt = pd.to_datetime(f"{date} {indoor_start}") + pd.Timedelta(hours=4)
                indoor_end_dt = pd.to_datetime(f"{date} {indoor_end}") + pd.Timedelta(hours=4)

                # Filter data
                indoor_filtered = indoor_df[(indoor_df["Datetime"] >= indoor_start_dt) &
                                            (indoor_df["Datetime"] <= indoor_end_dt)]
                outdoor_filtered = outdoor_df[(outdoor_df["Datetime"] >= pd.to_datetime(outdoor_start)) &
                                              (outdoor_df["Datetime"] <= pd.to_datetime(outdoor_end))]

                # Plot indoor and outdoor
                plt.plot(indoor_filtered["Datetime"], indoor_filtered["PM 2.5"], label=f"{station} - Indoor")
                plt.plot(outdoor_filtered["Datetime"], outdoor_filtered["PM 2.5"], label=f"{station} - Outdoor")

            except Exception as e:
                print(f"Skipping {station} on {date}: {e}")

        plt.title(f"PM 2.5 Time Series - All Stations ({date})")
        plt.xlabel("Time")
        plt.ylabel("PM 2.5")
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()

        file_path = os.path.join(output_dir, f"{date}_all_stations_timeseries.png")
        plt.savefig(file_path, dpi=300, bbox_inches="tight")
        plt.close()


def combined_violin_all_days(station_time_stamps, station_to_csv_mapping, base_path="C://Users//Angy//Documents//iaq_analysis//HIRES-2025-NYC-Subway-Air-Quality-Project//data//", output_dir="plots"):
    """
    Creates one big violin plot for all stations across all days.
    """
    os.makedirs(output_dir, exist_ok=True)
    all_data = []

    for date in station_time_stamps:
        for station in station_time_stamps[date]:
            try:
                indoor_file = station_to_csv_mapping[date][station]['indoor'].strip()
                outdoor_file = station_to_csv_mapping[date][station]['outdoor'].strip()

                indoor_df = load_and_prepare_csv(f"{base_path}{indoor_file}", is_indoor=True)
                outdoor_df = load_and_prepare_csv(f"{base_path}{outdoor_file}", is_indoor=False)

                # Shift indoor +4h
                indoor_df["Datetime"] = indoor_df["Datetime"] + pd.Timedelta(hours=4)

                indoor_start, indoor_end = station_time_stamps[date][station]["indoor"]
                outdoor_start, outdoor_end = station_time_stamps[date][station]["outdoor"]

                indoor_start_dt = pd.to_datetime(f"{date} {indoor_start}") + pd.Timedelta(hours=4)
                indoor_end_dt = pd.to_datetime(f"{date} {indoor_end}") + pd.Timedelta(hours=4)

                indoor_filtered = indoor_df[(indoor_df["Datetime"] >= indoor_start_dt) &
                                            (indoor_df["Datetime"] <= indoor_end_dt)]
                outdoor_filtered = outdoor_df[(outdoor_df["Datetime"] >= pd.to_datetime(outdoor_start)) &
                                              (outdoor_df["Datetime"] <= pd.to_datetime(outdoor_end))]

                indoor_filtered = indoor_filtered.copy()
                outdoor_filtered = outdoor_filtered.copy()
                indoor_filtered["Station"] = f"{station} ({date}) - Indoor"
                outdoor_filtered["Station"] = f"{station} ({date}) - Outdoor"

                all_data.append(indoor_filtered[["PM 2.5", "Station"]])
                all_data.append(outdoor_filtered[["PM 2.5", "Station"]])

            except Exception as e:
                print(f"Skipping {station} on {date}: {e}")

    if not all_data:
        print("No data available for combined violin plot.")
        return

    combined_df = pd.concat(all_data)

    plt.figure(figsize=(20, 8))
    sns.violinplot(x="Station", y="PM 2.5", data=combined_df, palette="Set2")
    plt.title("PM 2.5 Violin Plot - All Stations & Days")
    plt.xticks(rotation=90)
    file_path = os.path.join(output_dir, "all_days_all_stations_violin.png")
    plt.savefig(file_path, dpi=300, bbox_inches="tight")
    plt.close()


def combined_timeseries_all_days(station_time_stamps, station_to_csv_mapping, base_path="C://Users//Angy//Documents//iaq_analysis//HIRES-2025-NYC-Subway-Air-Quality-Project//data//", output_dir="plots"):
    """
    Creates one big time series plot for all stations across all days.
    """
    os.makedirs(output_dir, exist_ok=True)
    plt.figure(figsize=(20, 8))

    for date in station_time_stamps:
        for station in station_time_stamps[date]:
            try:
                indoor_file = station_to_csv_mapping[date][station]['indoor'].strip()
                outdoor_file = station_to_csv_mapping[date][station]['outdoor'].strip()

                indoor_df = load_and_prepare_csv(f"{base_path}{indoor_file}", is_indoor=True)
                outdoor_df = load_and_prepare_csv(f"{base_path}{outdoor_file}", is_indoor=False)

                indoor_df["Datetime"] = indoor_df["Datetime"] + pd.Timedelta(hours=4)

                indoor_start, indoor_end = station_time_stamps[date][station]["indoor"]
                outdoor_start, outdoor_end = station_time_stamps[date][station]["outdoor"]

                indoor_start_dt = pd.to_datetime(f"{date} {indoor_start}") + pd.Timedelta(hours=4)
                indoor_end_dt = pd.to_datetime(f"{date} {indoor_end}") + pd.Timedelta(hours=4)

                indoor_filtered = indoor_df[(indoor_df["Datetime"] >= indoor_start_dt) &
                                            (indoor_df["Datetime"] <= indoor_end_dt)]
                outdoor_filtered = outdoor_df[(outdoor_df["Datetime"] >= pd.to_datetime(outdoor_start)) &
                                              (outdoor_df["Datetime"] <= pd.to_datetime(outdoor_end))]

                plt.plot(indoor_filtered["Datetime"], indoor_filtered["PM 2.5"], label=f"{station} - Indoor")
                plt.plot(outdoor_filtered["Datetime"], outdoor_filtered["PM 2.5"], label=f"{station} - Outdoor")

            except Exception as e:
                print(f"Skipping {station} on {date}: {e}")

    plt.title("PM 2.5 Time Series - All Stations & Days")
    plt.xlabel("Time")
    plt.ylabel("PM 2.5")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

    file_path = os.path.join(output_dir, "all_days_all_stations_timeseries.png")
    plt.savefig(file_path, dpi=300, bbox_inches="tight")
    plt.close()



# Run batch plotting for all stations and dates

base_path = "C://Users//Angy//Documents//iaq_analysis//HIRES-2025-NYC-Subway-Air-Quality-Project//data//"
plot_all_stations_all_days(station_time_stamps, station_to_csv_mapping, base_path)

violin_plot_all_days(station_time_stamps, station_to_csv_mapping, base_path)

timeseries_plot_all_stations_per_day(station_time_stamps, station_to_csv_mapping, base_path)

#combined_timeseries_all_days(station_time_stamps, station_to_csv_mapping, base_path)   ifnore since hard to visualize when condensed into one plot

combined_violin_all_days(station_time_stamps, station_to_csv_mapping, base_path)
