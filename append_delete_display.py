# Python Program to Append, Delete and Display Elements of a List Using Classes

class check:
    def __init__(self):
        self.n = []

    def add(self,a):
        return self.n.append(a)

    def remove(self,b):
        self.n.remove(b)

    def display(self):
        return self.n

obj = check()

while True:
    print("0 Exit")
    print("1 Add")
    print("2 Delete")
    print("3 Display")
    choice = int(input("Enter your choice : "))
    if(choice == 0):
        print("Exiting")
        exit(0)
    elif(choice == 1):
        n = int(input("Enter item to append"))
        obj.add(n)
        print("List : ", obj.display())
    elif choice == 2:
        n = int(input("Enter item to remove"))
        obj.remove(n)
        print("List : ", obj.display())
    elif choice == 3:
        print("List : ", obj.display())
    else:
        print("invalid input")

print()