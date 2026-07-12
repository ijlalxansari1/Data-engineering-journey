import pandas as pd

data_employees = {
    "name": ["ijlal", "john", "luci", "abrama", "sarah", "michael", "emily", "david"],
    "Gender": ["male", "male", "female", "female", "female", "male", "female", "male"],
    "age": [23, 26, 25, 28, 31, 29, 24, 35],
    "Field": ["Data", "IT-Operations", "Web Applications", "Cloud Operations", "Data", "Design", "QA Testing", "IT-Operations"]
}

data_salaries = {
    "name": ["ijlal", "john", "luci", "abrama", "sarah", "michael", "emily", "david"],
    "Salary_USD": [75000, 82000, 78000, 91000, 88000, 70000, 65000, 85000],
    "Experience_Years": [2, 4, 3, 6, 5, 3, 2, 7]
}


df = pd.DataFrame(data_employees)
df["Gender"] = df["Gender"].str.strip()

# data_filtered = df[(df["Gender"] =="male") | df["age"] >= 25 )]
data_filtered = df[(df["Gender"] == "male") | (df["age"] >= 25)]

# print(data_filtered)

df2 =pd.DataFrame(data_salaries)



print(df2)



