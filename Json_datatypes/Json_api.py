import requests

import requests

import pandas as pd
response = requests.get("https://jsonplaceholder.typicode.com/users")


# print(type(response))
# print(response.status_code)

data = response.json()
print(data[0]["address"]["city"])

df = pd.json_normalize(data)
# print(type(data))
# print(df.head())
print(df.columns)

# print(data[0])