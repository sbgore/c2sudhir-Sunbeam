# 6). Define a procedure histogram() that takes a list of integers and prints a
# histogram to the screen.
# For example, histogram([4, 9, 7]) should print the following:
# ****
# *********
# ****
def histogram(l1):
    for i in l1:
        print('*' * i)


l2 = [4, 5, 7]
histogram(l2)
