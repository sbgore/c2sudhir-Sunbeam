mylist=[]
size=int(input(f"enter the how size of list "))
for i in range (size):
    data=int(input())
    mylist.append(data)
#logic priting the alerternet numbers
for i in range (0,size,2):
    print(mylist[i])
