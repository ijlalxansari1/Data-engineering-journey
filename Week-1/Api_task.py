import requests
import pandas as pd


response = requests.get("https://api.github.com")

data = response.json()

if response.status_code == 200 and data:
    print("Success: got data")

    Json_pandas = pd.json_normalize(data)
    print(Json_pandas.head())
else:
    print("Failed: bad response  ", response.status_code)



# print(bool({}))      # ?
# print(bool({"a": 1})) # ?
# print(bool([]))      # ?