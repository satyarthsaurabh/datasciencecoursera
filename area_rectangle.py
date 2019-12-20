class Area:
    def __init__(self, len, bre):
        self.length = len
        self.breath = bre

    def area(self):
        return self.length * self.breath


a1 = Area(2, 4)
a2 = Area(3, 6)
a3 = Area(5, 8)

print(a1.area())
print(a2.area())
print(a3.area())
