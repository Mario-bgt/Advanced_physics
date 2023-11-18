

def ints_divisible_by(ints, by):
    return [i for i in ints if i%by == 0]


print( ints_divisible_by(range(10), 3 ) )
print( ints_divisible_by(range(20), 5 ) )
print( ints_divisible_by([21, 2, 3, 33, 123], 3 ) )