players = {}

players["name"] = input("Enter player name: ")
players["sport"] = input("Enter sport  played: ")
players["achievements"] = int(input("Enter achievements: "))




# conditions
if players["sport"] == "Tennis" and players["achievements"] == 20:

    print("Meets the criteria!")
else:
    print("Does not meet the criteria.")



print(players)