#
# Copy scores above 50 into a new list called passing
# Multiply every score in the original list by 2 and store back
# Print both lists

scores = [45, 82, 91, 38, 77, 60]


passing =[]

for i in  range(len(scores)):
    if scores[i] >= 50:
        passing.append(scores[i])


    scores[i] *=2



print(f"The old score list is {scores}")


print(f"The new score list is {passing}")

