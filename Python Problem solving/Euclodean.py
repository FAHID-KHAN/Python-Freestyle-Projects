"""Write a program to find the euclodean distance between 2 coordinates 
    """
import math

x1 = float(input("x1\n"))
x2 = float(input("x2\n"))
y1 = float(input("y1\n"))
y2 = float(input("y2\n"))


x = [x1,x2]
y = [y1,y2]

euclodean  = round(math.dist(x,y),2)
new_value = str(euclodean)
print("="*100)
print("Euclodean value of given number is \n" + new_value)