"""
Write a program that will take three digits from the user and add the square of each digit 
    """

number = int(input("Enter a 3 digit number \n"))
number_to_str = str(number)
sliced = list(number_to_str[::-1])
total_sum = 0 
for digit in sliced:
    total_sum += int(digit) ** 2
print(total_sum)


