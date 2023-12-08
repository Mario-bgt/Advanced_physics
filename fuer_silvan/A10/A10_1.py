#!/usr/bin/env python3

import os


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def process_data(path_reading, path_writing):
    if not os.path.exists(path_reading):
        # what to do if the input file does not exist?
        return False
    data = open(path_reading).read().splitlines()
    if not data:
        # an empty output file should be written
        open(path_writing, "w").close()
        return None
    if data[0] == 'name' and len(data) == 1:
        res = ["Firstname,Lastname\n"]
        open(path_writing, "w").writelines(res)
        return None

    res = ["Firstname,Lastname\n"]
    for line in data[1:]:
        if "; " in line:
            find = line.find("; ")
            surname, name = line[find + 2:], line[:find]
            res.append(surname + "," + name + "\n")
        else:
            find = line.find(" ")
            surname, name = line[:find], line[find + 1:]
            res.append(surname + "," + name + "\n")

    res[-1] = res[-1][:-1]
    open(path_writing, "w").writelines(res)
    return None


# The following line calls your solution function with the provided input file
# and then attempts to read and print the contents of the resulting output file.
# You do not need to modify these lines.
INPUT_PATH = "task/my_data.txt"
OUTPUT_PATH = "task/my_data_processed.txt"
process_data(INPUT_PATH, OUTPUT_PATH)
if os.path.exists(OUTPUT_PATH):
    with open(OUTPUT_PATH) as resultfile:
        print(resultfile.read())
else:
    print("No output file exists")
