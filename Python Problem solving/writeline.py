"""
Problem : Writing multiple lines to the file 
    """

filename = "files/example.txt"

with open(filename,'w') as f:
    content = f.write("this line will be added to the file")
    print(content)