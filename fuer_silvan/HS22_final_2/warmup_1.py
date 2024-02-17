"""Implement a function to_list, which takes an arbitrary object thing and an optional function transform as arguments.
The function to_list should attempt to call Python's built-in list function with thing as the argument and return the
result. If this fails because of any exception, to_list should instead return the value resulting from calling transform
 with thing as the parameter. By default, transform should simply return a list containing the value passed to it as the
 only element.
You may assume that to_list will only be constructed with parameters that match the description. Make sure you correctly
formulate the function signature.
Use the following template:"""

def defult_transfrom(thing):
    return [thing]


def to_list(thing, transform=defult_transfrom):
    try:
        return list(thing)
    except:
        return transform(thing)






print( to_list([1,2,3]) )
print( to_list((1,2,3)) )
print( to_list(1.5) )
print( to_list(True) )
print( to_list(True, lambda x: [int(x)]) )