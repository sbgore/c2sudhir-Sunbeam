# Write a Python function to find the maximum of three numbers.

a = int(input("enter the num :"))
b = int(input("enter the num :"))
c = int(input("enter the num :"))
if a > b and a > c:
    print(f"greater num is { a }")
elif b > a and b > c:
    print(f"The greater num is { b }")
else:
    print(f"the greater num is { c }")
