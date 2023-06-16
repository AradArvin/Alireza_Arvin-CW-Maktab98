import sys
import os
from pathlib import Path

def read_file(file_name):
    with open(file_name, "r") as file:
        return file.read()


if len(sys.argv) == 1:
    print("Hello World!")
elif os.path.exists(sys.argv[1]):
    string = read_file(sys.argv[1])
    lst1 = string.split(" ")
    dict1 = dict()
    for word in lst1:
        dict1[word] = dict1.get(word,0) + 1
    print(dict1)
else:
    print(sys.argv[1][::-1])
