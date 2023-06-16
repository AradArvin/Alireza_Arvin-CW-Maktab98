import argparse
import os
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("-l", "--long", action="store_true", required=False)
parser.add_argument("path")

arg = parser.parse_args()

target_dir = os.listdir(arg.path)

if arg.long:
    for entry in os.listdir(arg.path):
        if os.path.isfile(entry):
            target_size = os.path.getsize(entry)
            print(f"{entry}, Size: {target_size} KB")
        else:
            print(entry)
else:   
    for entry in target_dir:
        print(entry)