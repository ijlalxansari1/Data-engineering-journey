# Create a dictionary called student with these four fields:
#
# name
# age
# city
# score

# Student Dict


student = {

"name": "Ijlal Ansari" ,
"age" : 25,
"city": "Gilgit",
"score": 92

}


# city  name
student["city"] ="Sofia"


# adding new course name Data engineering
student["course"] ="Data Engineering"

# print(student)





# updated student dict


# for key ,value in student.items():
#
#     print(f"{key}: {value}")

# task
students = [
    {"name": "Ijlal",  "score": 92, "city": "Skardu"},
    {"name": "Ali",    "score": 45, "city": "Lahore"},
    {"name": "Sara",   "score": 78, "city": "Karachi"},
    {"name": "Ahmed",  "score": 38, "city": "Peshawar"}
]

# printing score above 50;


Passing_students = [student["name"] for student in students if student["score"] >50]

print(f"The student who have above 50 marks is :  {Passing_students}")

# for student in students:
#     if student["score"] > 50:
#        print(f"The student who have above 50 marks is :  {student["name"]}")





