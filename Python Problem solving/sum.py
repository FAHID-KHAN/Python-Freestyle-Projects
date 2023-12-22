"""
    Problem : Generate a python program to add 3 numbers 
"""

def get_sum():
    x = input("Please enter a number ")
    sum = 0 
    for num in x:
        sum+=int(num)
    return sum 

print(get_sum())


    