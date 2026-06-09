# Import the library

import matplotlib.pyplot as plt
from markdown_it.rules_inline import newline


class Circle:

    def __init__(self, color, radius):
        self.color = color
        self.radius = radius

    # Method
    def add_radius(self, r):
        self.radius =self.radius + r
        return (self.radius)

    #  Method

    def draw_circle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()


    # Calling class Dog

New_circle = Circle("green", 4)

New_circle.draw_circle()


print(f"The new circle is  {New_circle.color} and its radius is {New_circle.radius} ")