class Dog:

     def __init__(self ,name, breed):
          self.name = name
          self.breed = breed

     def add_color(self,color):
          self.color = color
          return(self.color)





# Calling class Dog

New_dog = Dog("Bruno" ,"German shepherd")
Dog.add_color()

print(f"The new Dog is named {New_dog.name} and its breed is {New_dog.breed} ")