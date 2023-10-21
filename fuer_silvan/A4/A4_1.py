#!/usr/bin/env python3

# build a string
def build_string_pyramid(h):

    # One idea is to start with an empty string and append individual lines
    s = ""

    # You may want to use nested loops and the range() function
    for i in range(h):
        for j in range(i+1):
            s += str(j+1) + "*"
        s = s[:len(s) - 1]
        s += "\n"
    for i in range(h):
        for j in range(h-i-1):
            s += str(j+1) + "*"
        s = s[:len(s) - 1]
        s += "\n"
    return s

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# See the console output and compare it to the image in the task description
print(build_string_pyramid(5))



