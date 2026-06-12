import pandas as pd

# Left table — player stats
players = pd.DataFrame({
    "player": ["Haaland", "Vinicius", "Kane", "Mbappé" , "Bellingham" , "Çalhanoğlu"],
    "club": ["Man City", "Real Madrid", "Bayern", "PSG" , "Real Madrid", "Inter Milan"],
    "goals": [8, 5, 6, 4 , 4,3]
})

# Right table — club info
clubs = pd.DataFrame({
    "club": ["Man City", "Real Madrid", "Bayern" , "Inter Milan" ],
    "country": ["England", "Spain", "Germany", "Italy"],
    "stadium": ["Etihad", "Bernabeu", "Allianz Arena" , "San Siro"]
})


result = pd.merge(players ,clubs, on="club" , how="right"  )

print(result)