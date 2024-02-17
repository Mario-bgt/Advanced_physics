Implement a function `merge_dicts` which takes a list of dictionaries `dicts` as a positional argument, plus a keyword argument `reverse_priority`, which should be `False` by default.

The function should return a dictionary resulting from merging all the dictionaries in `dicts`. In other words, the resulting dictionary should contain all items of all dictionaries in `dicts`. If multiple dictionaries in `dicts` contain the same key, then the value contained in the last dictionary containing that key (in terms of order within `dicts`) should take precedence, unless `reverse_priority` is `True`, in which case, the first dictionary containing that key should be used.

 Note that `merge_dicts` should work no matter how many dictionaries are contained in `dicts`.
