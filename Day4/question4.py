# 4). Write a method in python to display the elements of list thrice if it is a
# number and display
# the element terminated with ‘#’ if it is not a number.
# Hint-: Use InBuilt Function isdigit()
# Refer below as a input:-

def display_element_thrice():
    # crating a list
    my_lists = ['41', 'drond', 'sunbeam', '13', 'Zara']
    for element in my_lists:
        if element.isdigit():
            print(element * 3)
        else:
            print(element + '#')


display_element_thrice()
