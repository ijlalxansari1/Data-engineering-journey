import pandas as pd

data = {
    "club": ["Real Madrid", "Bayern Munich", "Man City", "Real Madrid", "Real Madrid", "Bayern Munich", "Man City", "PSG", "Inter Milan", "Inter Milan"],
    "country": ["Spain", "Germany", "England", "Spain", "Spain", "Germany", "England", "France", "Italy", "Italy"],
    "player": ["Vinicius", "Kane", "Haaland", "Mbappe", "Bellingham", "Muller", "De Bruyne", "Hakimi", "Lautaro", "Calhanoglu"],
    "goals": [8, 6, 7, 9, 5, 3, 4, 6, 5, 4],
    "appearances": [10, 11, 10, 9, 10, 10, 9, 8, 10, 9]
}

df = pd.DataFrame(data)

# Total goals by country
goal_count = df.groupby("country")["goals"].sum()

# Top scoring country
most_goals = goal_count.sort_values(ascending=False)

# Average appearances by club
avg_appearances = df.groupby("club")["appearances"].mean().round(2)

print(most_goals)
print(avg_appearances)