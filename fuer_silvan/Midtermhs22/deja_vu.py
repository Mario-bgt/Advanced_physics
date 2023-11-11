def length(iterable):
    res = sum(1 for n in iterable)
    return res

print(length([1,2,[3,4]]))
print( length(("a", 1, 2, None)) )
print(length("oh dear"))

def length(iterable):
    counter = 0
    for n in iterable:
        counter += 1
    return counter

print(length([1,2,[3,4]]))
print( length([]))
print( length(("a", 1, 2, None)) )
print(length("oh dear"))