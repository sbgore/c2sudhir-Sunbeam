# 5)Define a function overlapping() that takes two lists and returns True if they
# have at least one member in common, False otherwise.
def overlapping(lists1, lists2):
    for item1 in lists1:
        for item2 in lists2:
            if item1 == item2:
                return True
    return False


lists1 = [1, 2, 3, 4, 5, 6]
lists2 = [1, 56, 6, 8, 9]
if overlapping(lists1, lists2):
    print("the lists have at least one common element")
else:
    print("do not have any common one")
