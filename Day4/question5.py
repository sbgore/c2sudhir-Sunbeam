def maxLength(n):
    max1 = len(n[0])
    temp = n[0]
    for word in n:
        if len(word) > max1:
            max1 = len(word)
            temp = word

    print(f"length of word is:\n{max1} \n the longest word is: \n{temp}")


# function call
my_lists = ['one', 'two', 'sunebeam', 'gratplace']
maxLength(my_lists)
