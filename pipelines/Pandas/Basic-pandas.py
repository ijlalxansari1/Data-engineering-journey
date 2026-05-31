import pandas as pd
from annotated_types import UpperCase

df = pd.read_csv("../Employees.csv")

df["bonus"] = df["salary"] * 0.10
# df["age"] = df["salary"].astype(int)
df = df.rename(columns={"salary": "annual_salary"})

# Fixing NA values
df["annual_salary"] = df["annual_salary"].fillna(df["annual_salary"].mean())
df["annual_salary"] = df["annual_salary"].astype(int)

df["age"] = df["age"].fillna(df["age"].mean())
df["age"] = df["age"].astype(int)



df["bonus"] = df["bonus"].fillna(df["bonus"].mean())


# Chaning name to uppercase



df["name"] = df["name"].str.upper()


print(df)



# filtered = df[(df["annual_salary"] > 40000) & (df["age"] >26)]
#
# filtered.to_csv("employees_clean_pandas.csv", index=False)

# print(filtered)

#
# print(df.shape)    # how many rows and columns?
# print(df.dtypes)   # what data type is each column?
# print(df.head(2))  # show me the first 2 rows