"""
Problem : Check file is empty or not,Write a program to check if the given file is empty or not
    """

import os 
size = os.stat("files/example.txt").st_size

if size == 0:
    print("File is empty ")
else:
    print("File contains information")