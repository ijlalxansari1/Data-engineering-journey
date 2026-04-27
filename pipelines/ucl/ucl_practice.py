import pandas as pd


# ucl dataset
df= pd.read_csv("./UCL/key_stats.csv")

data_filtered = df[(df["goals"] >= 15 ) | (df["assists"] > 5 )]
#
# print(df["goals"].max())
# print(df["assists"].max())

print(data_filtered.head())