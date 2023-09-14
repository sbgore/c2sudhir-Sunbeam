# )Write a program to read 6 numbers and create a dictionary having keys EVEN and ODD.
# Dictionary's value should be stored in list. Your dictionary should be like:
# {'EVEN':[8,10,64], 'ODD':[1,5,9]}

even = []
odd = []
for i in range(6):
    n = int(input("enter the number"))
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
# created the empty direcotry

d = {}
d['even'] = even
d['odd'] = odd
print(f"even:{even},odd:{odd}")
