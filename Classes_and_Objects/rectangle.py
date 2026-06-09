# Import the library

import matplotlib.pyplot as plt


class Rectangle:

    def __init__(self, Height , width , color):
        self.Height =Height
        self.width = width
        self.color = color


    #  Method

    def draw_rectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.Height,self.width , fc=self.color))
        plt.axis('scaled')
        plt.show()


    # Calling class Dog

New_rectangle= Rectangle(12, 5, "red")
New_rectangle2 = Rectangle(16, 6, "Yellow")


New_rectangle.draw_rectangle()
New_rectangle2.draw_rectangle()



print(f"The new rectangle height  is  {New_rectangle.Height} , its width is {New_rectangle.width}  and its color is {New_rectangle.color} ")

print(f"The new rectangle height  is  {New_rectangle2.Height} , its width is {New_rectangle2.width}  and its color is {New_rectangle2.color} ")