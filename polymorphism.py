import math

class Shape():
    def find_area(self):
        pass
    def find_perimeter(self):
        pass

class circle(Shape):
    def __init__(self, radius:int):
        self.radius = radius
        self.diameter = 2*radius
    def find_area(self):
        circle_area = math.pi * math.pow(self.radius,2)
        return circle_area
    def find_perimeter(self):
        circle_perimeter = 2 * math.pi * self.radius
        return circle_perimeter

class rectangle(Shape):
    def __init__(self, length:int, width:int):
        self.lenght = length
        self.width = width
    def find_area(self):
        rect_area = self.lenght * self.width
        return rect_area
    def find_perimeter(self):
        rect_perimeter = 2 * (self.width + self.lenght)
        return rect_perimeter

circle = circle(12)
rectangle = rectangle(12,5)

print(circle.find_area())
print(circle.find_perimeter())
print(rectangle.find_area())
print(rectangle.find_perimeter())