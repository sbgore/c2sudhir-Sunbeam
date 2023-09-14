def countFrequnecy(lists):
    dict1 = {}
    count = 0
    for i in lists:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1


    for key, value in dict1.items():
     print(f"{key}->{value}")


List1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 6, 2, 4, 2, 5, 23, 6, 4]
countFrequnecy(List1)
