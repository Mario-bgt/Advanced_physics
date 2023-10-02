#!/usr/bin/env python3
from math import*

def zoo(number):
    # return a tuple containing the required values
    upper = ceil(number)
    lower = floor(number)
    arctan = atan(number)
    frac_int = modf(number)
    minus_inf = nextafter(number, -inf)
    cube = cbrt(number)
    return (lower, upper, arctan, frac_int, minus_inf, cube)

print(zoo(5.7))
