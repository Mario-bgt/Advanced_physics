#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def invert(d):
    inv_map = {}
    for k, v in d.items():
        inv_map[v] = inv_map.get(v, []) + [k]
    # sort the values
    for k, v in inv_map.items():
        inv_map[k] = sorted(v)
    return inv_map


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(invert({"c":1, "b":1, "a":3}))
