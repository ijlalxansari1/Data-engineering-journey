import requests
import pandas as pd

# Pulling live data from a public API
url = "https://api.football-data.org/v4/matches"

response = requests.get(url)
# checking response
print(response.status_code)

# Convert JSON response to a DataFrame
df = pd.json_normalize(response.json())

print(df.shape)
print(df.head())