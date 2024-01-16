"""
Implement two functions encode and decode that work correctly with the following example calls. First, try to
understand what these functions do. Note that decode implements the reverse operations from encode and that each
 function returns three values, which represent the intermediate and final states reached within the respective
 functions. The parameters of each function are the
input string to be encoded and the two modification parameters that influence how the intermediate transformations
 are performed. Your solution should also work if these modification parameters take on any other kind of value of
 the same type as given in the examples, although the second string passed to encode or decode will never be empty.
Use the following template:
"""

def encode(str, code, shift):
    code = code*len(str)
    interm = []
    for i, val in enumerate(str):
        interm.append(val)
        interm.append(code[i])
    final = [ord(c) + shift for c in interm]
    res = "".join([chr(c) for c in final])
    return (interm, final, res)


def decode(str,code,shift):
    interm = [ord(c)-shift for c in str]
    final = [chr(c) for c in interm]
    res = []
    for i, c in enumerate(final):
        if i%2 == 0:
            res.append(c)
    res = "".join(res)
    return ([ord(c) for c in str], final, res)


x =decode("fvcwjxjvmw", "xyz", -2)
print(x)

print(encode("hello", "xyz", -2) ==
 (['h', 'x', 'e', 'y', 'l', 'z', 'l', 'x', 'o', 'y'], [102, 118, 99, 119, 106, 120, 106, 118, 109, 119], 'fvcwjxjvmw'))
print(decode("fvcwjxjvmw", "xyz", -2) ==
 ([102, 118, 99, 119, 106, 120, 106, 118, 109, 119], ['h', 'x', 'e', 'y', 'l', 'z', 'l', 'x', 'o', 'y'], 'hello'))
