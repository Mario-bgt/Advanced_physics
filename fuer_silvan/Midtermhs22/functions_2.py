def add(n):
    def inner(num2):
        return n+num2
    return inner


print(add(3)(10))
func = add(3)
print(func(10))
print(add(-5)(15))
