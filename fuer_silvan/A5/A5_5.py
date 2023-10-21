# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters.

def compress(data):
    keys = []
    vaL_DIC = []
    for i in data:
        vaL_DIC.append(tuple(i.values()))
        for j in i:
            if j not in keys:
                keys.append(j)
    keys.sort()
    return tuple(keys), vaL_DIC


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
data = [
    {"a": 1, "b": 2, "c": 3},
    {"a": 4, "d": 6, "b": 5}
]
data2 = []
data3 = [{1: 2}, {1: 3}]
data4 = [{}]

print(compress(data))
print(compress(data2))
print(compress(data3))
print(compress(data4))



