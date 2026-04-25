# 🌫️ Beijing Multi-Site Air Quality Analysis

---

## 📹 Video Presentation
🎬 


---

## 🧹 Task 2 — Data Cleaning

**Objective:** Handle missing values to prepare a clean dataset.

### Steps Taken

**Step 1 — Identify Missing Values**
```python
missing = df.isnull().sum()
print(missing[missing > 0])
```

**Step 2 — Fill with Column Mean**
```python
for col in ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]:
    df[col] = df[col].fillna(df[col].mean())
```

**Step 3 — Drop Remaining Null Rows**
```python
before = len(df)
df = df.dropna()
after = len(df)
print(f"Removed {before - after} rows")
```

### Results
- Missing values found in all 6 pollutant columns
  <img width="278" height="280" alt="Screenshot 2569-04-25 at 12 20 09 AM" src="https://github.com/user-attachments/assets/bb3a4c22-989e-4e5b-91fb-8700bb975d36" />

- Filled with column mean to preserve data volume  
- Remaining rows with NaN dropped  
- Output saved as `data/cleaned_data.csv` ✅
- Final verification: `df.isnull().sum().sum() == 0`

---

## 📈 Task 3 — Basic Statistical Analysis

**Objective:** Summarise PM2.5 and other pollutants using core statistics.

```python
pollutants = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]
print(df[pollutants].describe().round(2))
```

### Results — PM2.5

<img width="158" height="581" alt="Screenshot 2569-04-25 at 12 19 17 AM" src="https://github.com/user-attachments/assets/d2c3e990-df6d-4498-993b-a7e50d24cea3" />

### 🔍 Key Insight
> **Mean (77.4) is significantly higher than Median (51.0)**  
> This indicates a **right-skewed distribution** — most days have moderate pollution, but extreme pollution spikes (especially in winter) pull the average upward.

---

## 🔍 Task 4 — Data Filtering

**Objective:** Filter data by station and compare average PM2.5 levels.

```python
# Filter single station
dongsi = df[df["station"] == "Dongsi"]
print(f"Dongsi avg PM2.5: {dongsi['PM2.5'].mean():.2f}")

# Compare all stations
avg_pm25 = df.groupby("station")["PM2.5"].mean().round(2).sort_values(ascending=False)
print(avg_pm25)
```

### Results — Average PM2.5 by Station (µg/m³)

<img width="491" height="576" alt="Screenshot 2569-04-25 at 12 25 00 AM" src="https://github.com/user-attachments/assets/8ec835f6-dc39-43d3-b8ca-6aab0edb2ac3" />


### 🔍 Key Insight
> Urban stations (Gucheng, Dongsi) show **~65% higher** PM2.5 than rural stations (Huairou, Dingling), reflecting the impact of traffic, industry, and population density on air quality.

---

## 📉 Task 5 — Data Visualization

**Objective:** Create 3 charts to visually explore PM2.5 patterns.

### Chart 1 — Histogram of PM2.5

```python
df["PM2.5"].hist(bins=50, color="steelblue", edgecolor="white")
plt.title("Distribution of PM2.5")
plt.savefig("histogram_pm25.png")
```
<img width="800" height="500" alt="histogram_pm25" src="https://github.com/user-attachments/assets/d6349e92-0159-4f24-9761-85dae818696e" />

> **Interpretation:** Strong right skew — majority of readings below 100 µg/m³, but a long tail extends to 999, indicating severe pollution episodes.

---

### Chart 2 — Monthly PM2.5 Trend (Line Plot)

```python
monthly = df.groupby(["year","month"])["PM2.5"].mean().reset_index()
plt.plot(monthly["date"], monthly["PM2.5"], color="tomato")
plt.savefig("lineplot_pm25.png")
```
<img width="1200" height="500" alt="lineplot_pm25" src="https://github.com/user-attachments/assets/1e444a24-9b26-419f-b2bb-88e01a6fd9da" /> 

> **Interpretation:** Clear seasonal cycle — PM2.5 peaks every **November–January** (winter), driven by cold stagnant air and coal heating. Summer months consistently lower.

---

### Chart 3 — Boxplot of Pollutants

```python
df[["PM2.5","PM10","SO2","NO2","O3"]].boxplot()
plt.savefig("boxplot_pollutants.png")
```
<img width="1000" height="600" alt="boxplot_pollutants" src="https://github.com/user-attachments/assets/5e9eb715-e4af-4df0-bf8a-e9b8c614e928" />

> **Interpretation:** PM2.5 and PM10 show the widest interquartile range and most outliers. O3 follows an inverse seasonal pattern — higher in summer (photochemical reaction with sunlight).

---

## 🔗 Task 6 — Correlation Analysis

**Objective:** Identify which variables are most correlated with PM2.5.

```python
cols = ["PM2.5","PM10","SO2","NO2","CO","O3","TEMP","PRES","WSPM"]
corr_matrix = df[cols].corr()

# Most correlated with PM2.5
pm25_corr = corr_matrix["PM2.5"].drop("PM2.5").abs().sort_values(ascending=False)
print(pm25_corr)
```

### Results — Correlation with PM2.5

| Variable | Correlation | Direction | Meaning |
|----------|-------------|-----------|---------|
| **CO** | +0.74 | ⬆️ Positive | Same combustion source — rise together |
| **PM10** | +0.72 | ⬆️ Positive | Same pollution events |
| **NO2** | +0.62 | ⬆️ Positive | Traffic pollutant, similar source |
| **SO2** | +0.55 | ⬆️ Positive | Industrial / coal emissions |
| **TEMP** | −0.45 | ⬇️ Negative | Cold air traps pollutants |
| **WSPM** | −0.31 | ⬇️ Negative | Wind disperses pollution |

### Heatmap
<img width="900" height="700" alt="heatmap_correlation" src="https://github.com/user-attachments/assets/24e2fe52-c481-4027-b868-595819bc0156" />


### Scatter: Temperature vs PM2.5
<img width="800" height="500" alt="scatter_temp_pm25" src="https://github.com/user-attachments/assets/43ece42d-0855-4f24-b92e-16e2860bd7a0" />


### 🔍 Key Insights

> **1. CO is most correlated with PM2.5 (r = +0.74)**  
> Both are products of incomplete combustion — vehicles, heating, and industry drive them together.

> **2. Temperature negatively affects PM2.5 (r = −0.45)**  
> Cold winter conditions create temperature inversions that trap pollutants near ground level, causing Beijing's notorious "smog season."

> **3. Wind speed reduces PM2.5 (r = −0.31)**  
> Higher wind speed physically disperses particulates — windy days are measurably cleaner.

---

## 📁 File Structure

```
Activity-1-Beijing-Multi-Site-Air-Quality/
├── data/
│   ├── PRSA_Data_*.csv          # Raw data (12 files)
│   └── cleaned_data.csv         # Output from Task 2
├── task2.py                     # Data cleaning
├── task3.py                     # Statistics
├── task4.py                     # Filtering
├── task5.py                     # Visualization
├── task6.py                     # Correlation
├── histogram_pm25.png           # Chart output
├── lineplot_pm25.png            # Chart output
├── boxplot_pollutants.png       # Chart output
├── heatmap_correlation.png      # Chart output
├── scatter_temp_pm25.png        # Chart output
├── Beijing_AirQuality_Presentation.pptx
└── README.md
```

---

