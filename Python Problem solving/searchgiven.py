"""
Problem : : Write a python program to search a given number from a list
    """

l1 = [4,5,6,7,8,9,10]
n = int(input("Please enter a number "))

for i in l1:
    if i == n:
        print("Number exists ")
        break
    else:
        print("Number is not avaialable ")
