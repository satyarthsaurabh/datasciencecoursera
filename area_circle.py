# Python Program to Create a Class and Compute the Area and the Perimeter of the Circle


class Circle:
    pie = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.pie*self.radius**2

    def perimeter(self):
        return 2*self.pie*self.radius


for i in range(1,4):
    obj = Circle(i)
    print('Area of cicle',obj.area())
    print('perimeter of circle',obj.perimeter())


