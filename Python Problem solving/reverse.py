"""
Problem : Wirte a program that will reverse a four digit number and also it checks whether the reverse 
    """


def reverse():
    num = int(input("Enter a number "))
    new_num = str(num)
    reversed_num = list(reversed(new_num))
    print(reversed_num)


print(reverse())