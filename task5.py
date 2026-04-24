# Task 5: Data Visualization
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned_data.csv")

# ============================================
# Graph 1: Histogram of PM2.5
# ============================================
plt.figure(figsize=(8, 5)) 
df["PM2.5"].hist(bins=50, color="steelblue", edgecolor="white")
plt.title("Distribution of PM2.5")
plt.xlabel("PM2.5 (µg/m³)")  
plt.ylabel("Frequency")     
plt.tight_layout()       
plt.savefig("histogram_pm25.png")  
plt.show()  

# ============================================
# Graph 2: Line Plot of PM2.5 by time
# ============================================
monthly = (
    df.groupby(["year", "month"])["PM2.5"]
      .mean() 
      .reset_index() 
)
monthly["date"] = monthly["year"].astype(str) + "-" + monthly["month"].astype(str)

plt.figure(figsize=(12, 5))
plt.plot(monthly["date"], monthly["PM2.5"], color="tomato", linewidth=1.5)
plt.title("Monthly Average PM2.5 (2013-2017)")
plt.xlabel("Month")
plt.ylabel("PM2.5 (µg/m³)")
plt.xticks(rotation=45)  
plt.tight_layout()
plt.savefig("lineplot_pm25.png")
plt.show()

# ============================================
# Graph 3: Boxplot - comparing of each pollutants 
# ============================================
pollutants = ["PM2.5", "PM10", "SO2", "NO2", "O3"]
plt.figure(figsize=(10, 6))
df[pollutants].boxplot()
plt.title("Boxplot of Pollutants")
plt.ylabel("Concentration (µg/m³)")
plt.tight_layout()
plt.savefig("boxplot_pollutants.png")
plt.show()