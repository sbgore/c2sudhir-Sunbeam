#ind and display the largest number of a list without using built-in function
#max(). Your program should ask the user to input values in list from keyboard
from typing import List

mylists=[]
size=int(input("enter the size of lists"))

for i in range(size):
     data=int(input())
     mylists.append(data)
max=0
for data in mylists:
    if data > max:
        max=data
print("the largest element in the ists is", max)
