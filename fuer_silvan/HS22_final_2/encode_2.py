"""Implement two functions encode and decode that work correctly with the following example calls. First, try to
understand what these functions do. Note that decode implements the reverse operations from encode and that each
function returns three values, which represent the intermediate and final states reached within the respective functions.
 The parameters of each function are the
input string to be encoded and the two modification parameters that influence how the intermediate transformations
 are performed. Your solution should also work if these modification parameters take on any other kind of value of the
 same type as given in the examples, although the third parameter will always be a non-empty list of positive numbers.
Use the following template:"""
# Your implementation of the necessary class(es)


def encode(input, key, mod):
    temp_res = [ord(c) + key for c in input]
    print(temp_res)
    mod = mod*len(mod)
    inter_res = []
    for i in range(len(temp_res)):
        inter_res.append(temp_res[i])
        inter_res.append(mod[i])
    final = "".join(chr(i) for i in inter_res)
    return temp_res, inter_res, final


def decode(input, key, mod):
    temp_res = [ord(c) for c in input]
    inter_res = []
    for i in range(len(temp_res)):
        if i%2==0:
            inter_res.append(temp_res[i])
    final = "".join(chr(i - key) for i in inter_res)
    return temp_res, inter_res, final



print(encode("hello", 3, [65,99,120]))
print(decode("kAhcoxoArc", 3, [65,99,120]))

"""
print(encode("hello", 3, [65,99,120]) ==
([107, 104, 111, 111, 114], [107, 65, 104, 99, 111, 120, 111, 65, 114, 99], 'kAhcoxoArc'))
print(decode("kAhcoxoArc", 3, [65,99,120]) ==
([107, 65, 104, 99, 111, 120, 111, 65, 114, 99], [107, 104, 111, 111, 114], 'hello'))

The code above should produce the following output:
True
True
"""