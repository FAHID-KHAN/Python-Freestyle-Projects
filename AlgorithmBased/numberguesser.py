import random 
import math 

lower_bound = int(input("Please input the lower bound : \n"))
upper_bound = int(input("Please input the upper bound : \n"))

x = random.randint(lower_bound,upper_bound)

print("\n\t You have only ",round(math.log(upper_bound-lower_bound + 1,2))," chances to guess the integer !'\n")
print(math.log(9,2))

count= 0 

while count < math.log(upper_bound- lower_bound + 1,2):
    count +=1 
    guess = int(input("Guess a number:- "))
    if x == guess:
        print("Congratulations you did it ",count ,"try")
        break
    elif x > guess:
        print("You guessed too small !")
    elif x < guess:
        print("You guessed too high")

if count >= math.log(upper_bound- lower_bound + 1,2):
    print("\n the number is %d" %x)
    print("\t Better luck next time! ")