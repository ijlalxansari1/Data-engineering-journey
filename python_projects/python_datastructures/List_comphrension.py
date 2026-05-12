names = ['ali', 'sara', 'ahmed', 'zara']
# python list comprehension
name_uppered =[name.upper() for name in names]
print(name_uppered)


# Write a list comprehension that copies only scores above 50 into a new list called passing.


scores = [45, 82, 91, 38, 77, 60]

passing = [score for score in scores if score >= 50 ]


print (passing)





scores = [45, 82, 91, 38, 77, 60]

passing = [score*2  for score in scores if score >= 50 ]


print (passing)