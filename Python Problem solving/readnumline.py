"""
Problem : Read line number 4 from the following file
    """

filename = "files/test.txt"

with open (filename,"r") as f:
    readline = f.readlines()
    print(readline[3]) 