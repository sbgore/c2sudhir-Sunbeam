# 1)Using for loop, write and run a Python program to find factorial from 0 to 10.
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


# Input a number
num = int(input("Enter a number: "))

# Calculate and print the factorial
print(f"The factorial of {num} is {factorial(num)}")
