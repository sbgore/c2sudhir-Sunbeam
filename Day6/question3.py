str = input("enter the string")
# 3) Write a program that reads a string from keyboard and display:
# * The number of uppercase letters in the string
# * The number of lowercase letters in the string
# * The number of digits in the string
# * The number of whitespace characters in the string
uppercase_count = 0
lowercase_count = 0
digit_count = 0
space_count = 0

for i in str:
    if i.isupper():
        uppercase_count += 1
    elif i.islower():
        lowercase_count += 1
    elif i.isdigit():
        digit_count += 1
    elif i.isspace():
        space_count += 1
# Display the counts
print("Number of uppercase letters:", uppercase_count)
print("Number of lowercase letters:", lowercase_count)
print("Number of digits:", digit_count)
print("Number of whitespace characters:", space_count)
