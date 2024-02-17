In the lecture, you learned how Python's data model allows you to supports functionality like `==`, `<=` or `hash(...)`, via methods such as `__eq__`, `__lt__` or `__hash__`. In this task, you will apply this knowledge to implement a class `StringDict`, which largely functions just like a regular dictionary, but coerces all stored values into strings.

The example below shows how after instantiating a `StringDict`, one can set and retrieve values just like with a regular dictionary. However, whenever a value is set, it is immediately converted to a string.

`StringDict` should at least support the following features:

 * setting a value via the bracket notation: `d[key] = value`
 * retrieving a value via the bracket notation: `d[key]`
 * printing: `print(d)`, which should appear the same way as when printing a regular dictionary
 * printing in a collection: `print([d])`, which should appear the same way as when printing a regular dictionary in a collection
 * getting its size: `len(d)`
 * the `in` operator: `123 in d`, which, just like with regular dictionaries, checks if a key is present in the `StringDict`
 * equality: `d1 == d2` and `d1 != d2`
 * providing an optional, regular dictionary upon instantiation; don't forget to convert the values to strings.

It is up to you how you make this happen. `StringDict` does not *need to* support additional functionality that would be supported by regular dictionaries (such as `del(...)`, `iter(...)`, etc.).

*Hint*: The requirements above will make use of the following methods of [Python's data model](https://docs.python.org/3/reference/datamodel.html#object.__len__): `__init__`, `__len__`, `__eq__`, `__str__`, `__repr__`, `__setitem__`, `__getitem__`, `__contains__`.

*Hint*: Remeber that `dict` is a class like any other.

*Important:* Any instance members that aren't methods should be private.
