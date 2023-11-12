def venn(one, two, three):
    res = one + two
    res = [i for i in res if i in one and i in two]
    res = list(dict.fromkeys(res))
    res = [i for i in res if i not in three]
    return set(res)


print( venn([1, 2, 2, 2, 3, 4], [2, 2, 3, 4], [3]))
print( venn([1.0, "hi", 3], [1.0, 3, "hi"], [3, 1]))
print( venn([1, 2, 3], [4, 5, 6], []))
print( venn([1, 2, 3], [1, 2, 3], [1, 2, 3]))