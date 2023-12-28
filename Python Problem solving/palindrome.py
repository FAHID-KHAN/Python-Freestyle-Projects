"""
Problem : Write a program to check if the given number is a palindrome number.
A palindrome number is a number that is same after reverse. For example 545, is the palindrome
numbers
    """

number = input("Please enter a number ")

rev = number[::-1]

if number == rev: 
    print("The given number is palindrome ")
else:
    print("The given number is not palindrome")