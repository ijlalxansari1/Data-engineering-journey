import pandas as pd
import sqlite3

df = pd.read_csv("netflix.csv")

df = df.drop_duplicates()
df = df.dropna()

conn = sqlite3.connect("my_database.db")

df.to_sql("Tests_table", conn, if_exists="replace", index=False)

result = pd.read_sql("SELECT * FROM Test_table LIMIT 10", conn)

# print(result)

print(df.head())
conn.close()