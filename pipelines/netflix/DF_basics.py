import pandas as pd


df_raw = pd.read_csv("../../data/netflix/netflix.csv")

# cleaning data

def data_health_report(df):
    print("=" * 40)
    print("📊 DATA HEALTH REPORT")
    print("=" * 40)

    # 1. Completeness
    print("\n1️⃣ COMPLETENESS (missing values):")
    print(df.isnull().sum())

    # 2. Uniqueness
    print("\n2️⃣ UNIQUENESS (duplicate rows):")
    print(f"Duplicate rows: {df.duplicated().sum()}")

    # 3. Validity (are dates actually dates?)
    print("\n3️⃣ VALIDITY (data types):")
    print(df.dtypes)

    # 4. Basic shape
    print("\n4️⃣ SHAPE:")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    print("=" * 40)


def clean(df):
    # Completeness fixes
    df["director"] = df["director"].fillna("Unknown")
    df["cast"] = df["cast"].fillna("Unknown")
    df["country"] = df["country"].fillna("Unknown")
    df = df.dropna(subset=["rating"])

    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
    # Validity fix — convert date string to real date

    return df


data_health_report(df_raw)        # before
df_cleaned = clean(df_raw.copy())
data_health_report(df_cleaned)    # after ✅

df_cleaned.to_csv("../../data/netflix/netflix_cleaned.csv", index=False)
# print("✅ Cleaned data saved!")
df_updated = pd.read_csv("../../data/netflix/netflix_cleaned.csv")
df_updated["date_added"] = pd.to_datetime(df_updated["date_added"], errors="coerce")






