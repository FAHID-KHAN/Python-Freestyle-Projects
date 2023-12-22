"""
Problem : Write a program to extract each digit from an integer in the reverse order.For Example if the 
given int is 7536 the output shall be "6 3 5 7" with a space seperating the digits.

"""

number = input("Please enter a number \n")

sliced_number = number[::-1]

new_number = " ".join(sliced_number)

print(new_number)