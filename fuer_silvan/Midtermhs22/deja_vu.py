def length(iterable):
    res = sum(1 for n in iterable)
    return res

print(length([1,2,[3,4]]))
print(length("oh dear"))
