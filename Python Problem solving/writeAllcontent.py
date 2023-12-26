"""
Problem : Write all content of a given file into a new file by skipping line number 5
    """
filename = "files/test.txt"

with open(filename) as f: 
    lines = f.readlines()

with open("files/new.txt",'w') as f:
    count = 0
    for line in lines:
        if count == 4:
            count += 1
            continue 
        else:
            f.write(line)
        count += 1