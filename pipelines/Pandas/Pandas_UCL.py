import pandas as pd


data = {
    "player"      : ["Vinicius Jr", "Erling Haaland", "Kylian Mbappe", "Robert Lewandowski", "Sadio Mane", "Riyad Mahrez", "Karim Benzema", "Kevin De Bruyne"],
    "club"        : ["Real Madrid", "Man City", "PSG", "Barcelona", "Liverpool", "Man City", "Real Madrid", "Man City"],
    "country"     : ["Spain", "England", "France", "Spain", "England", "England", "Spain", "England"],
    "goals"       : [23, 35, 28, 18, 20, 15, 25, 10],
    "appearances" : [34, 35, 32, 30, 33, 28, 32, 30]
}


df = pd.DataFrame(data)

# Total goals by country
goal_count = df.groupby("country")["goals"].sum()

# Total goals by cLUB

# Top scoring country
most_goals = goal_count.sort_values(ascending=False)

# 1. Total goals per country
totalgoals = df.groupby("country")["goals"].sum()

# 2. Average appearances per club
avg_appearance = df.groupby("club")["appearances"].mean()

# 3. How many players per country
players_country = df.groupby("country")["player"].count()
# Average appearances by club
avg_appearances = df.groupby("club")["appearances"].mean().round(2)

# print(goal_count ,"\n ", players_country ,"\n ", avg_appearance)
club_goals = df.groupby("club")["goals"].mean()

club_goals.sort_values(ascending=False, inplace=True)
print(club_goals)

# print(most_goals)
# print(avg_appearances)