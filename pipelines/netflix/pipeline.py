

import pandas as pd
import sqlite3

# Extracting step
def extract():
    return pd.read_csv("../../data/netflix/netflix.csv  ")


# Transform step

def transform(df):
    df = df.drop_duplicates()
    df = df.dropna(subset=["title", "rating"])
    df = df[["title", "rating", "type"]]


    return df

# Load data step

def load(df):
    conn = sqlite3.connect("netflix.db")
    df.to_sql("movies", conn, if_exists="replace", index=False)
    return conn

# Query step
def query(conn):
    return pd.read_sql_query("""SELECT * FROM movies; """, conn)

# Calling main functiins

df = extract()
df = transform(df)
conn = load(df)
result = query(conn)

print(result.head())
print(df.info())
conn.close()