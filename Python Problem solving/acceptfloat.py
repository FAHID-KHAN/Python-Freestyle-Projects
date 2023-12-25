"""Problem : Accept a list of 5 float numbers as an input from the user
    """

empty = []

while len(empty)<5:
    n = float(input("Enter float number "))
    empty.append(n)

print(empty)