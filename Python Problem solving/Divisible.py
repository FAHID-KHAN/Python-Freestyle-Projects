"""
Problem : Write a program that will tell whether the given number is divisible by 3 & 6
    """

num = int(input("Please enter a number "))

if num%3==0 and num%6==0 :
    print("the number is divisible by 3 and 6")
else:
    print("the number is not divisible by 3 and 6")