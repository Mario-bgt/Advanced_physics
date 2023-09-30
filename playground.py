a = [1,2,3]
b = [1,2,3]
c = b
if a == c:
    j = b is c
else:
    j = b == c
x =j

print(x, type(x))