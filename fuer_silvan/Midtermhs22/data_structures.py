def duplicate_every(l,n):
    res = []
    for i, val in enumerate(l):
        res.append(val)
        if (i+1) % n == 0:
            res.append(val)
    return res

print(duplicate_every([1,2,4, 5],2))
