def merge(a, b):
    res = []
    if len(a) == 0 or len(b) == 0:
        return res
    elif len(a) > len(b):
        for i in range(len(a) - len(b)):
            b.append(b[-1])
    elif len(b) > len(a):
        for i in range(len(b) - len(a)):
            a.append(a[-1])
    print(a)
    print(b)
    for i, j in zip(a,b):
        res.append((i,j))
    return res




# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(merge([0, 1, 2], [5, 6]))
print(merge([0, 1, 2], [5, 6, 7])) # should return [(0, 5), (1, 6), (2, 7)]
print(merge([2, 1, 0], [5, 6]))    # should return [(2, 5), (1, 6), (0, 6)]
print(merge([], [2, 3]))           # should return []