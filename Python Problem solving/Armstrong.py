"""
Problem : Print a python program that will check whether the number is armstrong number or not 
    """

def armstrong(num):
    num = int(input("Enter a number "))
    num_to_str = str(num)
    digits = len(num_to_str)
    total_sum = 0 
    for digit in num_to_str:
        total_sum += int(digit) ** digits
    if total_sum == num:
        print(f"{num} is a armstrong number ")
    else:
        print(f"{num} is not a armstrong number")

print(armstrong(371))