# )The marks obtained by a student in 3 different subjects are input by the user. Your program should calc
# ulate the average of subjects and display the grade. The student gets a grade as per the following rules:
# Average Grade
# 90-100 A
# 80-89 B
# 70-79 C
# 60-69 D
# 0-59
def grade(mark1, mark2, mark3):
    avg = mark1 + mark2 + mark3/3
    print(f"avgerage is {avg}")
    if 100 > avg and avg < 90:
        print("------GRADE A")
    elif (avg > 89 and avg < 80):
        print("------>GRADE B")
    elif 79 >avg and avg < 70:
        print("------->GRADEC")
    elif avg >69 and avg <60:
        print("-------GRADE D")
    else:
        print("D")


# main
print("---------------------enter the data(marks) fro avg calculcation----------------------")
mark1 = int(input("enter the marks for sub1"))
mark2 = int(input("enter the marks for sub2"))
mark3 = int(input("enter the marks for sub3"))
grade(mark1,mark2,mark3)