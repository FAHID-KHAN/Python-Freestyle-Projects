"""
Problem : Write a program to find the simple interest when the value of principle,rate of interest
and time period is given
    """
import time
principal = float(input("Enter the principal value\n"))
roi = float(input ("Enter the return of interest \n")) / 100
tp = int(input("Enter the time period\n"))
print(f"Your given principle is {principal} with return of interest is {roi} and in the time period of {tp} ")
for i in range(10):
    print("Calculating .....")
    time.sleep(1)
    
simple_interest = principal * roi * tp

print("The simple interest on your principal is {} ".format(simple_interest))