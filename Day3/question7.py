# 8)Write a program that prompts the user to input a character and determine the character is vowel or constant
letter = input("enter the character\n").lower()
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print("vowels")
else:
    print("constant")
