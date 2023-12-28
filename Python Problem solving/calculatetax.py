"""
Problem : Calculate income tax for given income by adhering to the below rules 
first 10k--> 0%
second 10k--> 10%
remaining-->20%
    """

income = int(input("Please enter a number"))
print("Your income is {} $".format(income))

a = 10000
b = 10000
first_20 = a+b
c = income-(a+b)

if income < a:
    print("Your tax is 0 percent")
elif income > a and income < first_20:
    tax = b*(10/100)
    print("Your tax is {} $".format(tax))
else :
    tax = b*(10/100) + c*(20/100)
    print("Your tax is {} $".format(tax))
