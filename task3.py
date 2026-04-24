# Task 3: Basic Statistical Analysis
import pandas as pd

# Download Clean File
df = pd.read_csv("data/cleaned_data.csv")

# Specific columns for ananysis
pollutants = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]

# ============================================
# describe() 
# ============================================
print("--- Summary Data ---")
print(df[pollutants].describe().round(2))

# ============================================
# Seperate Calculation
# ============================================
for col in pollutants:
    print(f"\n{col}:")
    print(f" Mean: {df[col].mean():.2f}")
    print(f" Median: {df[col].median():.2f}")
    print(f" Min: {df[col].min():.2f}")
    print(f" Max: {df[col].max():.2f}")
    print(f" Std: {df[col].std():.2f}")