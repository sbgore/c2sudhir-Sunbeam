

def fun():
    list1 = [10, 20, 30, (40, 50), 60]
    count=0
    for value in list1:
        if type((10, 20))==type(value):
            count=list1.index(value)

    print(count)

fun()
