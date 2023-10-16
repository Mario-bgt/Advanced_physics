#!/usr/bin/env python3

# perform a ROTn encoding
def rot_n(plain_text, shift_by):
    # Make sure to return the correct result!
    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            if plain_text[i].isupper():
                plain_text = plain_text[:i] + chr((ord(plain_text[i]) + shift_by - 65) % 26 + 65) + plain_text[i+1:]
            else:
                plain_text = plain_text[:i] + chr((ord(plain_text[i]) + shift_by - 97) % 26 + 97) + plain_text[i+1:]
    return plain_text

print(rot_n("abc", 1))
