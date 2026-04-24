# Task 2: Data Cleaning
import pandas as pd
import glob

all_files = glob.glob("data/*.csv")
df = pd.concat([pd.read_csv(f) for f in all_files], ignore_index=True)

# ============================================
# Step 1: Missing Values
# ============================================
print("--- Missing Values ---")
missing = df.isnull().sum()  
print(missing[missing > 0])      
# ============================================
# Step 2: Adding values by column's average 
# ============================================
pollutants = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]
for col in pollutants:
    avg = df[col].mean()                 
    df[col] = df[col].fillna(avg)        
print("Completely filling average data")

# ============================================
# Step 3: Delete empty row
# ============================================
before = len(df)                       
df = df.dropna()                        
after = len(df)                     
print(f"Delete: {before - after} rows")
print(f"Total left row: {after} rows")

# Validate the empty row
print("\n Total empty data:", df.isnull().sum().sum())

# Save to New file for using in next step
df.to_csv("data/cleaned_data.csv", index=False)
print("Completely save in cleaned_data.csv !")