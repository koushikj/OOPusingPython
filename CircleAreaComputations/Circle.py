import math


class Circle:
    def __init__(self, radius=0):
        self.radius = radius
        # self.area = math.pi * radius ** 2

    def find_area(self):
        self.area = math.pi * self.radius ** 2

    def show(self):
        print(self.area)
