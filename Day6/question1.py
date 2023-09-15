# 1)Write a menu Driven Program To Calculate the Parameter and Area of
# different Shapes(Circle,Square,Rectangle) using functions
def circle():
    r =float(input("enter radius of circle"))
    PI = 3.14
    area = PI * r * r
    print(f"area if circle{area}")


def square():
    # formula
    side_length = input("enter the length")
    side_breadth = input("enter the breadth")
    Area = side_length * side_breadth
    print(f"Area of sqaure{Area}")


def reactangle():
    length = input("enter the length")
    width = input("enter the width")
    Area = length * width
    print(Area)


def menu():
    print("______________--------------WELCOME TO MENU DRIVEN PROGRAMME----------------_______________________-")
    print("welcome to application")
    print("1. enter 1 for calculation area of circle")
    print("2. enter 2 for calculation area of square ")
    print("3. enter 3 for calculation area of Rectangle ")
    print("5. exit")
    print('-' * 80)

    chcoice = int(input("enter the your choice"))
    return chcoice


# infinte loop
while True:
    # call menu and get the input from the user
    ch = menu()
    if ch == 1:
        circle()
    elif ch == 2:
        square()
    elif ch == 3:
        reactangle()
    else:
        print("bye", "bye")
        break
