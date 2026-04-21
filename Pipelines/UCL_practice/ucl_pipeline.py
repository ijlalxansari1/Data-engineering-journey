import pandas as pd

df = pd.read_csv("./UCL/attacking.csv")

# show data
print(df.head())

# filter something
# print(df['match_played'] > 8)
# print(df[df['match_played'] > 8])
# print(df[df['club'] == "Real Madrid"   ]  )



#
# 👉 Find:
#
# Players who are NOT from Real Madrid
# AND have dribbles > 20

# print(df.info())

Filtered_data = df[(df['club'] != "Real Madrid") & (df['dribbles'] > 20 )]

# print(Filtered_data[['player_name', 'club', 'dribbles']])


# #
# print(df[(df['dribbles'] > 40)])
# #
# print(df[(df['dribbles'] > 40)][['player_name', 'dribbles']])
# #

#
# 👉 Find:
#
# Players from Liverpool OR Bayern
# AND dribbles > 30
# Show only:
# player_name
# club
# dribbles


multi_filtered = (df[((df['club'] == "Liverpool") | (df['club'] == "Bayern")) & (df['dribbles'] > 30 )]
[['player_name','club' ,'dribbles' ]] )

# sorting

sorted_filtered =multi_filtered.sort_values(by=['dribbles'] , ascending=[False]).head(2)
# print(sorted_filtered)


#
# 👉 Find:
#
# Top 3 players
# From any club except Liverpool
# With match_played > 8
# Sort by match_played descending
# Show:
# player_name
# club
# match_played



PLAYERS_filtered = (df[(df['club'] != 'Liverpool') & (df['match_played']> 8 )][['player_name' , 'club' , 'match_played']] )
sorted_players = PLAYERS_filtered.sort_values(by=['match_played'], ascending=[False]).head(3)

print(sorted_players)