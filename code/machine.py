import os
import pandas as pd
import shap
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

#pip install pandas matplotlib seaborn shap scikit-learn


# === Folder setup ===


DATA_PATH = "PurpleAir"
OUTPUT_PATH = "station_plots"
os.makedirs(OUTPUT_PATH, exist_ok=True)

# === Feature columns ==='''
FEATURES = ["CO", "C02", "RELHUM", "TEMP", "PRESSURE"]

# === Time slicing dictionaries ===
# (Insert your actual dictionaries below)
day_1 = {
    "st_125" : ("13:47:02", '13:59:47'),
    "st_42_portauthority" : ("14:21:45", "14:34:36"),
    "barclayCenter" : ("15:09:36", "15:20:06")
}
day_2 = {
    "st_125_2" : ("13:01:17", "13:33:56"),
    "st_42_bryantpark" : ("13:49:03", "14:22:04"),
    "st_74" : ("14:50:19", "15:23:05"),
    "courtsquare" : ("15:31:27", "15:52:04"),
    "fulton" : ("16:12:29", "16:22:27")
}
day_3 = {
    "st_137" : ("13:32:38", "13:52:25"),
    "st_225" : ("14:10:31", "18:20:30"),
    "st_242" : ("18:28:43", "18:36:34")
}
day_4 = {
    'st_72' : ("14:45:40", "15:10:00"),
    'st_86' : ("15:13:42", "15:32:23"),
    'st_96' : ("15:36:19", "15:53:12")
}

# === Map of day data files to time windows ===
all_days = {
    "1379_2025-7-14 (1).csv": day_1,
    "1379_2025-7-15.csv": day_2,
    "1379_2025-7-16.csv": day_3,
    "1379_2025-7-24.csv": day_4
}

# === Analysis loop ===
for filename, station_times in all_days.items():
    print(f"\n Processing file: {filename}")
    try:
        df = pd.read_csv(os.path.join(DATA_PATH, filename))

        # Rename known columns
        df = df.rename(columns={
            "TEMP©": "TEMP",
            "PRES(HPA)": "PRESSURE",
            "Battery %": "Battery",
            "Cell-Strength()": "Signal",
            "Time": "Timestamp"
        })

        # Convert time to datetime
        df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")

        for station, (start_str, end_str) in station_times.items():
            print(f"  Station: {station}")
            start = pd.to_datetime(start_str)
            end = pd.to_datetime(end_str)

            df_station = df[(df["Timestamp"].dt.time >= start.time()) &
                            (df["Timestamp"].dt.time <= end.time())]

            df_station = df_station.dropna(subset=["PM2.5"] + FEATURES)

            X = df_station[FEATURES]
            y = df_station["PM2.5"]

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            model = RandomForestRegressor(n_estimators=100, random_state=42)
            model.fit(X_train, y_train)

            # === Plot Random Forest bar ===
            importances = pd.Series(model.feature_importances_, index=X.columns)
            plt.figure()
            sns.barplot(x=importances.values, y=importances.index, palette="viridis")
            plt.title(f"RF Feature Importance: {station}")
            plt.tight_layout()
            plt.savefig(os.path.join(OUTPUT_PATH, f"{filename}_{station}_rf.png"))
            plt.close()

            # === SHAP ===
            explainer = shap.TreeExplainer(model)
            shap_values = explainer.shap_values(X_test)

            # === Calculate average positive SHAP values ===
            import numpy as np

            shap_vals_array = np.array(shap_values)
            positive_mask = shap_vals_array > 0

            mean_positive_shap = []
            for i in range(shap_vals_array.shape[1]):
                if np.any(positive_mask[:, i]):
                    mean_val = shap_vals_array[:, i][positive_mask[:, i]].mean()
                else:
                    mean_val = 0
                mean_positive_shap.append(mean_val)

            mean_positive_shap_series = pd.Series(mean_positive_shap, index=X_test.columns)
            mean_positive_shap_series = mean_positive_shap_series.sort_values(ascending=False)

            print(f"Features most elevating PM2.5 at {station}:")
            print(mean_positive_shap_series)

            mean_positive_shap_series.to_csv(os.path.join(OUTPUT_PATH, f"{filename}_{station}_shap_positive_means.csv"))

            # SHAP bar plot
            shap.summary_plot(shap_values, X_test, plot_type="bar", show=False)
            plt.title(f"SHAP Bar: {station}")
            plt.tight_layout()
            plt.savefig(os.path.join(OUTPUT_PATH, f"{filename}_{station}_shap_bar.png"))
            plt.close()

            # SHAP beeswarm
            shap.summary_plot(shap_values, X_test, show=False)
            plt.title(f"SHAP Beeswarm: {station}")
            plt.tight_layout()
            plt.savefig(os.path.join(OUTPUT_PATH, f"{filename}_{station}_shap_swarm.png"))
            plt.close()

            print(f"   ✅ Saved plots for {station}")

    except Exception as e:
        print(f"Error in file {filename}: {e}")


