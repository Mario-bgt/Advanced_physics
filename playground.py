#!/usr/bin/env python3

def is_valid(password):
    num_upper = sum([1 for i in password if i.isupper()])
    num_lower = sum([1 for i in password if i.islower()])
    num_digit = sum([1 for i in password if i.isdigit()])
    num_special = sum([1 for i in password if i in ["+", "-", "*", "/"]])
    num_total = len(password)
    if (num_upper+num_lower+num_digit+num_special) != num_total:
        return False
    if num_upper >= 2 and num_lower >= 2 and num_digit >= 2 and num_special >= 2 and num_total >= 8 and num_total <= 16:
        return True
    return

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(is_valid("abAB12+-"))
"""Count the number of lower case characters
Count the number of upper case characters
Count the number of digits
Count the number of characters thar are considered "special"
Count the total number of characters
Check if the numbers from steps 1 to 4 add up to the total number of characters from step 5 
(otherwise it also contains disallowed characters)
Check that the numbers from steps 1 to 5 match the requirements (at least 2 each / between 8-16 total, respectively)
Note that you can do most of these steps using sum() and simple list comprehensions. The is no need for any for loops."""