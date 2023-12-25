"""
Problem : Write a program to find the volume of the cylinder. Also find the cost when ,when the
cost of 1litre milk is 40Rs.
    """

import math


pi = math.pi
radius = float(input("Enter the radius in cm: \n"))
height = float(input("Enter the height in cm: \n"))

print(f"The radius of the cylinder is {radius} cm and height is {height} cm\n")

area_of_cylinder = pi *(radius**2) * height

litr = area_of_cylinder/1000
cost = litr*40


print("Area of cylinder is {}".format(area_of_cylinder))
print("Volume of cylinder will be ",area_of_cylinder)
print("The cost of the milk will be {} $".format(cost))