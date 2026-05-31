# Write a function called get_top_students that:
#
# Takes the list as input
# Returns only students with score above 70
# Prints their name and city together
from debugpy.launcher import output

students = [
    {"name": "Ijlal",  "score": 92, "city": "Skardu"},
    {"name": "Ali",    "score": 45, "city": "Lahore"},
    {"name": "Sara",   "score": 78, "city": "Karachi"},
    {"name": "Ahmed",  "score": 38, "city": "Peshawar"}
]


def get_top_students(students):
    passed = [student["name"] + " - " + student["city"] for student in students if student["score"] > 70]
    return passed  # return the list

print(get_top_students(students))  # print outside the function


get_top_students(students)