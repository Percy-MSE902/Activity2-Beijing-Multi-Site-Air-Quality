# Task 6: Correlation Analysis
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned_data.csv")

cols = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3", "TEMP", "PRES", "WSPM"]

# ============================================
# Step 1: Calculation of all Correlation 
# ============================================
corr_matrix = df[cols].corr()  
print("--- Correlation Matrix ---")
print(corr_matrix.round(2))

# ============================================
# Step 2: ตัวแปรไหนสัมพันธ์กับ PM2.5 มากที่สุด?
# ============================================
pm25_corr = (
    corr_matrix["PM2.5"]
    .drop("PM2.5")              
    .abs()                   
    .sort_values(ascending=False)
)
print("\n--- Variable is correlated with  PM2.5 (High to Low) ---")
print(pm25_corr)
print(f"\n High correlation: {pm25_corr.index[0]} ({pm25_corr.iloc[0]:.2f})")

# ============================================
# Step 3: Temperature relate to PM2.5 ? (Scatter Plot)
# ============================================
sample = df.sample(3000, random_state=42)  

plt.figure(figsize=(8, 5))
plt.scatter(sample["TEMP"], sample["PM2.5"],
            alpha=0.3,        
            color="steelblue",
            s=10)           
plt.title("Temperature vs PM2.5")
plt.xlabel("Temperature (°C)")
plt.ylabel("PM2.5 (µg/m³)")
plt.tight_layout()
plt.savefig("scatter_temp_pm25.png")
plt.show()

# ============================================
# Step 4: Heatmap shows all correlation 
# ============================================
plt.figure(figsize=(9, 7))
plt.imshow(corr_matrix, cmap="coolwarm", vmin=-1, vmax=1)
plt.colorbar()  
plt.xticks(range(len(cols)), cols, rotation=45)
plt.yticks(range(len(cols)), cols)
for i in range(len(cols)):
    for j in range(len(cols)):
        val = corr_matrix.iloc[i, j]
        plt.text(j, i, f"{val:.2f}", ha="center", va="center", fontsize=8)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("heatmap_correlation.png")
plt.show()