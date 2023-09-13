def calcluations(n):
    sum = 0
    # for i in range(1, n + 1):
    #     sum += (i * i * i)
    #
    # print(f"sum of cube is {sum}")
    # another logic
    sum = 0
    for index in range(1, n + 1):
        sum += pow(index, 3)

    print(f"sum of cube of all numbers {sum}")


# main funciton

numbers = int(input("enter the number"))
calcluations(numbers)
