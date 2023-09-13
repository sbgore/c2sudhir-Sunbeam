def max(m, n, p):
    if num1 > num2 and num1 > num3:
        print(f"num is greater{num1}")
    elif num2 > num1 and num2 > num3:
        print(f'num2 is greater one{num2}')
    else:
        print(f'num3 is greater {num3}')


# main fucntion
num1 = int(input("enter first num"))
num2 = int(input("enter second one"))
num3 = int(input('enter third one'))
max(num1, num2, num3)
