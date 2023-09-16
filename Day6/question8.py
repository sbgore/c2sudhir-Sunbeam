# 6)Write a program that rotates the element of a list so that the element at the
# first index moves to the second index, the element in the second index moves to
# the third index, etc., and the element in the last index moves to the first index.Input:-
# [‘Sunday’,’Monday’,’Tuesday’,’Wednesday’]
# Output:- [’Wednesday’, ‘Sunday’, ’Monday’, ’Tuesday’]
# word1 = ['sunday', 'Monday', 'tuesday', 'wednesday']
# print(len(word1))
# first_element = word1[0]
# for i in range(len(word1)):
#     word1[i] = word1[i + 1]
#
# word1[-1] = first_element
# print(word1)
def rotate_list(arr):
    if len(arr) <= 1:
        return arr  # Nothing to rotate if the list has 0 or 1 element

    first_element = arr[0]  # Store the first element
    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]  # Shift elements to the left

    arr[-1] = first_element  # Set the last element to the first

# Input list
input_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday']

# Rotate the list
rotate_list(input_list)

# Print the rotated list
print(input_list)
