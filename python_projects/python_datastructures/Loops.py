# players = ["Federer", "Nadal", "Djokovic"]
#
#
# for player in players:  print(f"{player} is a Tennis player")

# Use for loop to change the elements in list

cities = ['Karachi', 'Lahore', 'Islamabad', 'Peshawar']

#
# for city in cities:
#
#     if city == 'Islamabad':
#         # print("Yes Correct")
#



# Level -3  coding


# temp list
temperatures = [72, 65, 80, 55, 90, 48, 77]

# using for loop and  new list warm_temp

warm_temp = []

for temp in temperatures:
    if temp >= 60:
        warm_temp.append(temp)


# print(warm_temp)


# Now Level 4 — Stop the loop early 🟡
# This is where break comes in. Same concept as yesterday but now you build it from scratch alone.

temperatures = [72, 65, 80, 55, 90, 48, 77]

# using for loop

for temp in temperatures:
    if temp < 60:
       break

    # print(temp)


#
# 🔴 Final Challenge — Solve This Completely Alone
# student list

students = [45, 78, 82, 91, 38, 88, 73]


passed = []

# for loop

for student in students:
    if student >= 50:
       passed.append(student)

    elif student < 40:
        break

print(passed)

