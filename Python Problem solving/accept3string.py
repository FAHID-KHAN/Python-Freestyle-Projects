"""
Problem :  Accept any three string from one input() call
    """
string = input("Enter the three names with keeping space in between: ")
sep = string.split()
print(sep)

print(sep[0],sep[1],sep[2])