""""
Problem : Swap the number without using 3rd variable 

"""

x = input("Enter the first number\n")
y = input("Enter the second number\n")

print("First value of x is "+ x)
print("Second value of y is "+ y)


x,y = y,x

print("The swapped variable of the given number of x and y is \n" + x,y)