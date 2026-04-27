import pandas as pd

# Step 1: Extract
df = pd.read_csv("./UCL/key_stats.csv")

# Step 2: Transform (basic cleaning)
df = df.drop_duplicates()
df = df.dropna()

# clean + convert
df = df.rename(columns={"distance_covered": "distance_covered_km"})
df["distance_covered_km"] = df["distance_covered_km"].astype(float)

print(df.dtypes)
# Quick inspection
# print(df.columns)
print(df.head())
# print(df.info())