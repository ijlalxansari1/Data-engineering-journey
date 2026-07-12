import json
import pandas as pd

# A JSON string (pretend this came from an API)
Ucl_data = ('{"match": "UCL Final", '
            '"players": '
            '[{"name": "Messi", "goals": 8, "assists": 4}, '
            '{"name": "Ronaldo", "goals": 6, "assists": 2}, '
            '{"name": "Benzema", "goals": 7, "assists": 3}]}')

# Parse it into a Python dict
player = json.loads(Ucl_data)
print(
    player["players"][2]["name"]
)

df = pd.DataFrame(player["players"])
print(df)