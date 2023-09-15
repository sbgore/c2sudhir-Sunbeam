# A. Display characters from even position
# B. Display characters from odd position
def odd_even_charcter():
    given_str = "sunbeam"
    even_charcter = []
    odd_character = []
    for i in range(len(given_str)):
        if i % 2 == 0:
            even_charcter.append(given_str[i])
        else:
            odd_character.append(given_str[i])
    print(f"character at even position{even_charcter},character at odd{odd_character}")

    # C. Display length of a string


def length():
    given_str = "engineering stram full of joy"
    print(len(given_str))


# D. Add a at the end of string length times
def modify():
    given_str = "python"
    length = len(given_str)
    output_str = given_str + '*' * length
    print(output_str)


def menu():
    print("______________--------------WELCOME TO MENU DRIVEN PROGRAMME----------------_______________________-")
    print("1. Display characters from even position and  Display characters from odd position")
    print("2. Display length of a string")
    print("3. Add a at the end of string length times")
    print("5. exit")
    print('-' * 80)
    choice = int(input("enter your choice"))
    return choice


# if else satatments

while True:
    # call menu
    ch = menu()
    if ch == 1:
        odd_even_charcter()
    elif ch == 2:
        length()
    elif ch==3:
        modify()
    else:
        print("bye bye")
        break


# 2)Display following menu and write required function for it

# A. Display characters from even position
# B. Display characters from odd position
# C. Display length of a string
# D. Add a at the end of string length times
