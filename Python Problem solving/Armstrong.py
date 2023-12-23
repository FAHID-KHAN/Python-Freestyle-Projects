"""
Problem : Print a python program that will check whether the number is armstrong number or not 
    """

def armstrong():
    num = int(input("Enter a number "))
    num_to_str = str(num)
    print(num_to_str)
    digits = len(num_to_str)
    print(digits)
    total_sum = 0 
    for digit in num_to_str:
        total_sum += int(digit) ** digits
        print(total_sum)
    if total_sum == num:
        print(f"{num} is a armstrong number ")
    else:
        print(f"{num} is not a armstrong number")

print(armstrong())