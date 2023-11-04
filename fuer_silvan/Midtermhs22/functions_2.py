def add(num):
    def inner(num2):
        return num+num2
    return inner

print(add(3)(10))
print(add(-5)(15))