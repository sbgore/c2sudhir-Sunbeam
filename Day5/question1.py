# 1) Given a dictionary of students and their favourite colours:
# people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}

# C. Remove 'Jenny' and her favourite colour
# D. Sort and print students and their favourite colours alphabetically by name
# dictionary of key-value pairs


def exmaple():
    people = {
        "arham": "blue",
        "lisa": "yellow",
        "vinod": "purple",
        "jenny": "pink"
    }
    # A. step=1Find out how many students are in the list
    no_of_people = len(people)
    print(f"the no of people in the list are :{no_of_people}")

    # B. Change Lisa’s favourite colour
    new_colour = 'white'
    people['lisa'] = new_colour
    print(f"A.the new fav. colour of list :{new_colour}")

    # C. Remove 'Jenny' and her favourite colour
    if 'jenny' in people:
        del people['jenny']
        print("c.'jenny' and her fav colour removed")

    # D. Sort and print students and their favourite colours alphabetically by name
    sorted_list = dict(sorted(people.items()))
    print("D. Students and their favorite colors sorted alphabetically:")
    for students, color in sorted_list.items():
        print(f"{students}:{color}")


exmaple()
