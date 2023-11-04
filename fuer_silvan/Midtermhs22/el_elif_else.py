def normalize(number, lower, upper):
    if number < lower:
        return lower
    elif number > upper:
        return upper
    else:
        return number

print(normalize(1.5, 0, 1))
print(normalize(15,10,20))