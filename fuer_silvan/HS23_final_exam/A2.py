def merge_dicts(dicts, reverse_priority=False):
    res = {}
    if reverse_priority:
        dicts = dicts[::-1]

    for d in dicts:
        res.update(d)

    return res




d1 = {1: "a", 2: "b", 3: "c"}
d2 = {1: 1, 20: 2, 300: 3}
d3 = {1: "please", 2: "send", 300: "help"}
print(merge_dicts([d1, d2, d3]))
print(merge_dicts([d1, d2, d3], True))