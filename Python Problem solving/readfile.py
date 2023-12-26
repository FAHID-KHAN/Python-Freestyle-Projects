"""
Problem : Read content from a file 
    """

filename = "files/read.txt"

with open(filename) as f:
    content = f.read()
    
print(content)