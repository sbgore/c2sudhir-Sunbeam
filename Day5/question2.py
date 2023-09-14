# sum of values in directory
def sum_of_vlaues(dict2):
    sum = 0
    for i in dict2:
        sum = sum + dict2[i]
    print(sum)


dict1 = {
    'key1': 200,
    'key2': 300
}
sum_of_vlaues(dict1)
