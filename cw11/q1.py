import sys
import os
# from pathlib import Path

def read_file(file_name):
    with open(file_name, "r") as file:
        file.read()


if len(sys.argv) == 1:
    print("Hello World!")
elif os.path.exists(sys.argv[1]):
    string = read_file(sys.argv[1])
    lst1 = string.split(" ").split(".")
    # dict1 = {}


elif len(sys.argv) == 2:
    print(sys.argv[1][::-1])
