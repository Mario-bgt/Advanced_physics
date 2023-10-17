#!/usr/bin/env python3


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def min_domino_rotations(top_row, bottom_row):
    # Initialize the number of rotations to 0
    rotations = 0

    # Check if it's possible to make both rows equal
    for i in range(len(top_row)):
        if top_row[i] != bottom_row[i]:
            if top_row[i] == top_row[0]:
                top_row[i], bottom_row[i] = bottom_row[i], top_row[i]
            else:
                return -1
        rotations += 1

    return rotations


# The following line calls the function which will print # value to the Console.
# This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!

print(min_domino_rotations([2, 6, 2, 1, 2, 2], [5, 2, 4, 2, 3, 2]))
print(min_domino_rotations([3, 5, 1, 2, 6], [3, 6, 3, 3, 6]))