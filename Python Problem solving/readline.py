"""
Problem : read line by line from a file 
    """

filename = "files/read.txt"

with open(filename) as f:
    lines = f.readlines()
    for line in lines:
        print(line.rstrip())