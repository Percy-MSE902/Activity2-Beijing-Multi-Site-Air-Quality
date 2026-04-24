# Task 4: Data Filtering
import pandas as pd

df = pd.read_csv("data/cleaned_data.csv")

# ============================================
# Step 1: Checking station 
# ============================================
print("List of station:")
print(df["station"].unique())

# ============================================
# Step 2: Filtering interesting Station
# ============================================
dongsi = df[df["station"] == "Dongsi"]  
print(f"\nDongsi Station: {len(dongsi)} rows")
print(f"Mean of PM2.5 at Dongsi Station: {dongsi['PM2.5'].mean():.2f}")

# ============================================
# Step 3: Caomparing all station
# ============================================
print("\n--- Mean of PM2.5 of all station (High to Low) ---")
avg_pm25 = (
    df.groupby("station")["PM2.5"]
      .mean()
      .round(2)
      .sort_values(ascending=False)
)
print(avg_pm25)

# ============================================
# Step 4: ดูสถิติครบทุกสารมลพิษ ทุกสถานี
# ============================================
pollutants = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]
print("\n--- Mean of pollutants from each station ---")
summary = df.groupby("station")[pollutants].mean().round(2)
print(summary)