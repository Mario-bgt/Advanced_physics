def gcd(a, b):
    if a == 0 and b == 0:
        raise ValueError("Both numbers can't be zero")
    a = abs(a)
    b = abs(b)
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    if a < b:
        return gcd(a, b - a)



# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
a = 34
b = 16
print(f"greatest common divisor of {a} and {b} is = {gcd(a, b)}")
print(f"greatest common divisor of {a} and {b} is = {gcd(0, 0)}")
